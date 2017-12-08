#python cleanfailed.py LHE/FCC secret
#python cleanfailed.py LHE/FCC_fcc_v01 secret
#python cleanfailed.py LHE/FCC_cms secret

import json
import os
import os.path
import sys

import EventProducer.common.isreading as isr

if "secret" in sys.argv:
    import EventProducer.config.param_test as para
    secret=True
else:
    import EventProducer.config.param as para


if len(sys.argv)>4 or len(sys.argv)<2:
    print 'usage: python cleanfailed.py FCC or LHE'
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
            os.system('rm -rf %s'%(mydict[s][j]['out']))

        else: mynewdict[s].append(mydict[s][j])
        
with open(indict, 'w') as f:
    json.dump(mynewdict, f)

readdic.comparedics(nf=nfailed, ns=0)
readdic.finalize()
