import os, yaml
from shader import *
from tools import *

RECORD_FROM = 1.
DURATION = 2. # sec

SHADER_HEAD = """
#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
"""

SHADER_MAIN = """
void main() {
    vec2 st = gl_FragCoord.xy/u_resolution;
    vec4 color = vec4(vec3(0.),1.);
"""

SHADER_FOOT = """
    gl_FragColor = color;
}
"""

def benchmark(yaml_filename, block_name, block, test_name):
    folder = os.path.dirname(yaml_filename)
    name_yaml = os.path.basename(yaml_filename);
    name, ext = os.path.splitext(name_yaml)
    text_code = getTest(test_name, block)
    shader_path = folder+'/'+name+'-'+test_name+'.frag'
    shader_output_path = name+'-'+test_name+'.png'

    # Collect global functions and defines
    standalone_yaml = yaml.safe_load(open(folder+'/'+name+'-full.yaml'))
    globals = getAllGlobals(standalone_yaml, block_name)
    defines_dict = {}
    collectDefines(standalone_yaml, block_name, defines_dict)
    defines = ""
    for define_name in defines_dict.keys():
        defines += "\n#define " + define_name + " " + str(defines_dict[define_name]) + '\n'
    
    # Compose a shader file
    shader_file = open(shader_path, "w")
    shader_file.write(SHADER_HEAD)
    shader_file.write(defines)
    shader_file.write(globals)
    shader_file.write(SHADER_MAIN)
    shader_file.write(text_code)
    shader_file.write(SHADER_FOOT)
    shader_file.close()

    # Test it! 
    log = dict()
    shader = Shader(shader_path, {'output':shader_output_path})
    time_start = time.time()

    log['values'] = []
    log['samples'] = []
    old_value = 0.0
    while True:
        time_now = time.time()
        time_diff = time_now - time_start
        if time_diff >= RECORD_FROM:
            if time_diff >= DURATION or shader.isFinish():
                break
            value = float(shader.getDelta())
            if not value == old_value:
                log['values'].append(value)
                log['samples'].append(time_diff)
                # print str(time_diff)+','+str(value)
    shader.stop()
    log['average'] = sum(log['values'])/float(len(log['values']))
    log['output'] = shader_output_path;
    os.remove(shader_path)

    return log

    # import matplotlib as mpl
    # mpl.use('Agg')
    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots( nrows=1, ncols=1 )
    # ax.plot(samples, values)
    # fig.savefig(benchmark_path)   # save the figure to file
    # plt.close(fig)
    