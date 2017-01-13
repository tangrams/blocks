#!/usr/bin/env python

import sys, glob, os, re, json, yaml
from tools import extractFunctions, appendDependencies
import glslViewer
from docs import appendDoc2README, mainREADME

# ================================== Main functions
# local folder
d='.'

# Sorted list of folders 
folders = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))];
folders.sort()

def benchmarks():
    #   Iterate through all the folders
    for folder in folders:

        # Skip hidden folders (ex.: .git)
        if (folder.startswith('./.')):
            continue

        # That contatin the documentation of all the *.yaml files inside
        for filename in glob.glob(folder+'/*.yaml'):
            block = os.path.splitext(os.path.basename(filename))[0]

            # Skip *-full.yaml
            if block.endswith('-full'):
                continue

            yaml_file = yaml.safe_load(open(filename))

            # For each style ('styles') in this yaml_file 
            for name_block in yaml_file['styles']:
                if 'shaders' in yaml_file['styles'][name_block]:
                    print name_block



# Generate *-full.yaml files... which are blocks that contain their dependencies
def standaloneBlocks():
    #   Iterate through all the folders
    for folder in folders:

        # Skip hidden folders (ex.: .git)
        if (folder.startswith('./.')):
            continue

        # That contatin the documentation of all the *.yaml files inside
        for filename in glob.glob(folder+'/*.yaml'):
            block = os.path.splitext(os.path.basename(filename))[0]

            # Skip *-full.yaml
            if block.endswith('-full'):
                continue

            # Make a *-full.yaml version that contain all dependencies
            full_yaml = dict()
            appendDependencies(full_yaml, filename)
            with open(folder+'/'+block+'-full.yaml', 'w') as yaml_file:
                yaml_file.write( yaml.dump(full_yaml, default_flow_style=False, indent=4))

# Generates READMES
def document():
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
                continue

            toc_styles = appendDoc2README(readme_file, filename, counter)
            counter += 1

            # Keep track of the folder structor for making an toc
            if not folder[2:] in toc:
                toc[folder[2:]] = dict()
                toc[folder[2:]][block] = toc_styles
            else:
                toc[folder[2:]][block] = toc_styles

        readme_file.close()
        # Keep track of all the README.md to construct a big main one
        readmes.append(readme)

    # Agregate all previus READMEs into a big main one
    mainREADME(readmes)

    # Compose a toc.json with the structure of the blocks
    sorted(toc)
    with open('toc.json', 'w') as outfile:
        json.dump(toc, outfile)


if len(sys.argv) > 1:
    if sys.argv[1] == 'docs':
        document()
    elif sys.argv[1] == 'standalones':
        standaloneBlocks()
    elif sys.argv[1] == 'benchmarks':
        benchmarks()
else:
    benchmarks()
    document()
    standaloneBlocks()