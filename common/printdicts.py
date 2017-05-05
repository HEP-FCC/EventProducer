#python printdicts.py /afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json /afs/cern.ch/user/h/helsens/www/LHEevents.txt
#python printdicts.py /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json /afs/cern.ch/user/h/helsens/www/Delphesevents.txt
import json
import sys
import os.path
import re

import EventProducer.config.param as para


if len(sys.argv)!=3:
    print 'usage: python printdicts.py indict.json outfile.txt'
    exit(3)


def comma_me(amount):
    orig = amount
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', amount)
    if orig == new:
        return new
    else:
        return comma_me(new)


indictname=sys.argv[1]
matching=False
if 'LHE' not in indictname:
    matching=True

if os.path.isfile(indictname)==False:
    print 'dictonary does not exists '
    exit(3)

outfile=sys.argv[2]

indict=None
with open(indictname) as f:
    indict = json.load(f)


OutFile   = open(outfile, 'w')
ntot_events=0
ntot_files=0
for s, value in sorted(indict.items()):
    evttot=0
    njobs=0
    outdir=''
    outdirtmp=''
    print '------------------------------- ',s
    for j in value:
        if j['status']=='done':
            evttot+=int(j['nevents'])
            njobs+=1
            outdir=j['out']
            outdirtmp=j['out']

    try: 
        teststring=para.gridpacklist[s][0]
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to an integer."
    except KeyError, e:
        print 'I got a KeyError - reason "%s"' % str(e)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    cmd=''
    if not matching:
        cmd='%s,,%s,,%i,,%s,,%s,,%s,,%s\n'%(s,comma_me(str(evttot)),njobs,outdir.replace(outdirtmp.split('/')[-1],''),para.gridpacklist[s][0],para.gridpacklist[s][1],para.gridpacklist[s][3])
    else:
         cmd='%s,,%s,,%i,,%s,,%s,,%s,,%s,,%s,,%s\n'%(s,comma_me(str(evttot)),njobs,outdir.replace(outdirtmp.split('/')[-1],''),para.gridpacklist[s][0],para.gridpacklist[s][1],para.gridpacklist[s][2],para.gridpacklist[s][3],para.gridpacklist[s][4])
    OutFile.write(cmd)               
   
    ntot_events+=int(evttot)
    ntot_files+=int(njobs)
cmd='%s,,%s,,%i,,%s,,%s,,%s,,%s\n'%('total',comma_me(str(ntot_events)),ntot_files,'','','','')
OutFile.write(cmd)
