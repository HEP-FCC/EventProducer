#python jobchecker.py LHE or FCC
import json
import subprocess
import sys
import os.path
import ROOT as r

import EventProducer.config.param as para
import EventProducer.common.isreading as isr

print len(sys.argv)
if len(sys.argv)!=2:
    print 'usage: python common/baddone.py LHE'
    exit(3)

indict=''
inread=''
if sys.argv[1]=='LHE':
    indict=para.lhe_dic
    inread=para.readlhe_dic
else:
    print 'unrecognized mode ',sys.argv[1],'  possible values are LHE'
    sys.exit(3)

if os.path.isfile(indict)==False:
    print 'dictonary does not exists '
    sys.exit(3)

readdic=isr.isreading(inread, indict)
readdic.backup('baddone')
readdic.reading()

mydict=None
with open(indict) as f:
    mydict = json.load(f)

for s in mydict:
    print 'process  ',s

    for j in mydict[s]:
        
        if j['status'] == 'bad':
            cmd='ls %s'%(j['out'])
            p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
            p.wait()
            print cmd
            if len(p.stderr.readline())==0: 
                if p.stdout.readline().split()[0]==j['out'].split('/')[-1]:
                    if '.root' not in j['out']:
                        filecounting='filecounting'
                        if os.path.isdir(filecounting)==False:
                            os.system('mkdir %s'%filecounting)
                        cmd='cp %s %s'%(j['out'],filecounting)
                        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
                        stdout,stderr = p.communicate()
                        if os.path.isfile('%s/%s'%(filecounting,j['out'].split('/')[-1])):
                            os.system('gunzip %s/%s'%(filecounting,j['out'].split('/')[-1]))
                            cmd='grep \"<event>\" %s/%s | wc -l'%(filecounting,j['out'].split('/')[-1].replace('.gz',''))
                            p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
                            stdout,stderr = p.communicate()
                            stdoutplit=stdout.split(' ')
                            print int(stdoutplit[0])
                            j['nevents']=int(stdoutplit[0])
                            j['status']='done'
                            os.system('rm %s/%s'%(filecounting,j['out'].split('/')[-1].replace('.gz','')))


with open(indict, 'w') as f:
    json.dump(mydict, f)


readdic.comparedics()
readdic.finalize()
    
