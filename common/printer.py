import sys
import os.path
import re
import yaml
import EventProducer.common.utils as ut
import time
class printer():

#__________________________________________________________
    def __init__(self, indir, outfile, matching, isLHE, para, detector, version=''):
        self.indir    = indir
        self.outfile  = outfile
        self.matching = matching
        self.isLHE = isLHE
        self.para = para
        self.version = version
        self.detector=detector
        self.OutFile   = open(self.outfile, 'w')

        self.tot_size=0
        self.ntot_events=0
        self.ntot_files=0
        self.ntot_bad=0
        self.ntot_eos=0
        self.ntot_sumw=0


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
        
        #ldir=[x[0] for x in os.walk(self.indir)]
        ldir=next(os.walk(self.indir))[1]

#        checkfiles=''
#        if self.isLHE: checkfiles='%s/files.yaml'%(self.para.lhe_dir)
#        else:          checkfiles='%s/%s/files.yaml'%(self.para.delphes_dir,self.version)
#
#        tmpcheck=None
#        with open(checkfiles, 'r') as stream:
#            try:
#                tmpcheck = yaml.load(stream, Loader=yaml.FullLoader)
#            except yaml.YAMLError as exc:
#                print(exc)


        for l in ldir:
            process=l
            mergefile=self.indir+'/'+l+'/merge.yaml'
            if not ut.file_exist(mergefile): continue
            print ('--------------  process  ',process)

            tmpf=None
            with open(mergefile, 'r') as stream:
                try:
                    tmpf = yaml.load(stream, Loader=yaml.FullLoader)
                except yaml.YAMLError as exc:
                    print(exc)
                except IOError as exc:
                    print(exc)
                    print ('file  ',mergefile)
                    time.sleep(10)
                    tmpf = yaml.load(stream, Loader=yaml.FullLoader)

            events_tot=tmpf['merge']['nevents']
            size_tot=tmpf['merge']['size']/1000000000.
            bad_tot=tmpf['merge']['nbad']
            files_tot=tmpf['merge']['ndone']
            sumw_tot=0
            proc = process.replace('mgp8_','mg_')
       
            news=str(proc)
            proc=str(proc)
 
            br=1
            decay=''
            decstr=''
            for dec in self.para.branching_ratios:
                dec_proc = proc.split('_')[-1]
                if dec in proc and dec_proc == dec:
                    br = self.para.branching_ratios[dec]
                    decay = dec
            if decay != '':
                print ('decay---------- ',decay,' ------- br ',br)
                decstr = '_{}'.format(decay)

            ispythiaonly=False
            try: 
                teststring=self.para.gridpacklist[proc][0]
            except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
            except ValueError:
                print ("Could not convert data to an integer.")
            except KeyError as e:
                print ('I got a KeyError 1 - reason "%s"' % str(e))
                ssplit=proc.split('_')
                stest=''
                ntest=1
                if '_HT_' in proc: ntest=4
                for procn in range(0,len(ssplit)-ntest):
                    stest+=ssplit[procn]+'_'

                stest= stest[0:len(stest)-1]
                proc=stest
 #CLEMENT TO BE FIXED
                if decay != '':
                    proc = proc.replace(decstr,'')
                    print ('--------------  ',decstr,'  --  ',proc)

                try: 
                    teststringdecay=self.para.decaylist[stest][0]
                except IOError as e:
                    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                except ValueError:
                    print ("Could not convert data to an integer.")
                except KeyError as e:
                    print ('I got a KeyError 2 - reason "%s"' % str(e))
                    try:
                        teststringpythia=self.para.pythialist[news][0]
                        ispythiaonly=True
                    except IOError as e:
                        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                    except ValueError:
                        print ("Could not convert data to an integer.")
                    except KeyError as e:
                        print ('I got a KeyError 3 - reason "%s"' % str(e))
            
            except:
                print ("Unexpected error:", sys.exc_info()[0])
                raise

            
            if not ispythiaonly:
                try:
                    stupidtest=self.para.gridpacklist[proc]
                except KeyError as e:
                    print ('changing proc :',proc,'  to dummy')
                    proc='dummy'
            if ispythiaonly:
                try :
                    stupidtest=self.para.pythialist[news]
                except KeyError as e:
                    print ('changing proc pythia :',news,'  to dummy')
                    news='dummy'


            nfileseos=0
#            nfileseos=tmpcheck[proc]['neos']
            if self.isLHE:
                if os.path.isdir('%s%s'%(self.para.lhe_dir,proc)):
                    nfileseos=len(os.listdir('%s%s'%(self.para.lhe_dir,proc)))
            else:                    
                if os.path.isdir('%s%s/%s/%s'%(self.para.delphes_dir,self.version,self.detector,process)): 
                    print ('%s%s/%s/%s'%(self.para.delphes_dir,self.version,self.detector,process))
                    nfileseos=len(os.listdir('%s%s/%s/%s'%(self.para.delphes_dir,self.version,self.detector,process)))

            print ('nevents               : %i'%events_tot)
            print ('nfiles on eos/checked : %i/%i'%(nfileseos,files_tot))
            print ('proc in the end       : ',proc)
            print ('news in the end       : ',news)

            marked_b=''
            marked_e=''

            if nfileseos>files_tot+bad_tot:
                marked_b='<h2><mark>'
                marked_e='</mark></h2>'

            cmd=''

            if not self.matching and not ispythiaonly:
                cmd='%s,,%s,,%s%i%s,,%i,,%s%i%s,,%.2f,,%s,,%s,,%s,,%s,,%s\n'%(process,self.comma_me(str(events_tot)),
                                                                              marked_b,files_tot,marked_e,bad_tot,
                                                                              marked_b,nfileseos,marked_e,size_tot,
                                                                              tmpf['merge']['outdir'],
                                                                              self.para.gridpacklist[proc][0],self.para.gridpacklist[proc][1],
                                                                              self.para.gridpacklist[proc][2],self.para.gridpacklist[proc][3])
            elif  self.matching and not ispythiaonly:
                cmd='%s,,%s,,%s,,%s%i%s,,%i,,%s%i%s,,%.2f,,%s,,%s,,%s,,%s,,%s,,%s\n'%(process,self.comma_me(str(events_tot)),self.comma_me(str(sumw_tot)),
                                                                                      marked_b,files_tot,marked_e,bad_tot,
                                                                                      marked_b,nfileseos,marked_e, size_tot ,
                                                                                      tmpf['merge']['outdir'],
                                                                                      self.para.gridpacklist[proc][0],self.para.gridpacklist[proc][1]
                                                                                      ,str(float(self.para.gridpacklist[proc][3])*br),self.para.gridpacklist[proc][4],
                                                                                      self.para.gridpacklist[proc][5])

            elif  ispythiaonly:
                cmd='%s,,%s,,%s,,%s%i%s,,%i,,%s%i%s,,%.2f,,%s,,%s,,%s,,%s,,%s,,%s\n'%(process,self.comma_me(str(events_tot)),self.comma_me(str(sumw_tot)),
                                                                                      marked_b,files_tot,marked_e,bad_tot,
                                                                                      marked_b,nfileseos,marked_e, size_tot ,
                                                                                      tmpf['merge']['outdir'],
                                                                                      self.para.pythialist[news][0],self.para.pythialist[news][1],
                                                                                      self.para.pythialist[news][3],self.para.pythialist[news][4],
                                                                                      self.para.pythialist[news][5])
                ispythiaonly=False
            self.OutFile.write(cmd)               

##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency



            self.ntot_events+=int(events_tot)
            self.ntot_files+=int(files_tot)
            self.tot_size+=float(size_tot)
            self.ntot_bad+=float(bad_tot)
            self.ntot_eos+=float(nfileseos)
            self.ntot_sumw+=float(sumw_tot)
        if not self.matching:
            cmd='%s,,%s,,%s,,%s,,%s,,%.2f,,%s,,%s\n'%('total',self.comma_me(str(self.ntot_events)),self.comma_me(str(self.ntot_files)),
                                                      self.comma_me(str(self.ntot_bad)),self.comma_me(str(self.ntot_eos)),self.tot_size,'','')
        else: 
            cmd='%s,,%s,,%s,,%s,,%s,,%s,,%.2f,,%s,,%s\n'%('total',self.comma_me(str(self.ntot_events)),self.comma_me(str(self.ntot_sumw)),
                                                          self.comma_me(str(self.ntot_files)),
                                                          self.comma_me(str(self.ntot_bad)),self.comma_me(str(self.ntot_eos)),self.tot_size,'','')

        self.OutFile.write(cmd)

