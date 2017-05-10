import os,subprocess
import EventProducer.config.param as para

for gp in para.gridpacklist:
    cmd="/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls %s%s.tar.gz"%(para.gp_dir,gp)
    p=subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout,stderr = p.communicate()
    if len(stderr)!=0:
        print 'GP %s does not exist'%gp
