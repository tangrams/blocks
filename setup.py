#!/usr/bin/env python

import sys, glob, os, re, json, yaml
from tools import *
from docs import *
from benchmark import *

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

# ================================== Main functions
# local folder
d='.'

# Sorted list of folders 
folders = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))];
folders.sort()

def benchmarks():
    print "Benchmarking on the PI"
    #   Iterate through all the folders
    for folder in folders:

        # Skip hidden folders (ex.: .git)
        if (folder.startswith('./.')):
            continue

        # That contatin the documentation of all the *.yaml files inside
        for filename in glob.glob(folder+'/*.yaml'):
            block_filename = os.path.splitext(os.path.basename(filename))[0]

            # Skip *-full.yaml
            if block_filename.endswith('-full'):
                continue

            yaml_file = yaml.safe_load(open(filename))
            logs = dict()
            # For each style ('styles') in this yaml_file 
            for block_name in yaml_file['styles']:
                block = yaml_file['styles'][block_name]

                if isTestIn(block):
                    for test_name in block['test']:
                        if not logs.has_key(block_name):
                            logs[block_name] = dict()

                        logs[block_name][test_name] = benchmark(filename, block_name, block, test_name)

                # If there is benchmarks save them in json
                if len(logs.keys()):
                    with open(folder+'/'+block_name+'.json', 'w') as outfile:
                        json.dump(logs, outfile)

                    # Make a chart
                    fig, ax = plt.subplots(nrows=1, ncols=1)
                    legends = []
                    for block_name in yaml_file['styles']:
                        for log_name in logs[block_name]:
                            legends.append(log_name)
                            ax.plot(logs[block_name][log_name]['samples'], 
                                    logs[block_name][log_name]['values'])

                    plt.legend(legends, loc='upper left')
                    fig.savefig(folder+'/'+block_name+'.png')   # save the figure to file
                    plt.close(fig)

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
    standaloneBlocks()
    if isRPi():
        benchmarks()
    document()
    