#python cleanfailed.py LHE/FCC secret
#python cleanfailed.py LHE/FCC_fcc_v01 secret
#python cleanfailed.py LHE/FCC_cms secret

import yaml
import os
import glob
import os.path
import sys


class cleanfailed():

#__________________________________________________________
    def __init__(self, indir, yamldir, process):
        self.indir = indir+'/'+process
        self.yamldir = yamldir+'/'+process
        self.process = process
#__________________________________________________________
    def clean(self):
        nfailed=0
        ldir=[x[0] for x in os.walk(self.yamldir)]
        print ldir
       
        for l in ldir:
      
            All_files = glob.glob("%s/events_*.yaml"%l)
            if len(All_files)==0:continue
            keys=l.split('/')
            if keys[-1]!='':process=keys[-1]
            else:process=keys[len(keys)-2]            
            print 'process from the input directory ',process
            if self.process!='' and self.process!=process: 
                continue

            for f in All_files:
                if not os.path.isfile(f): 
                    print 'file does not exists... %s'%f
                    continue
                
                with open(f, 'r') as stream:
                    try:
                       tmpf = yaml.load(stream)
                       if tmpf['processing']['status']=='BAD':
                           nfailed+=1
                           cmd="rm %s"%(tmpf['processing']['out'])
                           print cmd
                           os.system(cmd)

                           cmd="rm %s"%(f)
                           print cmd
                           os.system(cmd)

                    except yaml.YAMLError as exc:
                        print(exc)

   
