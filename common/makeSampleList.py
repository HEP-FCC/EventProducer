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

#______________________________________________________________________________________________________
def addEntry(process, processlhe, xsec, kf, lheDict, fccDict, heppyFile, procDict):
   
   nmatched = 0
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
                   njobs+=1

                   # add file to heppy sample list 
                   heppyFile.write("           '{}/{}',\n".format(eosdir,jobfcc['out']))
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
   entry = '   "{}": {{"numberOfEvents": {}, "crossSection": {}, "kfactor": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, xsec, kf, matchingEff)
   print 'N: {}, xsec: {} , kf: {} pb, eff: {}'.format(nmatched, xsec, kf, matchingEff)

   procDict.write(entry)

   return matchingEff

#_______________________________________________________________________________________________________
if __name__=="__main__":

    eosdir = 'root://eospublic.cern.ch/'

    heppyList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/heppySampleList.py'
    procList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/procDict.json'

    lhe = para.lhe_dic
    fcc = para.fcc_dic

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
           if dec in process:
               br = para.branching_ratios[dec]
               decay = dec
       if br < 1.0 and decay != '':
           decstr = '_{}'.format(decay)
           proc_param = process.replace(decstr,'')
           xsec = float(para.gridpacklist[proc_param][3])*br
           kf = float(para.gridpacklist[proc_param][4])
           matchingEff = addEntry(process, proc_param, xsec, kf, lheDict, fccDict, heppyFile, procDict)

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
