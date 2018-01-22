#python cleanfailed.py LHE/FCC secret
#python cleanfailed.py LHE/FCC_fcc_v01 secret
#python cleanfailed.py LHE/FCC_cms secret

import json
import os
import os.path
import sys
import EventProducer.common.isreading as isr


class cleanfailed():

#__________________________________________________________
    def __init__(self, indict, inread, process):
        self.indict = indict
        self.inread = inread
        self.process = process
        if os.path.isfile(self.indict)==False:
            print 'dictonary does not exists '
            sys.exit(3)


        self.readdic=isr.isreading(self.inread, self.indict)
        self.readdic.backup('cleanfailed')
        self.readdic.reading()

#__________________________________________________________
    def clean(self):
        nfailed=0
        mydict=None
        mynewdict={}
        user=os.environ['USER']
        with open(self.indict) as f:
            mydict = json.load(f)
        for s in mydict:
            mynewdict[s]=[]
            if self.process != '' and self.process != s: 
                mynewdict[s]=mydict[s]
                continue
            for j in xrange(len(mydict[s])):
                if mydict[s][j]['status']=='BAD'and user in (mydict[s][j]['user']): 
                    print 'job failed ',j,'  ',mydict[s][j]['out']
                    nfailed+=1
                    os.system('rm %s'%(mydict[s][j]['out']))
            
                else: mynewdict[s].append(mydict[s][j])
        
        with open(self.indict, 'w') as f:
            json.dump(mynewdict, f)

        self.readdic.comparedics(nf=nfailed, ns=0)
        self.readdic.finalize()
