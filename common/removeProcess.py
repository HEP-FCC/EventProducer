#python jobchecker.py LHE or FCC
import json
import subprocess
import sys
import os.path
import ROOT as r

import EventProducer.config.param as para
import EventProducer.common.isreading as isr

if len(sys.argv)!=3:
    print 'usage: python removeProcess.py LHE/FCC_fcc_v01/FCC_cms process'
    exit(3)

indict=''
inread=''
if sys.argv[1]=='LHE':
    indict=para.lhe_dic
    inread=para.readlhe_dic
elif 'FCC_' in sys.argv[1]:
    version=sys.argv[1].replace('FCC_','')
    if version not in para.fcc_versions:
        print 'version of the cards should be: fcc_v01, cms'
        print '======================%s======================'%version
        sys.exit(3)
    indict=para.fcc_dic.replace('VERSION',version)
    inread=para.readfcc_dic.replace('VERSION',version)
else:
    print 'unrecognized mode ',sys.argv[1],'  possible values are LHE/FCC'
    sys.exit(3)

if os.path.isfile(indict)==False:
    print 'dictonary does not exists '
    sys.exit(3)

process=sys.argv[2]

readdic=isr.isreading(inread, indict)
readdic.backup('removeProcess')
readdic.reading()

#indict='/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict_REMOVE_OUT.json'

mydict=None
with open(indict) as f:
    mydict = json.load(f)

mynewdict={}

for element in mydict:
    if process == str(element):
        print process,'    ',str(element)
        continue
    else:
        mynewdict[element]=mydict[element]

with open(indict, 'w') as f:
    json.dump(mynewdict, f)

readdic.comparedics(nf=0,ns=1)
readdic.finalize()
    
