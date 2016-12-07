import json
import os


mydict=None
mynewdict={}
with open('/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json') as f:
    mydict = json.load(f)
for s in mydict:
    mynewdict[s]=[]
    for j in xrange(len(mydict[s])):
        if mydict[s][j]['status']=='failed': 
            print 'job failed ',j,'  ',mydict[s][j]['script']
            os.system('rm -rf %s'%(mydict[s][j]['script']))
            os.system('rm -rf %s'%(mydict[s][j]['log']))
        else: mynewdict[s].append(mydict[s][j])
        
with open('/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json', 'w') as f:
    json.dump(mynewdict, f)
