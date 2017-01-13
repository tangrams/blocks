import os, re, yaml

def extractFunctions(searchText):
    # return re.findall("((void|bool|int|float|vec\\d|mat\\d)+\\s.*\\(.*\\)\\s+\\{)", searchText)
    return re.findall("((void|bool|int|float|vec\\d|mat\\d)\\s(((?!=).)*)\\(.*\\))", searchText)

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

def getGlobalFunctions(yaml_block):
    if isGlobalBlockIn(yaml_block):
        return extractFunctions(yaml_block['shaders']['blocks']['global'])
    return []

def isUniformsIn(yaml_block):
    return 'uniforms' in yaml_block['shaders']

def isDefinesIn(yaml_block):
    return 'defines' in yaml_block['shaders']

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



def isExamplesIn(yaml_block):
    if isDocumentationIn(yaml_block):
        return 'examples' in yaml_block['doc']
    return False

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