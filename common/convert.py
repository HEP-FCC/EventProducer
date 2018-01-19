#python common/convert.py /eos/experiment/fcc/hh/generation/mg5_amcatnlo/lhe/pp_ee_nlo/ files
#python common/convert.py /eos/experiment/fcc/hh/generation/DelphesEvents/fcc_v01/pp_ee_nlo/ files
#python common/convert.py /eos/experiment/fcc/helhc/generation/gridpacks/ gp
#python common/convert.py /eos/experiment/fcc/helhc/generation/lhe/ process



import glob, os, sys
import commands

import time
import random
from datetime import datetime
import EventProducer.config.users as us
import EventProducer.common.utils as ut

#__________________________________________________________
def runFiles(basedir):
    ldir=[x[0] for x in os.walk(basedir)]
    user=os.environ['USER']
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
            
            if len(f.split('/')[-1])>20: continue

            if not os.path.isfile(f): continue
            if '.root' in f:
                exten='.root'
            elif '.lhe.gz' in f:
                exten='.lhe.gz'
            
            ori_id=f.split('/')[-1].replace('events','')
            ori_id=ori_id.split('.')[0]
            
            if user in ut.find_owner(f):
                baseid=''
                for i in xrange(9-len(ori_id)):
                    baseid+='0'
                ori_id=int(ori_id)
                ori_id+=1
                new_id=baseid+str(ori_id)
                print ori_id,'    ',new_id

                uniqueID='%s_%s'%(user,new_id)
                outfile = 'events_%s%s'%(uniqueID,exten)
 
                cmd = 'mv %s %s'%(f,basedir+outfile)
                print cmd
                #os.system(cmd)
                time.sleep(0.01)


#__________________________________________________________
def runProcess(basedir):
    ldir=[x[0] for x in os.walk(basedir)]
    for l in ldir:
        All_files = glob.glob("%s/*tar.gz"%(l))
        for f in All_files:
            if not os.path.isfile(f): continue
            print 'mv %s %s'%(f,basedir+outfile)


#__________________________________________________________
def runGP(basedir):
    ldir=[x[0] for x in os.walk(basedir)]
    for l in ldir:
        All_files = glob.glob("%s/*tar.gz"%(l))
        for f in All_files:
            if not os.path.isfile(f): continue
            infile=f.split('/')[-1]
            if infile[0:3]=="mg_": continue
            outfile = 'mg_%s'%(infile)
            cmd = 'mv %s %s'%(f,basedir+outfile)
            print cmd
            os.system(cmd)
            time.sleep(0.01)


#__________________________________________________________
if __name__=="__main__":

    if len(sys.argv)!=3:
        print 'usage: python common/convert.py directory process/files/gp'
        sys.exit(3)
    basedir=sys.argv[1]
    
    if sys.argv[2]=='files':
        runFiles(basedir)

    elif sys.argv[2]=='process':
        runProcess(basedir)

    elif sys.argv[2]=='gp':
        runGP(basedir)


