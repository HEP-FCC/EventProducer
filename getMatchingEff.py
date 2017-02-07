#!/usr/bin/env python
import json
import subprocess
import sys
import os.path

'''if len(sys.argv) < 1:
  print " Usage: python getMatchingEfficiency.py process"
  sys.exit(1)

process = sys.argv[1]'''

lhe = '/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json'
fcc = '/afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json'

lheDict=None
with open(lhe) as f:
   lheDict = json.load(f)

fccDict=None
with open(fcc) as f:
   fccDict = json.load(f)

nmatched = 0
nlhe = 0
njobs = 0

for process in fccDict:
   nmatched = 0
   nlhe = 0
   njobs = 0

   for jobfcc in fccDict[process]:
       if jobfcc['nevents']>0 and jobfcc['status']== 'done':
           for joblhe in lheDict[process]:
               if joblhe['jobid'] == jobfcc['jobid'] and joblhe['status']== 'done':
                   nlhe += joblhe['nevents']
                   nmatched+=jobfcc['nevents']
                   njobs+=1
                   break

   print  '============================================'
   print  ''
   print  'process:                    ', process
   print  'number of matched events  : ', nmatched
   print  'number of generated events: ', nlhe
   print  '----------------------------------' 
   if(nlhe > 0):
       print  'matching efficiency:        ', round(float(nmatched)/nlhe, 3)
   else: 
       print  'no events found for this process...'
   print  ''
