#python common/printdicts.py LHE /afs/cern.ch/user/h/helsens/www/LHEevents.txt
#python common/printdicts.py FCC_fcc_v01 /afs/cern.ch/user/h/helsens/www/Delphesevents_fcc_v01.txt
#python common/printdicts.py FCC_cms /afs/cern.ch/user/h/helsens/www/Delphesevents_cms.txt

#python common/printdicts.py FCC LHE /afs/cern.ch/user/h/helsens/www/LHEevents.txt
#python common/printdicts.py FCC DEL fcc_v01 /afs/cern.ch/user/h/helsens/www/Delphesevents_fcc_v01.txt


import json
import sys
import os.path
import re

if len(sys.argv)<3:
    print 'usage: python printdicts.py FCC/HELHC LHE/DEL /version'
    exit(3)

if sys.argv[1]=="FCC":
    import EventProducer.config.param as para
elif sys.argv[1]=="HELHC":
    import EventProducer.config.param_HELHC as para
else:
    print 'unknown case' 
    sys.exit(3)


matching=False


indictname=''
outfile=''
if sys.argv[2]=='LHE':
    indictname=para.lhe_dic
    outfile=para.lhe_web
elif sys.argv[2] == 'DEL':
    version=sys.argv[3]
    if version not in para.fcc_versions:
        print 'version of the cards should be: fcc_v01, cms'
        print '======================%s======================'%version
        sys.exit(3)
    indictname=para.fcc_dic.replace('VERSION',version)
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

if os.path.isfile(indictname)==False:
    print 'dictonary does not exists '
    exit(3)

indict=None
with open(indictname) as f:
    indict = json.load(f)

OutFile   = open(outfile, 'w')
ntot_events=0
ntot_files=0
for proc, value in sorted(indict.items()):
    evttot=0
    sumw=0
    njobs=0
    njobs_bad=0
    njobs_pending=0
    njobs_running=0
    njobs_failed=0

    outdir=''
    outdirtmp=''
    print '------------------------------- ',proc, type(proc)
    for j in value:
        if j['status']=='DONE':
            evttot+=int(j['nevents'])
            njobs+=1
            outdir=j['out']
            outdirtmp=j['out']
            try:
                sumw+=int(j['nweights'])
                if proc=='pp_ttv01j_5f': print sumw,'   ',j['nweights']
            except KeyError, e:
                sumw+=0
        if j['status']=='bad':njobs_bad+=1
        if j['status']=='running':njobs_running+=1
        if j['status']=='submitted':njobs_pending+=1
        if j['status']=='failed':njobs_failed+=1

            
    news=str(proc)
    proc=str(proc)
    print '------------------------------- ',proc, type(proc)

    ispythiaonly=False
    try: 
        teststring=para.gridpacklist[proc][0]
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to an integer."
    except KeyError, e:
        print 'I got a KeyError 1 - reason "%s"' % str(e)
        ssplit=proc.split('_')
        stest=''
        ntest=1
        if '_HT_' in proc: ntest=4
        for proc in xrange(0,len(ssplit)-ntest):
            stest+=ssplit[proc]+'_'

        stest= stest[0:len(stest)-1]
        proc=stest
        try: 
            teststringdecay=para.decaylist[stest][0]
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except KeyError, e:
            print 'I got a KeyError 2 - reason "%s"' % str(e)
            try:
                teststringpythia=para.pythialist[news][0]
                ispythiaonly=True
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
            except ValueError:
                print "Could not convert data to an integer."
            except KeyError, e:
                print 'I got a KeyError 3 - reason "%s"' % str(e)
            
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


    nfileseos=0
    if sys.argv[2]=='LHE':
        nfileseos=len(os.listdir('%s%s'%(para.lhe_dir,proc)))
    elif 'DEL' in sys.argv[2]:
        if os.path.isdir('%s%s/%s'%(para.delphes_dir,sys.argv[3],news)): 
            nfileseos=len(os.listdir('%s%s/%s'%(para.delphes_dir,sys.argv[3],news)))

    print 'nfiles on eos :  ',nfileseos
    print 's  ',type(proc),'  news  ',type(news)
    cmd=''
    print '-----fefefeefefefefefe----------',comma_me(str(sumw))
    if not matching and not ispythiaonly:
        cmd='%s,,%s,,%s,,%i,,%i,,%i,,%i,,%s,,%s,,%s,,%s,,%s\n'%(news,comma_me(str(evttot)),comma_me(str(sumw)),njobs,njobs_bad, njobs_running,nfileseos  ,outdir.replace(outdirtmp.split('/')[-1],''),para.gridpacklist[proc][0],para.gridpacklist[proc][1],para.gridpacklist[proc][2],para.gridpacklist[proc][3])
    elif  matching and not ispythiaonly:
        cmd='%s,,%s,,%s,,%i,,%i,,%i,,%i,,%s,,%s,,%s,,%s,,%s,,%s\n'%(news,comma_me(str(evttot)),comma_me(str(sumw)),njobs,njobs_bad, njobs_running,nfileseos ,outdir.replace(outdirtmp.split('/')[-1],''),para.gridpacklist[proc][0],para.gridpacklist[proc][1],para.gridpacklist[proc][3],para.gridpacklist[proc][4],para.gridpacklist[proc][5])
    elif  ispythiaonly:
        cmd='%s,,%s,,%s,,%i,,%i,,%i,,%i,,%s,,%s,,%s,,%s,,%s,,%s\n'%(news,comma_me(str(evttot)),comma_me(str(sumw)),njobs,njobs_bad, njobs_running,nfileseos ,outdir.replace(outdirtmp.split('/')[-1],''),para.pythialist[news][0],para.pythialist[news][1],para.pythialist[news][3],para.pythialist[news][4],para.pythialist[news][5])
        ispythiaonly=False
    OutFile.write(cmd)               

##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency



    ntot_events+=int(evttot)
    ntot_files+=int(njobs)
cmd='%s,,%s,,%s,,%s,,%s,,%s,,%s,,%s\n'%('total',comma_me(str(ntot_events)),'',comma_me(str(ntot_files)),'','','','')
OutFile.write(cmd)

