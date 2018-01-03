#python common/convert.py /eos/experiment/fcc/hh/generation/mg5_amcatnlo/lhe/pp_ee_nlo/ "/eos/experiment/fcc/hh/generation/DelphesEvents/fcc_v0*"
import glob, os, sys
import commands

import time
import random
from datetime import datetime
import EventProducer.config.users as us
import EventProducer.common.utils as ut

#__________________________________________________________
if __name__=="__main__":

    basedir=sys.argv[1]
    baserootdir=sys.argv[2]
    ldir=[x[0] for x in os.walk(basedir)]
    user=os.environ['USER']
    userext=-999999
    for key, value in us.users.iteritems():
        if key==user: 
            userext=value
    if userext<0:
        print 'user not known ',user,'   exit'
        sys.exit(3)
    exten=''
    for l in ldir:
        All_files = glob.glob("%s/*events*"%(l))
        if len(All_files)==0:continue
        process = l.split('/')[-1]
        if process=='':
            ltmp=l.split('/')
            process=l.split('/')[len(ltmp)-2]
        print 'process  ',process
        for f in All_files:
            if not os.path.isfile(f): continue
            if '.root' in f:
                exten='.root'
            elif '.lhe.gz' in f:
                exten='.lhe.gz'
                 
            allrootfiles=glob.glob('%s/%s/%s'%(baserootdir,process,f.split('/')[-1].replace('lhe.gz','root')))
            if user in ut.find_owner(f):
                seed = int(datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3])
                uniqueID='%s_%s_%i%i'%('lsf',user,seed,userext)
                outfile = 'events_%s%s'%(uniqueID,exten)
                if len(allrootfiles)>0:
                    outfileroot = 'events_%s.root'%(uniqueID)
                    for r in allrootfiles:
                        baseroot = r.rsplit('/',1)[0]
                        print "ROOT ----------- "+baseroot+"/"+outfileroot
                        os.system('mv %s %s/%s'%(r,baseroot,outfileroot))
                print "LHE ONLY ----------- "+basedir+outfile

                
                os.system('mv %s %s'%(f,basedir+outfile))
                time.sleep(0.05)



