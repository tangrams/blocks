import os, yaml, re
from shader import *
from tools import *

import numpy as np 

RECORD_FROM = 1.
DURATION = 2. # sec
TEMPLATE = 'benchmark_template.frag'

def benchmark(yaml_filename, block_name, block, test_name):
    folder = os.path.dirname(yaml_filename)
    name_yaml = os.path.basename(yaml_filename);
    name, ext = os.path.splitext(name_yaml)

    shader_path = folder+'/'+name+'-'+test_name+'.frag'
    shader_output_path = name+'-'+test_name+'.png'

    pragmas = {}

    # Collect testing blocks
    if 'blocks' in block['test'][test_name]:
        for b_name in block['test'][test_name]['blocks']:
            pragmas[b_name] = block['test'][test_name]['blocks'][b_name]

    # Collect global functions and defines
    standalone_yaml = yaml.safe_load(open(folder+'/'+name+'-full.yaml'))
    pragmas['global'] = getAllGlobals(standalone_yaml, block_name)
    defines_dict = {}
    collectDefines(standalone_yaml, block_name, defines_dict)

    # Add / overwrite defines with test defines
    if 'defines' in block['test'][test_name]:
        for d_name in block['test'][test_name]['defines']:
            defines_dict[b_name] = block['test'][test_name]['defines'][d_name]

    # Add defines into a single block of text for pragma injection
    pragmas['defines'] = ''
    for define_name in defines_dict.keys():
        pragmas['defines'] += "\n#define " + define_name + " " + str(defines_dict[define_name]) + '\n'

    # Test it! 
    shader = Shader(shader_path, {'template': TEMPLATE, 'pragmas': pragmas, 'output':shader_output_path})
    time_start = time.time()

    values = []
    samples = []
    old_value = 0.0
    while True:
        time_now = time.time()
        time_diff = time_now - time_start
        if time_diff >= RECORD_FROM:
            if time_diff >= DURATION or shader.isFinish():
                break
            value = float(shader.getDelta())
            # if not value == old_value:
            values.append(value)
            samples.append(time_diff)
                # print str(time_diff)+','+str(value)
    shader.stop()

    log = dict()
    log['values'] = values
    log['samples'] = samples
    log['mean'] = np.mean(log['values'])
    log['median'] = np.median(log['values'])
    log['output'] = shader_output_path;

    return log
    