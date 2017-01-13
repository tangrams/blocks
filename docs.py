import os, yaml
from tools import *

URL = 'http://tangrams.github.io/blocks/'

def mainREADME(readmes):
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

def appendDoc2README(readme_file, filename, counter):
    toc_of_blocks = []
    yaml_file = yaml.safe_load(open(filename))

    # For each style ('styles') in this yaml_file 
    for block_name in yaml_file['styles']:
        block = yaml_file['styles'][block_name]

        if counter != 0:
            readme_file.write('\n![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)\n')

        # Add a title that points to github
        readme_file.write('\n\n#### [' + block_name + ']('+URL+'#'+block_name+') <a href="https://github.com/tangrams/blocks/blob/gh-pages'+filename[1:]+'" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>\n\n');
        toc_of_blocks.append(block_name) 

        # Add a description if it have
        if isDocumentationIn(block):
            readme_file.write(getDescriptionOf(block))

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

        if isShaderIn(block):
            readme_file.write('These blocks uses a custom **shader**.\n');
            shader = block['shaders']

            # Add a list of uniforms
            if isUniformsIn(block):
                readme_file.write('These are the **uniforms**:\n')
                for uniform_name in shader['uniforms'].keys():
                    uniform_doc = ' **' + uniform_name + '**: '
                    
                    # Add extra information from the UI 
                    if uniformHaveMetadata(uniform_name, block):
                        uniform_metadata = block['ui']['shaders']['uniforms'][uniform_name]

                        uniform_label = uniform_metadata['label'].lower()
                        if uniform_metadata['type'] == 'number':
                            uniform_doc += ' number between ```' + str(uniform_metadata['range']['min']) + '``` and ```' + str(uniform_metadata['range']['max']) + '``` that control the *' + uniform_label + '*.'
                        
                        elif uniform_metadata['type'] == 'dropdownArray':
                            uniform_doc += ' variable that control the *' + uniform_label + '* with one of the following values: ```'
                            uniform_doc += ', '.join(uniform_metadata['values']) + '```.'

                        elif uniform_metadata['type'] == 'dropdownList':
                            uniform_doc += ' variable that control the *' + uniform_label + '* with one of the following values: '
                            uniform_values = []
                            for key, value in uniform_metadata['values'].iteritems():
                                uniform_values.append('```'+value+'``` ( *' + key + '* )')
                            uniform_doc += ', '.join(uniform_values) + '.'

                    uniform_doc += ' The *default value* is ```' + str(shader['uniforms'][uniform_name]) + '```. '
                    readme_file.write(' - ' + uniform_doc + '\n')

                readme_file.write('\n')

            # Add a list of defines
            if isDefinesIn(block):
                readme_file.write('These are the **defines**:\n')
                for define_name in shader['defines'].keys():
                    define_doc = ' **' + define_name + '**: ' # name
                    
                    # Add extra information from the UI 
                    if defineHaveMetadata(define_name, block):
                        define_metadata = block['ui']['shaders']['defines'][define_name]
                        define_label = define_metadata['label'].lower()
                        if define_metadata['type'] == 'number':
                            define_doc += ' number between ```' + str(define_metadata['range']['min']) + '``` and ```' + str(define_metadata['range']['max']) + '``` that control the *' + define_label + '*.'
                        
                        elif define_metadata['type'] == 'dropdownArray':
                            define_doc += ' variable that control the *' + define_label + '* with one of the following values: ```'
                            define_doc += ', '.join(define_metadata['values']) + '```.'
                        
                        elif define_metadata['type'] == 'dropdownList':
                            define_doc += ' variable that control the *' + define_label + '* with one of the following values: '
                            define_values = []
                            for key, value in define_metadata['values'].iteritems():
                                define_values.append('```'+value+'``` ( *' + key + '* )')
                            define_doc += ', '.join(define_values) + '.'
                
                    define_doc += ' The *default value* is ```' + str(shader['defines'][define_name]) + '```. '
                    readme_file.write(' - ' + define_doc + '\n')

                readme_file.write('\n')

            # Add a list of blocks
            if isShaderBlocksIn(block):
                readme_file.write('These are the **shader blocks**:\n');

                global_fncs = getGlobalFunctionsIn(block)
                if len(global_fncs):
                    readme_file.write('\n- **global**:')
                    for function in global_fncs:
                        readme_file.write('\n + `' + function[0]+ '`')

                for block_type in block['shaders']['blocks'].keys():
                    # In case of a 'global' block... just list the functions it contain
                    if block_type != 'global':
                        readme_file.write('\n- **' + block_type + '**:')
                        readme_file.write(  '\n\n```glsl\n' + 
                                            block['shaders']['blocks'][block_type] +
                                            '\n```\n\n')
                readme_file.write('\n')

        # Add a list of examples
        if isExamplesIn(block):
            readme_file.write('\nExamples:\n');
            for example in block['doc']['examples']:
                if 'url' in block['doc']['examples'][example]:
                    url = 'https://mapzen.com/tangram/play/?scene=' + block['doc']['examples'][example]['url']
                    if 'lines' in block['doc']['examples'][example]:
                        url = url + '&lines=' + str(block['doc']['examples'][example]['lines'])
                    if 'img' in block['doc']['examples'][example]:
                        readme_file.write('<a href="'+url+'" target="_blank">\n<img src="'+block['doc']['examples'][example]['img']+'" style="width: 100%; height: 100px; object-fit: cover;">\n</a>\n')

                    else:
                        readme_file.write('<a href="'+url+'" target="_blank">'+example+'</a>\n')

    return toc_of_blocks