#python common/printdicts.py LHE /afs/cern.ch/user/h/helsens/www/LHEevents.txt
#python common/printdicts.py FCC_fcc_v01 /afs/cern.ch/user/h/helsens/www/Delphesevents_fcc_v01.txt
#python common/printdicts.py FCC_cms /afs/cern.ch/user/h/helsens/www/Delphesevents_cms.txt
import json
import sys
import os.path
import re

import EventProducer.config.param as para
import EventProducer.common.isreading as isr


if len(sys.argv)!=3:
    print 'usage: python printdicts.py LHE/FCC outfile.txt'
    exit(3)

matching=False


indictname=''
inread=''
if sys.argv[1]=='LHE':
    indictname=para.lhe_dic
    inread=para.readlhe_dic
elif 'FCC_' in sys.argv[1]:
    version=sys.argv[1].replace('FCC_','')
    if version not in para.fcc_versions:
        print 'version of the cards should be: fcc_v01, cms'
        print '======================%s======================'%version
        sys.exit(3)
    indictname=para.fcc_dic.replace('VERSION',version)
    inread=para.readfcc_dic.replace('VERSION',version)
    matching=True
else:
    print 'unrecognized mode ',sys.argv[1],'  possible values are FCC or LHE'
    sys.exit(3)


def comma_me(amount):
    orig = amount
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', amount)
    if orig == new:
        return new
    else:
        return comma_me(new)


readdic=isr.isreading(inread, indictname)
readdic.backup('printdic')
readdic.reading()


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
    njobs_bad=0
    njobs_pending=0
    njobs_running=0
    njobs_failed=0

    outdir=''
    outdirtmp=''
    print '------------------------------- ',s
    for j in value:
        if j['status']=='done':
            evttot+=int(j['nevents'])
            njobs+=1
            outdir=j['out']
            outdirtmp=j['out']

        if j['status']=='bad':njobs_bad+=1
        if j['status']=='running':njobs_running+=1
        if j['status']=='submitted':njobs_pending+=1
        if j['status']=='failed':njobs_failed+=1

            
    news=s
    ispythiaonly=False
    print '====================================',s
    try: 
        teststring=para.gridpacklist[s][0]
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to an integer."
    except KeyError, e:
        print 'I got a KeyError - reason "%s"' % str(e)
        ssplit=s.split('_')
        stest=''
        ntest=1
        if '_HT_' in s: ntest=4
        for s in xrange(0,len(ssplit)-ntest):
            stest+=ssplit[s]+'_'

        stest= stest[0:len(stest)-1]
        s=stest
        try: 
            teststringdecay=para.decaylist[stest][0]
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except KeyError, e:
            print 'I got a KeyError - reason "%s"' % str(e)
            try:
                teststringpythia=para.pythialist[news][0]
                ispythiaonly=True
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
            except ValueError:
                print "Could not convert data to an integer."
            except KeyError, e:
                print 'I got a KeyError - reason "%s"' % str(e)
            
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


    nfileseos=0
    if sys.argv[1]=='LHE':
        nfileseos=len(os.listdir('%s%s'%(para.lhe_dir,s)))
    elif 'FCC_' in sys.argv[1]:
        if os.path.isdir('%s%s/%s'%(para.delphes_dir,sys.argv[1].replace('FCC_',''),news)): 
            nfileseos=len(os.listdir('%s%s/%s'%(para.delphes_dir,sys.argv[1].replace('FCC_',''),news)))

    print 'nfiles on eos :  ',nfileseos

    cmd=''
    if not matching and not ispythiaonly:
        cmd='%s,,%s,,%i,,%i,,%i,,%i,,%s,,%s,,%s,,%s,,%s\n'%(news,comma_me(str(evttot)),njobs,njobs_bad, njobs_running,nfileseos  ,outdir.replace(outdirtmp.split('/')[-1],''),para.gridpacklist[s][0],para.gridpacklist[s][1],para.gridpacklist[s][2],para.gridpacklist[s][3])
    elif  matching and not ispythiaonly:
        cmd='%s,,%s,,%i,,%i,,%i,,%i,,%s,,%s,,%s,,%s,,%s,,%s\n'%(news,comma_me(str(evttot)),njobs,njobs_bad, njobs_running,nfileseos ,outdir.replace(outdirtmp.split('/')[-1],''),para.gridpacklist[s][0],para.gridpacklist[s][1],para.gridpacklist[s][3],para.gridpacklist[s][4],para.gridpacklist[s][5])
    elif  ispythiaonly:
        cmd='%s,,%s,,%i,,%i,,%i,,%i,,%s,,%s,,%s,,%s,,%s,,%s\n'%(news,comma_me(str(evttot)),njobs,njobs_bad, njobs_running,nfileseos ,outdir.replace(outdirtmp.split('/')[-1],''),para.pythialist[news][0],para.pythialist[news][1],para.pythialist[news][3],para.pythialist[news][4],para.pythialist[news][5])
        ispythiaonly=False
    OutFile.write(cmd)               

##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency



    ntot_events+=int(evttot)
    ntot_files+=int(njobs)
cmd='%s,,%s,,%i,,%s,,%s,,%s,,%s\n'%('total',comma_me(str(ntot_events)),ntot_files,'','','','')
OutFile.write(cmd)

readdic.comparedics()
readdic.finalize()
