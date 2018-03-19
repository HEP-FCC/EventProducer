#python jobchecker.py LHE or FCC
import EventProducer.common.utils as ut
import os, sys

class removeProcess():

#__________________________________________________________
    def __init__(self, process, indir, yamldir):
        self.process = process
        self.indir = indir
        self.yamldir = yamldir

        if not ut.dir_exist(indir+'/'+process):
            print 'process eos does not exist, exit ',indir+'/'+process
            sys.exit(3)
        if not ut.dir_exist(yamldir+'/'+process):
            print 'process yaml does not exist, exit ',yamldir+'/'+process
            sys.exit(3)


#__________________________________________________________
    def remove(self):
        
        
        print 'remove process in eos'
        cmd="rm %s/%s/events*"%(self.indir, self.process)
        print cmd
        os.system(cmd)
        print 'remove process in yaml'
        cmd="rm %s/%s/events*"%(self.yamldir, self.process)
        print cmd
        os.system(cmd)
        print 'remove merged yaml'
        cmd="rm %s/%s/merge.yaml"%(self.yamldir, self.process)
        print cmd
        os.system(cmd)

