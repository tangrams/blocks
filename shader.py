#!/usr/bin/env python
import os, time, sys, urllib, re

# http://eyalarubas.com/python-subproc-nonblock.html
from subprocess import Popen, PIPE
from time import sleep
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read

class Shader:
    COMMAND='glslViewer'
    TMP_DIR='/tmp/'
    process = {}
    cout = {}
    wait_time = 0.0001
    time = 0.
    delta = 0.
    fps = 0
    generated_file = ''

    def __init__(self, filename, options = {}):
        # Compose a shader file
        
        if 'template' in options:
            self.generated_file = filename
            shader_file = open(filename, "w")
            with open(options['template']) as f:
                if 'pragmas' in options:
                    for line in f:
                        matches = re.findall('\\#pragma tangram:\\s+([\\w|]*)\\n', line)
                        if len(matches):
                            if options['pragmas'].has_key(matches[0]):
                                shader_file.write(options['pragmas'][matches[0]])
                        else:
                            shader_file.write(line)
                else:
                    # TODO: make sense of this case
                    for line in f:
                        shader_file.write(line)
            shader_file.close()

        # compose and excecute a glslViewer command
        cmd = [self.COMMAND]
        cmd.append(filename)

        if options.has_key('size'):
            cmd.append('-w')
            cmd.append(str(options['size']))
            cmd.append('-h')
            cmd.append(str(options['size']))

        if options.has_key('headless'):
            cmd.append('--headless')

        if options.has_key('output'):
            cmd.append('-o')
            cmd.append(options['output'])

        tex_counter=0
        if options.has_key('textures'):
            for uniform_name in options['textures'].keys():
                url = options['textures'][uniform_name]
                ext = os.path.splitext(url)[1]
                img_path = self.TMP_DIR + str(tex_counter) + ext
                http = urllib.URLopener()
                http.retrieve(url, img_path)
                cmd.append('-' + uniform_name)
                cmd.append(img_path);
        
        # print 'EXE ',  ' '.join(cmd)
        self.process = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False)
        flags = fcntl(self.process.stdout, F_GETFL) # get current self.process.stdout flags
        fcntl(self.process.stdout, F_SETFL, flags | O_NONBLOCK)
        # self.cout = NonBlockingStreamReader(self.process)

    def read(self):
        while True:
            try:
                return read(self.process.stdout.fileno(), 1024).rstrip() 
            except OSError:
                return 'none'

    def isFinish(self):
        return self.process.poll() is not None

    def getTime(self):
        self.process.stdin.write('time\n')
        sleep(self.wait_time)
        answer = self.read()
        if answer:
            if answer.replace('.','',1).isdigit():
                self.time = float(answer)
        return self.time
        
    def getDelta(self):
        self.process.stdin.write('delta\n')
        sleep(self.wait_time)
        answer = self.read()
        if answer:
            if answer.replace('.','',1).isdigit():
                self.delta = float(answer)
        return self.delta


    def getFPS(self):
        return self.process.stdin.write('fps\n')
        sleep(self.wait_time)
        answer = self.read()
        if answer:
            if answer.replace('.','',1).isdigit():
                self.fps = float(answer)
        return self.fps

    def stop(self):
        self.process.stdin.write('exit\n')
        while not self.isFinish():
            sleep(1)
        # print "Finish"
        # self.process.kill()
        # if len(self.generated_file):
            # os.remove(self.generated_file)
