#python makeSampleList.py  /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json
import subprocess
import sys
import os
import json

if len(sys.argv)!=2:
    print 'usage: python makeSampleList.py indict.json'
    exit(3)


indict=sys.argv[1]
if os.path.isfile(indict)==False:
    print 'dictonary does not exists '
    exit(3)

mydict=None
with open(indict) as f:
    mydict = json.load(f)


eosroot = 'root://eospublic.cern.ch/'
outdir = '/afs/cern.ch/work/h/helsens/public/FCCDicts/'
out = open("%sFCChh_samples.py"%outdir, "w")
out.write("import heppy.framework.config as cfg\n")
out.write("\n")

for s in mydict:
    print 'process  ',s

    out.write("%s = cfg.MCComponent(\n" %s)
    out.write("    \'%s\',\n" %s)
    out.write("    files=[\n")
   
    for j in mydict[s]:
         if j['status']== 'done':
             out.write("           '%s%s',\n" %(eosroot,j['out']))

    out.write("]\n")
    out.write(")\n")
    out.write("\n")

