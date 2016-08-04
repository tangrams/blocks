#!/usr/bin/env python

import sys, glob, os, re, json, yaml

URL = 'http://tangrams.github.io/blocks/'

def extractFunctions(searchText):
    return re.findall("((void|bool|int|float|vec\\d|mat\\d)+\\s.*\\(.*\\)\\s+\\{)", searchText)

def appendDocumentation(readme_file, filename, counter):
    blocks = []
    yaml_file = yaml.safe_load(open(filename))

    # For each style ('styles') in this yaml_file 
    for name_block in yaml_file['styles']:

        if counter != 0:
            readme_file.write('\n![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)\n')

        # Add a title that points to github
        readme_file.write('\n\n#### [' + name_block + ']('+URL+'#'+name_block+') <a href="https://github.com/tangrams/blocks/blob/gh-pages'+filename[1:]+'" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>\n\n');

        blocks.append(name_block)

        # Add a description if it have
        if 'doc' in yaml_file['styles'][name_block]:
            if 'description' in yaml_file['styles'][name_block]['doc']:
                readme_file.write(yaml_file['styles'][name_block]['doc']['description']+'\n')

        # Add an explanation of how to import this block
        readme_file.write(  '\n\nTo import this block add the following url to your `import` list:\n\n' +
                            '```yaml\n' +
                            'import:\n' +
                            '    - https://tangrams.github.io/blocks/' + filename[2:] + '\n' +
                            '```\n\n\n')

        # Add an explanation of how to import this block with dependencies
        readme_file.write(  '\n\nIf you want to import this block together **with their dependencies** use this other url:\n\n' +
                            '```yaml\n' +
                            'import:\n' +
                            '    - https://tangrams.github.io/blocks/' + filename[2:-5] + '-full.yaml\n' +
                            '```\n\n\n')

        if 'shaders' in yaml_file['styles'][name_block]:
            readme_file.write('These blocks uses a custom **shader**.\n');

            # Add a list of uniforms
            if 'uniforms' in yaml_file['styles'][name_block]['shaders']:
                readme_file.write('These are the **uniforms**:\n')
                for uniform in yaml_file['styles'][name_block]['shaders']['uniforms'].keys():
                    uniform_doc = ' **' + uniform + '**: '
                    
                    # Add extra information from the UI 
                    if 'ui' in yaml_file['styles'][name_block]:
                        if 'shaders' in yaml_file['styles'][name_block]['ui']:
                            if 'uniforms' in yaml_file['styles'][name_block]['ui']['shaders']:
                                if uniform in yaml_file['styles'][name_block]['ui']['shaders']['uniforms']:
                                    if yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['type'] == 'number':
                                        uniform_min = yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['range']['min']
                                        uniform_max = yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['range']['max']
                                        uniform_label = yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['label'].lower()
                                        uniform_doc += ' number between ```' + str(uniform_min) + '``` and ```' + str(uniform_max) + '``` that control the *' + uniform_label + '*.'
                                    
                                    elif yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['type'] == 'dropdownArray':
                                        uniform_label = yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['label'].lower()
                                        uniform_doc += ' variable that control the *' + uniform_label + '* with one of the following values: ```'
                                        uniform_doc += ', '.join(yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['values']) + '```.'

                                    elif yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['type'] == 'dropdownList':
                                        uniform_label = yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['label'].lower()
                                        uniform_doc += ' variable that control the *' + uniform_label + '* with one of the following values: '
                                        uniform_values = []
                                        for key, value in yaml_file['styles'][name_block]['ui']['shaders']['uniforms'][uniform]['values'].iteritems():
                                            uniform_values.append('```'+value+'``` ( *' + key + '* )')

                                        uniform_doc += ', '.join(uniform_values) + '.'

                    uniform_doc += ' The *default value* is ```' + str(yaml_file['styles'][name_block]['shaders']['uniforms'][uniform]) + '```. '

                    readme_file.write(' - ' + uniform_doc + '\n')
                readme_file.write('\n')

            # Add a list of defines
            if 'defines' in yaml_file['styles'][name_block]['shaders']:
                readme_file.write('These are the **defines**:\n')
                for define in yaml_file['styles'][name_block]['shaders']['defines'].keys():
                    define_doc = ' **' + define + '**: ' # name
                    
                    # Add extra information from the UI 
                    if 'ui' in yaml_file['styles'][name_block]:
                        if 'shaders' in yaml_file['styles'][name_block]['ui']:
                            if 'defines' in yaml_file['styles'][name_block]['ui']['shaders']:
                                if define in yaml_file['styles'][name_block]['ui']['shaders']['defines']:
                                    if yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['type'] == 'number':
                                        define_min = yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['range']['min']
                                        define_max = yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['range']['max']
                                        define_label = yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['label'].lower()
                                        define_doc += ' number between ```' + str(define_min) + '``` and ```' + str(define_max) + '``` that control the *' + define_label + '*.'
                                    
                                    elif yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['type'] == 'dropdownArray':
                                        define_label = yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['label'].lower()
                                        define_doc += ' variable that control the *' + define_label + '* with one of the following values: ```'
                                        define_doc += ', '.join(yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['values']) + '```.'
                                    
                                    elif yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['type'] == 'dropdownList':
                                        define_label = yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['label'].lower()
                                        define_doc += ' variable that control the *' + define_label + '* with one of the following values: '
                                        define_values = []
                                        for key, value in yaml_file['styles'][name_block]['ui']['shaders']['defines'][define]['values'].iteritems():
                                            define_values.append('```'+value+'``` ( *' + key + '* )')

                                        define_doc += ', '.join(define_values) + '.'
                
                    define_doc += ' The *default value* is ```' + str(yaml_file['styles'][name_block]['shaders']['defines'][define]) + '```. '

                    readme_file.write(' - ' + define_doc + '\n')
                readme_file.write('\n')

            # Add a list of blocks
            if 'blocks' in yaml_file['styles'][name_block]['shaders']:
                readme_file.write('These are the **shader blocks**:\n');

                if 'global' in yaml_file['styles'][name_block]['shaders']['blocks']:
                    readme_file.write('\n- **global**:')
                    functions = extractFunctions(yaml_file['styles'][name_block]['shaders']['blocks']['global'])
                    for function in functions:
                        readme_file.write('\n + `' + function[0][:-1] + '`')

                for block in yaml_file['styles'][name_block]['shaders']['blocks'].keys():
                    # In case of a 'global' block... just list the functions it contain
                    if block != 'global':
                        readme_file.write('\n- **' + block + '**:')
                        readme_file.write(  '\n\n```glsl\n' + 
                                            yaml_file['styles'][name_block]['shaders']['blocks'][block] +
                                            '\n```\n\n')
                readme_file.write('\n')

        # Add a list of examples
        if 'doc' in yaml_file['styles'][name_block]:
            if 'examples' in yaml_file['styles'][name_block]['doc']:
                readme_file.write('\nExamples:\n');
                for example in yaml_file['styles'][name_block]['doc']['examples']:
                    if 'url' in yaml_file['styles'][name_block]['doc']['examples'][example]:
                        url = 'https://mapzen.com/tangram/play/?scene=' + yaml_file['styles'][name_block]['doc']['examples'][example]['url']
                        if 'lines' in yaml_file['styles'][name_block]['doc']['examples'][example]:
                            url = url + '&lines=' + str(yaml_file['styles'][name_block]['doc']['examples'][example]['lines'])
                        if 'img' in yaml_file['styles'][name_block]['doc']['examples'][example]:
                            readme_file.write('<a href="'+url+'" target="_blank">\n<img src="'+yaml_file['styles'][name_block]['doc']['examples'][example]['img']+'" style="width: 100%; height: 100px; object-fit: cover;">\n</a>\n')

                        else:
                            readme_file.write('<a href="'+url+'" target="_blank">'+example+'</a>\n')

    return blocks

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

# ================================== Main functions
# local folder
d='.'

# Sorted list of folders 
folders = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))];
folders.sort()

def cleanAll():
    print "CLEAN ALL *-full.yaml"
    os.system("rm -R */*-full.yaml") 

    print "CLEAN ALL README.md"
    os.system("rm README.md") 
    os.system("rm -R */README.md") 

def makeAll():
    print "MAKE ALL"

    # List to append all folder README.md files to compose a big main README.md file
    readmes = []
    toc = dict()

    #   Iterate through all the folders
    for folder in folders:

        # Skip hidden folders (ex.: .git)
        if (folder.startswith('./.')):
            continue

        # Make a README.md file per folder
        readme = folder+'/README.md'
        readme_file = open(readme, "w")

        counter = 0
        toc_blocks = []
        # That contatin the documentation of all the *.yaml files inside
        for filename in glob.glob(folder+'/*.yaml'):
            block = os.path.splitext(os.path.basename(filename))[0]

            # Skip *-full.yaml
            if block.endswith('-full'):
                print "Skipping " + block
                continue

            toc_styles = appendDocumentation(readme_file, filename, counter)
            counter += 1

            # Keep track of the folder structor for making an toc
            if not folder[2:] in toc:
                toc[folder[2:]] = dict()
                toc[folder[2:]][block] = toc_styles
            else:
                toc[folder[2:]][block] = toc_styles

            # Make a *-full.yaml version that contain all dependencies
            full_yaml = dict()
            appendDependencies(full_yaml, filename)
            with open(folder+'/'+block+'-full.yaml', 'w') as yaml_file:
                yaml_file.write( yaml.dump(full_yaml, default_flow_style=False, indent=4))
            

        readme_file.close()
        # Keep track of all the README.md to construct a big main one
        readmes.append(readme)

    # Compose a toc.json with the structure of the blocks
    sorted(toc)
    with open('toc.json', 'w') as outfile:
        json.dump(toc, outfile)

    # Compose a the BIG main README.md
    with open('README.md', 'w') as outfile:
        # Add the intro 
        with open('INTRO.md') as infile:
                outfile.write(infile.read())

        # Content
        # Add all folder README.md one after the other 
        outfile.write('\n## Blocks description\n<hr>\n')
        for fname in readmes:
            with open(fname) as infile:
                folder = os.path.dirname(fname)[2:]

                outfile.write('\n\n### [' + folder.upper() + ']('+URL+'#'+folder+') <a href="https://github.com/tangrams/blocks/blob/gh-pages/'+folder+'" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>')
                outfile.write(infile.read())
                outfile.write('\n![](https://mapzen.com/common/styleguide/images/divider/compass-lg-red.png)\n')

        # Add the License at the end
        with open('LICENSE.md') as infile:
                outfile.write(infile.read())

if len(sys.argv) > 1:
    if sys.argv[1] == 'clean':
        cleanAll()
    elif sys.argv[1] == 'all':
        makeAll()
else:
    makeAll()