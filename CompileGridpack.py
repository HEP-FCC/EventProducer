#! /usr/bin/env python


import subprocess
import time

import sys, optparse, os, re

parser = optparse.OptionParser(usage ="""
    usage: %prog gridpack1.tar.gz gridpack2.tar.gz ...
    
    Compiles gridpacks and then repackages them.
     """)

opts, args = parser.parse_args()
if len(args) < 1:
    parser.print_help()
    sys.exit(1)

for gridpack in args:

    # generate and package grid pack
    subprocess.call('tar -xf ' + gridpack, shell=True)
    subprocess.call('cd ./madevent; ./bin/compile', shell=True)
    subprocess.call('cd ./madevent; ./bin/clean4grid', shell=True)
    subprocess.call('tar --remove-files -czf ' + gridpack + ' madevent run.sh', shell=True)
    os.system('rm -rf ./madevent README.gridpack')





