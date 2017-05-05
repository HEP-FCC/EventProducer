import os.path
import subprocess
import sys

import EventProducer.common.dicwriter as dicr
import EventProducer.config.param as para

mydict=dicr.dicwriter('/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict_recreate.json')
process=''
if len(sys.argv)>1:
    process=sys.argv[1]

for pr in para.gridpacklist:
    if process!='' and process!=pr:continue
    print pr
    filecounting='filecounting'
    if os.path.isdir(filecounting)==False:
        os.system('mkdir %s'%filecounting)

    cmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls %s%s'%(para.lhe_dir,pr)
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    stdout,stderr = p.communicate()

    print 'n files =',len(stdout.split('\n'))
    for f in stdout.split('\n'):
        cmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select cp %s%s/%s %s'%(para.lhe_dir,pr,f,filecounting)
        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        stdout,stderr = p.communicate()
        if os.path.isfile('%s/%s'%(filecounting,f)):
            os.system('gunzip %s/%s'%(filecounting,f))
            cmd='grep \"<event>\" %s/%s | wc -l'%(filecounting,f.replace('.gz',''))
            p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
            stdout,stderr = p.communicate()
            stdoutplit=stdout.split(' ')
            
            nevents=int(stdoutplit[0])
            os.system('rm %s/%s'%(filecounting,f.replace('.gz','')))

            if nevents%1000!=0:
                dic = {'sample':pr, 
                       'jobid':int(f.replace('events','').replace('.lhe.gz','')),
                       'nevents':nevents,
                       'status':'bad',
                       'out':'%s%s/%s'%(para.lhe_dir,pr,f)
                       }
                mydict.addjob_new(dic)
                print 'BAD FILE============',f,'==========   ',nevents
            else:
                dic = {'sample':pr, 
                       'jobid':int(f.replace('events','').replace('.lhe.gz','')),
                       'nevents':nevents,
                       'status':'done',
                       'out':'%s%s/%s'%(para.lhe_dir,pr,f)
                       }
                mydict.addjob_new(dic)
                print f,'   ',nevents

    mydict.write()
