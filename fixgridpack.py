#! /usr/bin/env python


import subprocess
import time
import sys, optparse, os, re


#__________________________________________________________
def getCommandOutput(command):
    p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout,stderr = p.communicate()
    return {"stdout":stdout, "stderr":stderr, "returncode":p.returncode}


parser = optparse.OptionParser(usage ="""
    usage: %prog gridpack1.tar.gz gridpack2.tar.gz ...
    
    Repackages grid pack with fixed me5_configuration.txt, madevent_interace.py, and renamed to remove underscores and add suffix
     """)

opts, args = parser.parse_args()
if len(args) < 1:
    parser.print_help()
    sys.exit(1)

for gridpack in args:

    # repackage grid pack
    gridfilename = os.path.basename(gridpack)
    localdir=os.getcwd()
    if localdir[-1]!='/':localdir+='/'
    subprocess.call('tar -zxf ' + gridfilename, shell=True)
    dirtogo='%s'%(localdir+gridfilename.replace('.tar.gz',''))
    os.chdir(dirtogo)
    files=getCommandOutput('ls *.tar.gz')["stdout"].split('\n')
    print '---',files
    flist=''
    for f in files: flist+=' %s'%(f)
    print flist
    print 'python CompileGridpack.py %s'%flist
    os.system('python CompileGridpack.py %s'%flist)
    os.chdir(localdir)
    #print 'tar -czf  '+gridfilename.replace('.tar.gz','_lxplus.tar.gz')+' '+gridfilename.replace('.tar.gz','')
    #subprocess.call('tar -czf  '+gridfilename.replace('.tar.gz','_lxplus.tar.gz')+' '+gridfilename.replace('.tar.gz',''), shell=True)
    
    print ""

