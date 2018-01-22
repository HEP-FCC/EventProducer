#python jobchecker.py LHE or FCC
import json
import subprocess
import sys
import os.path

import EventProducer.config.param as para
import EventProducer.common.isreading as isr

class removeProcess():


#__________________________________________________________
    def __init__(self, indict, inread, process, indir):
        self.indict = indict
        self.inread = inread
        self.process = process
        self.indir = indir
        if os.path.isfile(self.indict)==False:
            print 'dictonary does not exists '
            sys.exit(3)

        self.readdic=isr.isreading(self.inread, self.indict)
        self.readdic.backup('removeProcess')
        self.readdic.reading()


#__________________________________________________________
    def remove(self):
        mydict=None
        with open(self.indict) as f:
            mydict = json.load(f)

        mynewdict={}
        for element in mydict:
            if self.process == str(element):
                print self.process,'    ',str(element)
                continue
            else:
                mynewdict[element]=mydict[element]

        with open(self.indict, 'w') as f:
            json.dump(mynewdict, f)

        self.readdic.comparedics(nf=0,ns=1)
        self.readdic.finalize()


        import os
        print 'remove process in eos'
        cmd="rm %s/%s/events*"%(self.indir, self.process)
        print cmd
        os.system(cmd)
