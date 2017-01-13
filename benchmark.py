import yaml
import glslViewer
from tools import *

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

    # Collect global functions and defines
    standalone_yaml = yaml.safe_load(open(folder+'/'+name+'-full.yaml'))
    globals = getAllGlobals(standalone_yaml, block_name)
    defines_dict = {}
    collectDefines(standalone_yaml, block_name, defines_dict)
    defines = ""
    for define_name in defines_dict.keys():
        defines += "\n#define " + define_name + " " + str(defines_dict[define_name]) + '\n'
    
    # Compose a shader file
    shader_file = open(folder+'/'+name+'-'+test_name+'.frag', "w")
    shader_file.write(SHADER_HEAD)
    shader_file.write(defines)
    shader_file.write(globals)
    shader_file.write(SHADER_MAIN)
    shader_file.write(text_code)
    shader_file.write(SHADER_FOOT)
    shader_file.close()

    # Test it! 
    