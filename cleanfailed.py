#python cleanfailed.py /afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json
import json
import os
import os.path
import sys

if len(sys.argv)!=2:
    print 'usage: python cleanfailed.py indict.json'
    exit(3)

indict=sys.argv[1]
if os.path.isfile(indict)==False:
    print 'dictonary does not exists '
    exit(3)

mydict=None
mynewdict={}
with open(indict) as f:
    mydict = json.load(f)
for s in mydict:
    mynewdict[s]=[]
    for j in xrange(len(mydict[s])):
        if mydict[s][j]['status']=='failed': 
            print 'job failed ',j,'  ',mydict[s][j]['script']
            os.system('rm -rf %s'%(mydict[s][j]['script']))
            os.system('rm -rf %s'%(mydict[s][j]['log']))
        else: mynewdict[s].append(mydict[s][j])
        
with open(indict, 'w') as f:
    json.dump(mynewdict, f)
