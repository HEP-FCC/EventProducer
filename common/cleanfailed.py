#python cleanfailed.py /afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json
import json
import os
import os.path
import sys

import EventProducer.config.param as para
import EventProducer.common.isreading as isr

if len(sys.argv)!=2:
    print 'usage: python cleanfailed.py FCC or LHE'
    exit(3)

indict=''
inread=''
if sys.argv[1]=='LHE':
    indict=para.lhe_dic
    inread=para.readlhe_dic
elif sys.argv[1]=='FCC':
    indict=para.fcc_dic
    inread=para.readfcc_dic
else:
    print 'unrecognized mode ',sys.argv[1],'  possible values are FCC or LHE'
    sys.exit(3)

if os.path.isfile(indict)==False:
    print 'dictonary does not exists '
    sys.exit(3)


readdic=isr.isreading(inread, indict)
readdic.backup('cleanfailed')
readdic.reading()
nfailed=0
mydict=None
mynewdict={}
with open(indict) as f:
    mydict = json.load(f)
for s in mydict:
    mynewdict[s]=[]
    for j in xrange(len(mydict[s])):
        if mydict[s][j]['status']=='failed': 
            print 'job failed ',j,'  ',mydict[s][j]['script']
            nfailed+=1
            os.system('rm -rf %s'%(mydict[s][j]['script']))
            os.system('rm -rf %s'%(mydict[s][j]['log']))
        else: mynewdict[s].append(mydict[s][j])
        
with open(indict, 'w') as f:
    json.dump(mynewdict, f)

readdic.comparedics(nf=nfailed)
readdic.finalize()
