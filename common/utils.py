import warnings
import ROOT as r
import subprocess
import os
import sys
import yaml

from datetime import datetime
from pwd import getpwuid

import EventProducer.config.users as us

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


#__________________________________________________________
def getsize(f):
    exist=os.path.isfile(f)
    if exist:
        size = os.path.getsize(f)
        return size
    return -1


#__________________________________________________________
def getCommandOutput(command):
    p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout,stderr = p.communicate()
    return {"stdout":stdout, "stderr":stderr, "returncode":p.returncode}

#__________________________________________________________
def testeos(f,fs):
    exist=os.path.isfile(f)
    if exist:
        size = os.path.getsize(f)
        if size==fs:
            return True
    return False
#__________________________________________________________
def find_owner(filename):
    return getpwuid(os.stat(filename).st_uid).pw_name

#__________________________________________________________
def SubmitToCondor(cmd,nbtrials):
    submissionStatus=0
    cmd=cmd.replace('//','/')
    for i in xrange(nbtrials):            
        outputCMD = getCommandOutput(cmd)
        stderr=outputCMD["stderr"].split('\n')
        stdout=outputCMD["stdout"].split('\n')

        if len(stderr)==1 and stderr[0]=='' :
            print "------------GOOD SUB"
            submissionStatus=1
        else:
            print "++++++++++++ERROR submitting, will retry"
            print "Trial : "+str(i)+" / "+str(nbtrials)
            print "stderr : ",stderr
            print "stderr : ",len(stderr)

            time.sleep(10)

            
        if submissionStatus==1:
            return 1,0
        
        if i==nbtrials-1:
            print "failed sumbmitting after: "+str(nbtrials)+" trials, will exit"
            return 0,0

#__________________________________________________________
def SubmitToLsf(cmd,nbtrials):
    submissionStatus=0
    for i in range(nbtrials):            
        outputCMD = getCommandOutput(cmd)
        stderr=outputCMD["stderr"].split('\n')

        for line in stderr :
            if line=="":
                print "------------GOOD SUB"
                submissionStatus=1
                break
            else:
                print "++++++++++++ERROR submitting, will retry"
                print "error: ",stderr
                print "Trial : "+str(i)+" / "+str(nbtrials)
                time.sleep(10)
                break
            
        if submissionStatus==1:
            jobid=outputCMD["stdout"].split()[1].replace("<","").replace(">","")
            return 1,jobid
        
        if i==nbtrials-1:
            print "failed sumbmitting after: "+str(nbtrials)+" trials, will exit"
            return 0,0

#__________________________________________________________
def file_exist(myfile):
    import os.path
    if os.path.isfile(myfile): return True
    else: return False

#__________________________________________________________
def dir_exist(mydir):
    import os.path
    if os.path.exists(mydir): return True
    else: return False
  
#__________________________________________________________
def getuid(user):
    userext=-999999
    for key, value in us.users.iteritems():
        if key==user: 
            userext=value
    if userext<0:
        print 'user not known ',user,'   exit'
        sys.exit(3)
    seed = int(datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3])
    uniqueID='%i%i'%(seed,userext)
    return uniqueID

#__________________________________________________________
def getuserid(user):
    userext=-999999
    for key, value in us.users.iteritems():
        if key==user: 
            userext=value
    if userext<0:
        print 'user not known ',user,'   exit'
        sys.exit(3)
    return userext


#__________________________________________________________
def getuid2(user):
    import random
    userext=-999999
    for key, value in us.users.iteritems():
        if key==user: 
            userext=value
    if userext<0:
        print 'user not known ',user,'   exit'
        sys.exit(3)
    
    seed = '%i%i%i%i%i%i%i%i%i'%(random.randint(0,1),
                                 random.randint(0,9),
                                 random.randint(0,9),
                                 random.randint(0,9),
                                 random.randint(0,9),
                                 random.randint(0,9),
                                 random.randint(0,9),
                                 random.randint(0,9),
                                 random.randint(0,9))
    return seed



#__________________________________________________________
def yamlcheck(yamlfile, process):
#if no input file
    if not file_exist(yamlfile):
        return False
    
    doc = None
    with open(yamlfile) as f:
        try:
            doc = yaml.load(f)
        except yaml.YAMLError as exc:
            print(exc)
    try: 
        value = doc[process]
        if value: return True
        return False
    except KeyError, e:
        print 'Process %s does not exist' % str(e)
        return False

  
    
       

#__________________________________________________________
def yamlstatus(yamlfile, process, status):
#if no input file
    if not file_exist(yamlfile):
        dic={process:True}
        with open(yamlfile, 'w') as f:
            yaml.dump(dic, f, default_flow_style=False)
        return

#if change the value of existing process
    doc = None
    with open(yamlfile) as f:
        try:
            doc = yaml.load(f)
        except yaml.YAMLError as exc:
            print(exc)
    doc[process] = status

    with open(yamlfile, 'w') as f:
        yaml.dump(doc, f, default_flow_style=False)

