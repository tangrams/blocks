#!/usr/bin/env python
import glob, os, yaml, re

def extractFunctions(searchText):
    return re.findall("((void|bool|int|float|vec\\d|mat\\d)+\\s.*\\(.*\\)\\s+\\{)", searchText)

def appendDocumentation(readme_file, yaml_file):
    # For each style ('styles') in this yaml_file 
    for name_block in yaml_file['styles']:

        # Add a title that points to github
        url = 'https://github.com/tangrams/blocks/blob/gh-pages'+filename[1:]
        readme_file.write('\n\n#### + [' + name_block + ']('+url+')\n\n');

        # Add a description if it have
        if 'doc' in yaml_file['styles'][name_block]:
            if 'description' in yaml_file['styles'][name_block]['doc']:
                readme_file.write(yaml_file['styles'][name_block]['doc']['description']+'\n')

        if 'shaders' in yaml_file['styles'][name_block]:
            # Add a list of blocks
            if 'blocks' in yaml_file['styles'][name_block]['shaders']:
                readme_file.write('This provides the following blocks:\n');

                for block in yaml_file['styles'][name_block]['shaders']['blocks'].keys():
                    readme_file.write('\n- **' + block + '**:')

                    # In case of a 'global' block... just list the functions it contain
                    if block == 'global':
                        functions = extractFunctions(yaml_file['styles'][name_block]['shaders']['blocks'][block])
                        for function in functions:
                            readme_file.write('\n + `' + function[0][:-1] + '`')
                    else:
                        readme_file.write(  '\n\n```glsl\n' + 
                                            yaml_file['styles'][name_block]['shaders']['blocks'][block] +
                                            '\n```\n\n')
            # Add a list of defines
            if 'defines' in yaml_file['styles'][name_block]['shaders']:
                readme_file.write('\n\nThis block use the following **defines** with the following defaults. Remember you can use or tweak.\n')
                for define in yaml_file['styles'][name_block]['shaders']['defines'].keys():
                    readme_file.write(' - **' + define + '**: ```' + str(yaml_file['styles'][name_block]['shaders']['defines'][define]) + '```\n')

            # Add a list of uniforms
            if 'uniforms' in yaml_file['styles'][name_block]['shaders']:
                readme_file.write('\n\nThis block use the following **uniforms** with the following defaults. Remember you can use or tweak.\n')
                for uniform in yaml_file['styles'][name_block]['shaders']['uniforms'].keys():
                    readme_file.write(' - **' + uniform + '**: ```' + str(yaml_file['styles'][name_block]['shaders']['uniforms'][uniform]) + '```\n')

        # Add an explanation of how to import this block
        readme_file.write(  '\n\nImport it using:\n\n' +
                            '```yaml\n' +
                            'import:\n' +
                            '    - http://tangrams.github.io/blocks/' + filename[2:] + '\n' +
                            '```\n\n\n')

# https://gist.github.com/angstwad/bf22d1822c38a92ec0a9
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

# ================================== Main function

# local folder
d='.'

# Sorted list of folders 
folders = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))];
folders.sort()

# List to append all folder README.md files to compose a big main README.md file
readmes = []
#   Iterate through all the folders
for folder in folders:

    # Skip hidden folders (ex.: .git)
    if (folder.startswith('./.')):
        continue

    # Make a README.md file per folder
    readme = folder+'/README.md'
    readme_file = open(readme, "w")

    # That contatin the documentation of all the *.yaml files inside
    for filename in glob.glob(folder+'/*.yaml'):
        block = os.path.splitext(os.path.basename(filename))[0]

        # Skip *-full.yaml
        if block.endswith('-full'):
            print "Skipping " + block
            continue

        yaml_file = yaml.safe_load(open(filename))
        appendDocumentation(readme_file, yaml_file)

        # Make a *-full.yaml version that contain all dependencies
        full_yaml = dict()
        appendDependencies(full_yaml, filename)
        with open(folder+'/'+block+'-full.yml', 'w') as yaml_file:
            yaml_file.write( yaml.dump(full_yaml, default_flow_style=False, indent=4))
        
        
    readme_file.close()
    # Keep track of all the README.md to construct a big main one
    readmes.append(readme)

# Compose a the BIG main README.md
with open('README.md', 'w') as outfile:
    # Add the intro 
    with open('INTRO.md') as infile:
            outfile.write(infile.read())

    # Add all folder README.md one after the other 
    for fname in readmes:
        with open(fname) as infile:
            folder = os.path.dirname(fname)[2:]
            outfile.write("\n<hr>\n")
            outfile.write("\n\n### [" + folder.upper() +"](https://github.com/tangrams/blocks/tree/gh-pages/"+folder+")")
            outfile.write(infile.read())

    # Add the License at the end
    outfile.write('\n## License\n')
    with open('LICENSE.md') as infile:
            outfile.write(infile.read())