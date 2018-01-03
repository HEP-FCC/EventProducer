import warnings
import ROOT as r
import subprocess
import os
from pwd import getpwuid
import sys
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
        outputCMD = ut.getCommandOutput(cmd)
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
def eosexist(myfile):
    cmd='ls %s'%(myfile)
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    p.wait()
    if len(p.stderr.readline())==0:
        return True
    else: 
        return False
