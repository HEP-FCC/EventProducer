#python common/jobchecker.py LHE or FCC
#python common/jobchecker.py LHE_version/FCC secret
#python common/jobchecker.py LHE/FCC_fcc_v01 secret
#python common/jobchecker.py LHE/FCC_cms secret

import json
import subprocess
import sys
import os.path
import ROOT as r
import os.path
import EventProducer.common.isreading as isr
import warnings


# adding this because heppy does not handle root recovered trees'
#_____________________________________________________________
def isValidROOTfile(infile):
    valid = True
    with warnings.catch_warnings(record=True) as was:
        f=r.TFile.Open(infile)
        ctrlstr = 'probably not closed'
        for w in was:
            if ctrlstr in str(w.message):
                valid = False
    return valid
#________________________________________________________________


if "secret" in sys.argv:
    import EventProducer.config.param_test as para
    secret=True
else:
    import EventProducer.config.param as para

#force=False
force=True

if len(sys.argv)>5 or len(sys.argv)<2:
    print 'usage: python jobchecker.py LHE/FCC (process)'
    exit(3)

indict=''
inread=''
if sys.argv[1]=='LHE':
    indict=para.lhe_dic
    inread=para.readlhe_dic
elif 'FCC_' in sys.argv[1]:
    version=sys.argv[1].replace('FCC_','')
    if version not in para.fcc_versions:
        print 'version of the cards should be: fcc_v01, cms'
        print '======================%s======================'%version
        sys.exit(3)
    indict=para.fcc_dic.replace('VERSION',version)
    inread=para.readfcc_dic.replace('VERSION',version)
else:
    print 'unrecognized mode ',sys.argv[1],'  possible values are FCC or LHE'
    sys.exit(3)

if os.path.isfile(indict)==False:
    print 'dictonary does not exists ',indict
    sys.exit(3)

inprocess=''
if len(sys.argv)==3 and sys.argv[2]!='secret':
    inprocess=sys.argv[2]


readdic=isr.isreading(inread, indict)
readdic.backup('jobchecker')
readdic.reading()

mydict=None
with open(indict) as f:
    mydict = json.load(f)
firstprocess=True
for s in mydict:
    evttot=0
    njobs=0
    print 'process  ',s

    if inprocess!='':
        if inprocess!=s: continue

    for j in mydict[s]:
        if force==False:

            if (j['status']== 'done' or j['status']== 'bad')and '.root' not in j['out']:
                njobs+=1
                evttot+=int(j['nevents'])
                continue
            if j['status']=='done' and '.root' in j['out'] and j['nevents']>0:
                njobs+=1
                evttot+=int(j['nevents'])
                continue


        cmd='ls %s'%(j['out'])
        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        p.wait()
        if len(p.stderr.readline())==0: 
            #if p.stdout.readline().split()[0]==j['out'].split('/')[-1]:
            if p.stdout.readline()==j['out']+'\n':

##########################################################
#For LHE files
##########################################################
                if '.root' not in j['out']:
                    filecounting='filecounting'
                    if os.path.isdir(filecounting)==False:
                        os.system('mkdir %s'%filecounting)
                    cmd='cp %s %s'%(j['out'],filecounting)
                    print cmd
                    size=os.path.getsize(j['out'])
                    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
                    stdout,stderr = p.communicate()
                    if os.path.isfile('%s/%s'%(filecounting,j['out'].split('/')[-1])) and size>0:
                        os.system('gunzip %s/%s'%(filecounting,j['out'].split('/')[-1]))
                        cmd='grep \"<event>\" %s/%s | wc -l'%(filecounting,j['out'].split('/')[-1].replace('.gz',''))
                        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
                        stdout,stderr = p.communicate()
                        stdoutplit=stdout.split(' ')

                        if int(stdoutplit[0])==j['nevents']:
                            evttot+=j['nevents']
                            njobs+=1
                            j['status']='done'

                        else:
                            if int(stdoutplit[0])==0:
                                j['status']='failed'
                            print 'job is bad exp %s obs %i'%(j['nevents'],int(stdoutplit[0]))
                            j['status']='bad'
                        os.system('rm %s/%s'%(filecounting,j['out'].split('/')[-1].replace('.gz','')))

                    else:
                        print "not able to copy file %s checking size"%j['out']
                        size=os.path.getsize(j['out'])
                        print 'file size  :  ',size,'  ',type(size)
                        if size==0:
                            print 'bad job'
                            j['status']='failed'
                            os.system('rm %s'%(j['out']))
                        else:
                            print "size ok %s please check"%j['out']

##########################################################
#For ROOT files
##########################################################

                if '.root' in j['out']:
                    if not isValidROOTfile(j['out']):
                        print 'corrupt file'
                        j['status']='failed'
                        continue 


                    f=r.TFile.Open(j['out'])
                    if f:
                        size=os.path.getsize(j['out'])
                        print '--------------------   ',size
                        if size==0:
                            print 'bad job'
                            j['status']='failed'

                        else:
                            lok=[key.GetName() for key in r.gDirectory.GetListOfKeys()]
                            if 'events' not in lok:
                                 print 'no trees, job failed'
                                 j['status']='failed'
                                 continue
                            tree=f.Get('events')    
                            print j['out'],'  ',tree.GetEntries()
                            if tree.GetEntries()==0:
                                print '0 entries, job failed'
                                j['status']='failed'
                            else:
                                posentries=tree.GetEntries("mcEventWeights.value>0.")
                                negentries=tree.GetEntries("mcEventWeights.value<0.")
                                if negentries>0:
                                    print 'NLO ',posentries,'   ',negentries,'  ',posentries-negentries
                                    j['nweights'] = posentries-negentries
                                    print 'weight  ',j['nweights']
                                else :j['nweights'] = posentries
                                j['nevents'] = tree.GetEntries()
                                evttot+=j['nevents']
                                j['status']='done'
                        f.Close()
                    else:
                        if os.path.isfile(j['out']): 
                            print 'no file, job failed'
                            j['status']='failed'

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


readdic.comparedics()
readdic.finalize()
    
