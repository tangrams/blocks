#!/usr/bin/env python

import glob, os, yaml, re

d='.'
folders = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))];
folders.sort()

def extractFunctions(searchText):
    return re.findall("((void|bool|int|float|vec\\d|mat\\d)+\\s.*\\(.*\\)\\s+\\{)", searchText)

readmes = []

# FOLDER
for folder in folders:
    readme = folder+'/README.md'
    readme_file = open(readme, "w")

    for filename in glob.glob(folder+'/*.yaml'):
        yaml_file = yaml.safe_load(open(filename))
        for name_block in yaml_file['styles']:
            url = 'https://github.com/tangrams/blocks/blob/gh-pages'+filename[1:]

            readme_file.write('\n\n### [' + name_block + ']('+url+')\n\n');

            if 'doc' in yaml_file['styles'][name_block]:
                if 'description' in yaml_file['styles'][name_block]['doc']:
                    readme_file.write(yaml_file['styles'][name_block]['doc']['description']+'\n')

            if 'shaders' in yaml_file['styles'][name_block]:
                if 'blocks' in yaml_file['styles'][name_block]['shaders']:
                    readme_file.write('This provides the following blocks:\n');

                    for block in yaml_file['styles'][name_block]['shaders']['blocks'].keys():
                        readme_file.write('\n- **' + block + '**:')

                        if block == 'global':
                            functions = extractFunctions(yaml_file['styles'][name_block]['shaders']['blocks'][block])
                            for function in functions:
                                readme_file.write('\n + `' + function[0][:-1] + '`')
                        else:
                            readme_file.write(  '\n\n```glsl\n' + 
                                                yaml_file['styles'][name_block]['shaders']['blocks'][block] +
                                                '\n```\n\n')
                if 'defines' in yaml_file['styles'][name_block]['shaders']:
                    readme_file.write('\n\nThis block use the following **defines** with the following defaults. Remember you can use or tweak.\n')
                    for define in yaml_file['styles'][name_block]['shaders']['defines'].keys():
                        readme_file.write(' - **' + define + '**: ```' + str(yaml_file['styles'][name_block]['shaders']['defines'][define]) + '```\n')

                if 'uniforms' in yaml_file['styles'][name_block]['shaders']:
                    readme_file.write('\n\nThis block use the following **uniforms** with the following defaults. Remember you can use or tweak.\n')
                    for uniform in yaml_file['styles'][name_block]['shaders']['uniforms'].keys():
                        readme_file.write(' - **' + uniform + '**: ```' + str(yaml_file['styles'][name_block]['shaders']['uniforms'][uniform]) + '```\n')

            readme_file.write(  '\n\nImport it using:\n\n' +
                                '```yaml\n' +
                                'import:\n' +
                                '    - http://tangrams.github.io/blocks/' + filename[2:] + '\n' +
                                '```\n\n')

            readme_file.write('\n')
    readme_file.close()
    readmes.append(readme)
    
with open('README.md', 'w') as outfile:
    with open('INTRO.md') as infile:
            outfile.write(infile.read())

    for fname in readmes:
        with open(fname) as infile:
            outfile.write(infile.read())

    outfile.write('\n## License\n')
    with open('LICENSE.md') as infile:
            outfile.write(infile.read())

