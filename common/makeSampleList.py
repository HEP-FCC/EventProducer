#!/usr/bin/env python

# this script updates param.py with matching efficiencies and produces two files:
# - "heppySampleList.py" contains the list of FCCSW root files properly formatted for heppy
# - "procDict.json" contains a skimmed dictionary containing information for physics analysis

import subprocess, glob
import json, time, datetime
import ast, os
import collections
import re
import EventProducer.config.param as para
import sys
#______________________________________________________________________________________________________
def addEntry(process, processlhe, xsec, kf, lheDict, fccDict, heppyFile, procDict):
   
   nmatched = 0
   nweights = 0
   nlhe = 0
   njobs = 0
   
   heppyFile.write('{} = cfg.MCComponent(\n'.format(process))
   heppyFile.write("    \'{}\',\n".format(process))
   heppyFile.write('    files=[\n')

   matchingEff = 1.0

   for jobfcc in fccDict[process]:
       if jobfcc['nevents']>0 and jobfcc['status']== 'done':
           for joblhe in lheDict[processlhe]:
               if int(joblhe['jobid']) == jobfcc['jobid'] and joblhe['status']== 'done':
                   nlhe += int(joblhe['nevents'])
                   nmatched+=jobfcc['nevents']
                   try:
                       nweights+=int(jobfcc['nweights'])
                   except KeyError, e:
                       nweights+=0
                   njobs+=1

                   # add file to heppy sample list 
                   heppyFile.write("           'root://eospublic.cern.ch/{}',\n".format(jobfcc['out']))
                   break

   heppyFile.write(']\n')
   heppyFile.write(')\n')
   heppyFile.write('\n')

   # skip process if do not find corresponding lhes
   if nlhe == 0:
       print 'did not find any LHE event for process', process
       return matchingEff
       
   if nmatched == 0:
       print 'did not find any FCCSW event for process', process
       return matchingEff

   # compute matching efficiency
   matchingEff = round(float(nmatched)/nlhe, 3)
   if nweights==0: nweights=nmatched
   entry = '   "{}": {{"numberOfEvents": {}, "sumOfWeights": {}, "crossSection": {}, "kfactor": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, nweights, xsec, kf, matchingEff)
   print 'N: {}, Nw:{}, xsec: {} , kf: {} pb, eff: {}'.format(nmatched, nweights, xsec, kf, matchingEff)

   procDict.write(entry)

   return matchingEff

#______________________________________________________________________________________________________
def addEntryPythia(process, xsec, kf, fccDict, heppyFile, procDict):
   
   heppyFile.write('{} = cfg.MCComponent(\n'.format(process))
   heppyFile.write("    \'{}\',\n".format(process))
   heppyFile.write('    files=[\n')     

   nmatched = 0
   nweights = 0
   njobs = 0
   matchingEff = 1.0

   for jobfcc in fccDict[process]:
       if jobfcc['nevents']>0 and jobfcc['status']== 'done':
           nmatched+=jobfcc['nevents']
           try:
               nweights+=int(jobfcc['nweights'])
           except KeyError, e:
               nweights+=0
           njobs+=1
           heppyFile.write("           '{}',\n".format(jobfcc['out']))

   heppyFile.write(']\n')
   heppyFile.write(')\n')
   heppyFile.write('\n')
       
   if nmatched == 0:
       print 'did not find any FCCSW event for process', process
       return matchingEff

   if nweights==0: nweights=nmatched
   entry = '   "{}": {{"numberOfEvents": {}, "sumOfWeights": {}, "crossSection": {}, "kfactor": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, nweights, xsec, kf, matchingEff)
   print 'N: {}, Nw:{}, xsec: {} , kf: {} pb, eff: {}'.format(nmatched, nweights, xsec, kf, matchingEff)
   procDict.write(entry)
   return matchingEff
   
#_______________________________________________________________________________________________________
if __name__=="__main__":


    heppyList = ''
    procList = ''
    fcc=''
    lhe=''
    version=sys.argv[1]
    if version not in para.fcc_versions:
        print 'version of the cards should be: fcc_v01, cms'
        print '======================%s======================'%version
        sys.exit(3)
    else:
        fcc=para.fcc_dic.replace('VERSION',version)
        heppyList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/heppySampleList_%s.py'%version
        procList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/procDict_%s.json'%version
        lhe = para.lhe_dic


    # make backups
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
    user = os.environ['USER']

    suffix = '_{}_{}'.format(user,st)
    heppyListbk = '{}_{}'.format(heppyList,suffix)
    procListbk = '{}_{}'.format(procList,suffix)

    os.system('cp {} {}'.format(heppyList, heppyListbk))
    os.system('cp {} {}'.format(procList, procListbk))

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
    heppyFile = open(heppyList, 'w')
    heppyFile.write('import heppy.framework.config as cfg\n')
    heppyFile.write('\n')

    # write paramfile
    paramFile = 'config/param.py'
    # parse param file
    with open(paramFile) as f:
        infile = f.readlines()

    process_list = fccDict.keys()
    process_list.sort()

    # start loop over fcc dict 
    for process in process_list:

       print ''
       print '------ ', process, '-------------'
       print ''

       # maybe this was a decayed process, so it cannot be found as such in in the param file
       br = 1.0
       decay = ''
       for dec in para.branching_ratios:
           dec_proc = process.split('_')[-1]
           if dec in process and dec_proc == dec:
               br = para.branching_ratios[dec]
               decay = dec
       if br < 1.0 and decay != '':
           print 'decay---------- '
           decstr = '_{}'.format(decay)
           proc_param = process.replace(decstr,'')
           print '--------------  ',decstr,'  --  ',proc_param
           xsec = float(para.gridpacklist[proc_param][3])*br
           kf = float(para.gridpacklist[proc_param][4])
           matchingEff = addEntry(process, proc_param, xsec, kf, lheDict, fccDict, heppyFile, procDict)

       elif process in para.pythialist:
           xsec = float(para.pythialist[process][3])
           kf = float(para.pythialist[process][4])
           matchingEff = addEntryPythia(process, xsec, kf, fccDict, heppyFile, procDict)

       elif process not in para.gridpacklist:
           print 'process :', process, 'not found in param.py --> skipping process'
           continue
       else: 
           xsec = float(para.gridpacklist[process][3])
           kf = float(para.gridpacklist[process][4])
           matchingEff = addEntry(process, process, xsec, kf, lheDict, fccDict, heppyFile, procDict)
           # parse new param file
           with open(paramFile) as f:
               lines = f.readlines()
               isgp=False
               for line in xrange(len(lines)):
                   if 'gridpacklist' in str(lines[line]): isgp=True
                   if isgp==False: continue
                   if process == lines[line].rsplit(':', 1)[0].replace("'", ""):
                       ll = ast.literal_eval(lines[line].rsplit(':', 1)[1][:-2])                
                       infile[line] = "'{}':['{}','{}','{}','{}','{}','{}'],\n".format(process, ll[0],ll[1],ll[2],ll[3],ll[4], matchingEff)

           with open("tmp.py", "w") as f1:
               f1.writelines(infile)

    procDict.close()
    # parse param file

    # strip last comma
    with open('tmp.json', 'r') as myfile:
        data=myfile.read()
        newdata = data[:-2]

    # close header for heppy file
    procDict = open(procList, 'w')
    procDict.write(newdata)
    procDict.write('\n')
    procDict.write('}\n')

    # replace existing param.py file
    os.system("mv tmp.py config/param.py")
