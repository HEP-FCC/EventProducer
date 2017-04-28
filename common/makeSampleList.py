#!/usr/bin/env python

# this script updates param.py with matching efficiencies and produces two files:
# - "heppySampleList.py" contains the list of FCCSW root files properly formatted for heppy
# - "procDict.json" contains a skimmed dictionary containing information for physics analysis

import subprocess, glob
import json, param
import ast, os

import re

version = 'v0_0'

eosdir = 'root://eospublic.cern.ch/'

lhe = '/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json'
fcc = '/afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_{}.json'.format(version)

lheDict=None
with open(lhe) as f:
   lheDict = json.load(f)

fccDict=None
with open(fcc) as f:
   fccDict = json.load(f)

nmatched = 0
nlhe = 0
njobs = 0

# write header for heppy file
procDict = open('tmp.json', 'w')
procDict.write('{\n')

# write header for heppy file
heppyFile = open('heppySampleList.py', 'w')
heppyFile.write('import heppy.framework.config as cfg\n')
heppyFile.write('\n')

# write paramfile
paramFile = 'param.py'
# parse param file
with open(paramFile) as f:
    infile = f.readlines()

for process in fccDict:
   nmatched = 0
   nlhe = 0
   njobs = 0

   heppyFile.write('{} = cfg.MCComponent(\n'.format(process))
   heppyFile.write("    \'{}\',\n".format(process))
   heppyFile.write('    files=[\n')

   print ''
   print '------ ', process, '-------------'
   print ''
   
   # extract cross-section from param file
   if process not in param.gridpacklist:
       print 'process :', process, 'not found in param.py --> skipping process'
       heppyFile.write(']\n')
       heppyFile.write(')\n')
       heppyFile.write('\n')
       continue
   else: 
       xsec = float(param.gridpacklist[process][3])
   # compute matching efficiency
   for jobfcc in fccDict[process]:
       if jobfcc['nevents']>0 and jobfcc['status']== 'done':
           for joblhe in lheDict[process]:
               if joblhe['jobid'] == jobfcc['jobid'] and joblhe['status']== 'done':
                   nlhe += joblhe['nevents']
                   nmatched+=jobfcc['nevents']
                   njobs+=1
                   
                   # add file to heppy sample list 
                   heppyFile.write("           '{}/{}',\n".format(eosdir,jobfcc['out']))
                   break
   # skip process if do not find corresponding lhes
   if nlhe == 0:
       print 'did not find any LHE event for process', process
       heppyFile.write(']\n')
       heppyFile.write(')\n')
       heppyFile.write('\n')
       continue
   if nmatched == 0:
       print 'did not find any FCCSW event for process', process
       heppyFile.write(']\n')
       heppyFile.write(')\n')
       heppyFile.write('\n')
       continue

   # compute matching efficiency
   matchingEff = round(float(nmatched)/nlhe, 3)
   entry = '   "{}": {{"numberOfEvents": {}, "crossSection": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, xsec, matchingEff)
   print 'N: {}, xsec: {} pb, eff: {}'.format(nmatched, xsec, matchingEff)
   
   procDict.write(entry)
   
   # parse new param file
   with open(paramFile) as f:
       lines = f.readlines()
       for line in xrange(len(lines)):
           if process == lines[line].rsplit(':', 1)[0].replace("'", ""):
               ll = ast.literal_eval(lines[line].rsplit(':', 1)[1][:-2])	        
               infile[line] = "'{}':['{}','{}','{}','{}','{}'],\n".format(process, ll[0],ll[1],ll[2],ll[3], matchingEff)

   with open("tmp.py", "w") as f1:
       f1.writelines(infile)

   heppyFile.write(']\n')
   heppyFile.write(')\n')
   heppyFile.write('\n')


procDict.close()
# parse param file

# strip last comma
with open('tmp.json', 'r') as myfile:
    data=myfile.read()
    newdata = data[:-2]

# close header for heppy file
procDict = open('procDict.json', 'w')
procDict.write(newdata)
procDict.write('\n')
procDict.write('}\n')

# replace existing param.py file
os.system("mv tmp.py param.py")



