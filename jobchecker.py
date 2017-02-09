#python jobchecker.py /afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json
import json
import subprocess
import sys
import os.path
import ROOT as r

force=False


if len(sys.argv)>3:
    print 'usage: python jobchecker.py indict.json process'
    exit(3)

indict=sys.argv[1]
if os.path.isfile(indict)==False:
    print 'dictonary does not exists '
    exit(3)

inprocess=''
if len(sys.argv)==3:
    inprocess=t=sys.argv[2]

mydict=None
with open(indict) as f:
    mydict = json.load(f)
firstprocess=True
for s in mydict:
    evttot=0
    njobs=0

    if inprocess!='':
        if inprocess!=s: continue

    for j in mydict[s]:

        if force==False:

            if (j['status']== 'done' or j['status']== 'bad')and '.root' not in j['out']:
                njobs+=1
                evttot+=j['nevents']
                continue
            if j['status']=='done' and '.root' in j['out'] and j['nevents']>0:
                njobs+=1
                evttot+=j['nevents']
                continue



        cmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls %s'%(j['out'])
        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        p.wait()
        if len(p.stderr.readline())==0: 
            if p.stdout.readline().split()[0]==j['out'].split('/')[-1]:

##########################################################
#For LHE files
##########################################################
                if '.root' not in j['out']:
                    cmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select cp %s /tmp/helsens/'%(j['out'])
                    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
                    stdout,stderr = p.communicate()
                    if os.path.isfile('/tmp/helsens/%s'%(j['out'].split('/')[-1])):
                        os.system('gunzip /tmp/helsens/%s'%(j['out'].split('/')[-1]))
                        cmd='grep \"<event>\" /tmp/helsens/%s | wc -l'%(j['out'].split('/')[-1].replace('.gz',''))
                        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
                        stdout,stderr = p.communicate()
                        stdoutplit=stdout.split(' ')

                        if int(stdoutplit[0])==j['nevents']:
                            evttot+=j['nevents']
                            njobs+=1
                            j['status']='done'

                        else:
                            print 'job is bad exp %s obs %i'%(j['nevents'],int(stdoutplit[0]))
                            j['status']='bad'
                        os.system('rm /tmp/helsens/%s'%(j['out'].split('/')[-1].replace('.gz','')))

                    else:
                        print "not able to copy file %s please check"%j['out']


##########################################################
#For ROOT files
##########################################################
                if '.root' in j['out']:
                    toOpen='root://eospublic.cern.ch/'+j['out']
                    f=r.TFile.Open(toOpen)
                    if f:
                        tree=f.Get('events')
                        print j['out'],'  ',tree.GetEntries()
                        j['nevents'] = tree.GetEntries()
                        evttot+=j['nevents']
                        j['status']='done'
                        f.Close()

        else:
            cmd='bjobs %s'%(j['batchid'])
            print 'cmd: ',cmd
            p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
            stdout,stderr = p.communicate()
            stdoutplit=stdout.split(' ')
            stderrplit=stderr.split(' ')

            if "EXIT" in stdoutplit or "DONE" in stdoutplit or ("is" in stderrplit and "not"  in stderrplit and "<%s>"%(j['batchid'])  in stderrplit):
                print 'job failed'
                j['status']='failed'
            else:
                print '----->> job running or pending'
                j['status']='running'
        
    lstring=20
    sprint=s
    for i in xrange(lstring-len(s)):
        sprint+=" "

    if firstprocess:
        print 'process            \t\tnjobs  \t\t   nevents'

    print sprint,'  \t\t',njobs,'\t\t  ',evttot
    firstprocess=False
with open(indict, 'w') as f:
    json.dump(mydict, f)
