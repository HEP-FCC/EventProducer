import json
import subprocess


mydict=None
with open('/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json') as f:
    mydict = json.load(f)
for s in mydict:
    evttot=0
    njobs=0
    for j in mydict[s]:
        if j['status']=='done':continue
        cmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls %s'%(j['out'])
        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        p.wait()
        if len(p.stderr.readline())==0: 
            if p.stdout.readline().split()[0]==j['out'].split('/')[-1]:
                #print 'job succeeded'
                evttot+=j['nevents']
                njobs+=1
                j['status']='done'
        else:
            cmd='bjobs %s'%(j['batchid'])
            p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
            p.wait()
            jobstatus=(p.stderr.readline()).rstrip()
            myjobstatus=str('Job <%s> is not found'%(j['batchid']))
            
            print jobstatus
            print myjobstatus
            print jobstatus == myjobstatus
            print '---------------------------'

            if jobstatus == myjobstatus:
                print 'job failed'
                j['status']='failed'
            else:
                print '----->> job running or pending'
                j['status']='running'
        

    print s,'  \t',njobs,'\t  ',evttot
    
with open('/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json', 'w') as f:
    json.dump(mydict, f)
