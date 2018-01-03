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
