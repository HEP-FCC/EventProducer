#python common/printdicts.py LHE /afs/cern.ch/user/h/helsens/www/LHEevents.txt
#python common/printdicts.py FCC_fcc_v01 /afs/cern.ch/user/h/helsens/www/Delphesevents_fcc_v01.txt
#python common/printdicts.py FCC_cms /afs/cern.ch/user/h/helsens/www/Delphesevents_cms.txt

#python common/printdicts.py FCC LHE /afs/cern.ch/user/h/helsens/www/LHEevents.txt
#python common/printdicts.py FCC DEL fcc_v01 /afs/cern.ch/user/h/helsens/www/Delphesevents_fcc_v01.txt


import json
import sys
import os.path
import re


print 'usage: python printdicts.py FCC/HELHC LHE/DEL /version'
    

class printdicts():

#__________________________________________________________
    def __init__(self,indict, outfile, matching, isLHE, para, version=''):
        self.outfile  = outfile
        self.matching = matching
        self.indictname   = indict
        self.isLHE = isLHE
        self.para = para
        self.version = version
        if os.path.isfile(self.indictname)==False:
            print 'dictonary does not exists '
            sys.exit(3)

        self.indict=None
        with open(self.indictname) as f:
            self.indict = json.load(f)

        self.OutFile   = open(self.outfile, 'w')

        self.tot_size=0
        self.ntot_events=0
        self.ntot_files=0
#__________________________________________________________
    def comma_me(self, amount):
        orig = amount
        new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', amount)
        if orig == new:
            return new
        else:
            return self.comma_me(new)


#__________________________________________________________
    def run(self):
        for proc, value in sorted(self.indict.items()):
            evttot=0
            sumw=0
            njobs=0
            njobs_bad=0
            size=0
            outdir=''
            outdirtmp=''
            print '------------------------------- ',proc, type(proc)
            for j in value:
                if j['status']=='DONE':
                    evttot+=int(j['nevents'])
                    size+=int(j['size'])/1000000.
                    njobs+=1
                    outdir=j['out']
                    outdirtmp=j['out']
                    try:
                        sumw+=int(j['nweights'])
                    except KeyError, e:
                        sumw+=0
                if j['status']=='BAD':njobs_bad+=1
                
            news=str(proc)
            proc=str(proc)
            print '------------------------------- ',proc, type(proc)

            ispythiaonly=False
            try: 
                teststring=self.para.gridpacklist[proc][0]
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
                    teststringdecay=self.para.decaylist[stest][0]
                except IOError as e:
                    print "I/O error({0}): {1}".format(e.errno, e.strerror)
                except ValueError:
                    print "Could not convert data to an integer."
                except KeyError, e:
                    print 'I got a KeyError 2 - reason "%s"' % str(e)
                    try:
                        teststringpythia=self.para.pythialist[news][0]
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
            if self.isLHE:
                nfileseos=len(os.listdir('%s%s'%(self.para.lhe_dir,proc)))
            else:
                if os.path.isdir('%s%s/%s'%(self.para.delphes_dir,self.version,news)): 
                    nfileseos=len(os.listdir('%s%s/%s'%(self.para.delphes_dir,self.version,news)))

            print 'nfiles on eos :  ',nfileseos
            print 's  ',type(proc),'  news  ',type(news)
            cmd=''
            print '-----fefefeefefefefefe----------',self.comma_me(str(sumw))
            if not self.matching and not ispythiaonly:
                cmd='%s,,%s,,%s,,%i,,%i,,%i,,%i,,%s,,%s,,%s,,%s,,%s\n'%(news,self.comma_me(str(evttot)),self.comma_me(str(sumw)),njobs,njobs_bad,nfileseos,size  ,outdir.replace(outdirtmp.split('/')[-1],''),self.para.gridpacklist[proc][0],self.para.gridpacklist[proc][1],self.para.gridpacklist[proc][2],self.para.gridpacklist[proc][3])
            elif  matching and not ispythiaonly:
                cmd='%s,,%s,,%s,,%i,,%i,,%i,,%s,,%s,,%s,,%s,,%s,,%s\n'%(news,self.comma_me(str(evttot)),self.comma_me(str(sumw)),njobs,njobs_bad,nfileseos, size ,outdir.replace(outdirtmp.split('/')[-1],''),self.para.gridpacklist[proc][0],self.para.gridpacklist[proc][1],self.para.gridpacklist[proc][3],self.para.gridpacklist[proc][4],self.para.gridpacklist[proc][5])
            elif  ispythiaonly:
                cmd='%s,,%s,,%s,,%i,,%i,,%i,,%i,,%i,,%s,,%s,,%s,,%s,,%s,,%s\n'%(news,self.comma_me(str(evttot)),self.comma_me(str(sumw)),njobs,njobs_bad, njobs_running,nfileseos ,outdir.replace(outdirtmp.split('/')[-1],''),self.para.pythialist[news][0],self.para.pythialist[news][1],self.para.pythialist[news][3],self.para.pythialist[news][4],self.para.pythialist[news][5])
                ispythiaonly=False
            self.OutFile.write(cmd)               

##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency



            self.ntot_events+=int(evttot)
            self.ntot_files+=int(njobs)
            self.tot_size+=int(size)
        cmd='%s,,%s,,%s,,%s,,%s,,%s,,%s,,%s\n'%('total',self.comma_me(str(self.ntot_events)),'',self.comma_me(str(self.ntot_files)),self.comma_me(str(self.tot_size)),'','','')
        self.OutFile.write(cmd)

