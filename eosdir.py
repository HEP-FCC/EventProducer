import os
import subprocess
import param as param
import glob

for pr in param.griddic:
    cmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select mkdir %s%s'%(param.outdir,pr)
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    p.wait()

    cmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select mkdir %s%s'%(param.indir,pr)
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    p.wait()

    for ht in param.griddic[pr]:
        cmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select mkdir %s%s/%s'%(param.outdir,pr,ht.replace('.tar.gz',''))
        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        p.wait()
        
        listcopy=glob.glob('LxplusCompiled/%s/*'%(pr))
        for l in listcopy:
            cmd='/usr/bin/xrdcp %s root://eospublic.cern.ch/%s%s/%s '%(l,param.indir,pr,l.split('/')[-1])
            
            p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            p.wait()
        
