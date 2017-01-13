import os, re, yaml

def extractFunctions(searchText):
    return re.findall("((void|bool|int|float|vec\\d|mat\\d)+\\s.*\\(.*\\)\\s+\\{)", searchText)

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