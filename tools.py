import os, re, yaml

def extractFunctions(searchText):
    return re.findall("((void|bool|int|float|vec\\d|mat\\d)\\s(((?!=).)*)(\\(.*\\)))", searchText)

def isDocumentationIn(yaml_block):
    return 'doc' in yaml_block

def isDescriptionIn(yaml_block):
    if isDocumentationIn(yaml_block):
        return 'description' in yaml_block['doc']
    return False

def getDescriptionOf(yaml_block):
    if isDescriptionIn(yaml_block):
        return yaml_block['doc']['description'] + '\n'
    else:
        return ''

def isShaderIn(yaml_block):
    return 'shaders' in yaml_block

def isShaderBlocksIn(yaml_block):
    if isShaderIn(yaml_block):
        return 'blocks' in yaml_block['shaders']
    return False

def isGlobalBlockIn(yaml_block):
    if isShaderBlocksIn(yaml_block):
        return 'global' in yaml_block['shaders']['blocks']

def getGlobalBlockIn(yaml_block):
    if isGlobalBlockIn(yaml_block):
        return "\n"+yaml_block['shaders']['blocks']['global']
    return ""

def getGlobalFunctionsIn(yaml_block):
    return extractFunctions(getGlobalBlockIn(yaml_block))

def isNormalBlockIn(yaml_block):
    if isShaderBlocksIn(yaml_block):
        return 'global' in yaml_block['shaders']['normal']

def getNormalBlockIn(yaml_block):
    if isNormalBlockIn(yaml_block):
        return "\n"+yaml_block['shaders']['blocks']['normal']
    return ""

def isColorBlockIn(yaml_block):
    if isShaderBlocksIn(yaml_block):
        return 'global' in yaml_block['shaders']['color']

def getColorBlockIn(yaml_block):
    if isColorBlockIn(yaml_block):
        return "\n"+yaml_block['shaders']['blocks']['color']
    return ""

def isFilterBlockIn(yaml_block):
    if isShaderBlocksIn(yaml_block):
        return 'global' in yaml_block['shaders']['filter']

def getFilterBlockIn(yaml_block):
    if isFilterBlockIn(yaml_block):
        return "\n"+yaml_block['shaders']['blocks']['filter']
    return ""

def isUniformsIn(yaml_block):
    return 'uniforms' in yaml_block['shaders']

def isDefinesIn(yaml_block):
    return 'defines' in yaml_block['shaders']

def getDefinesIn(yaml_block):
    if isDefinesIn(yaml_block):
        return yaml_block['shaders']['defines'].keys()
    return []

def isUniformsIn(yaml_block):
    return 'uniforms' in yaml_block['shaders']

def getUniformsIn(yaml_block):
    if isUniformsIn(yaml_block):
        return yaml_block['shaders']['uniforms'].keys()
    return []

def uniformHaveMetadata(uniform_name, yaml_block):
    if 'ui' in yaml_block:
        if 'shaders' in yaml_block['ui']:
            if 'uniforms' in yaml_block['ui']['shaders']:
                if uniform_name in yaml_block['ui']['shaders']['uniforms']:
                    return True
    return False

def defineHaveMetadata(define_name, yaml_block):
    if 'ui' in yaml_block:
        if 'shaders' in yaml_block['ui']:
            if 'defines' in yaml_block['ui']['shaders']:
                if define_name in yaml_block['ui']['shaders']['defines']:
                    return True
    return False

def isTestIn(yaml_block):
    return 'test' in yaml_block

def isExamplesIn(yaml_block):
    if isDocumentationIn(yaml_block):
        return 'examples' in yaml_block['doc']
    return False

def isDependenceIn(yaml_block):
    return 'mix' in yaml_block

def getDependencesIn(yaml_block):
    if isDependenceIn(yaml_block):
        if isinstance(yaml_block['mix'], (str, unicode)):
            return [yaml_block['mix']]
        else:
            return yaml_block['mix']
    return []

def collectDefines(yaml_file, block_name, defines_dict):
    block = yaml_file['styles'][block_name]
    depts = getDependencesIn(block)
    for dep_block_name in depts:
        collectDefines(yaml_file, dep_block_name, defines_dict)

    defines = getDefinesIn(block)
    for define_name in defines:
        defines_dict[define_name] = block['shaders']['defines'][define_name]

def getAllGlobals(yaml_file, block_name):
    rta = ""
    depts = getDependencesIn(yaml_file['styles'][block_name])
    for dep_block_name in depts:
        rta += getAllGlobals(yaml_file, dep_block_name)
    rta += getGlobalBlockIn(yaml_file['styles'][block_name])
    return rta

# Recursive dict merge (From https://gist.github.com/angstwad/bf22d1822c38a92ec0a9)
def dict_merge(dct, merge_dct):
    """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.
    :param dct: dict onto which the merge is executed
    :param merge_dct: dct merged into dct
    :return: None
    """
    for k, v in merge_dct.iteritems():
        if (k in dct and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], dict)):
            dict_merge(dct[k], merge_dct[k])
        else:
            dct[k] = merge_dct[k]

# Append yaml dependences in yaml_file ('import' files) to another yaml file (full_yaml_file)
def appendDependencies(full_yaml, filename):
    # print "Append all dependences of " + filename
    folder = os.path.dirname(filename)
    yaml_file = yaml.safe_load(open(filename))

    dict_merge(full_yaml, yaml_file)

    if 'import' in yaml_file:
        if (type(yaml_file['import']) is str):
            dep = folder + '/' + yaml_file['import']
            # print "\tMerging " + dep
            appendDependencies(full_yaml, dep)
        else:
            for file in yaml_file['import']:
                dep = folder + '/' + file
                # print "\tMerging " + dep
                appendDependencies(full_yaml, dep)

# From https://github.com/adafruit/Adafruit_Python_GPIO/blob/master/Adafruit_GPIO/Platform.py
def isRPi():
    """Detect the version of the Raspberry Pi.  Returns either 1, 2 or
    None depending on if it's a Raspberry Pi 1 (model A, B, A+, B+),
    Raspberry Pi 2 (model B+), or not a Raspberry Pi.
    """
    # Check /proc/cpuinfo for the Hardware field value.
    # 2708 is pi 1
    # 2709 is pi 2
    # Anything else is not a pi.
    try:
        with open('/proc/cpuinfo', 'r') as infile:
            cpuinfo = infile.read()
            # Match a line like 'Hardware   : BCM2709'
            match = re.search('^Hardware\s+:\s+(\w+)$', cpuinfo, flags=re.MULTILINE | re.IGNORECASE)
            if not match:
                # Couldn't find the hardware, assume it isn't a pi.
                return None
            if match.group(1) == 'BCM2708':
                # Pi 1
                return True
            elif match.group(1) == 'BCM2709':
                # Pi 2
                return True
            else:
                # Something else, not a pi.
                return False
    except:
        return False