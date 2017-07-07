import json
import os, sys
import time
import datetime

#__________________________________________________________
class isreading():
    def __init__(self,inread, indic):
        self.read=inread

        self.fexist=self.exist(inread)
        if not self.fexist: 
            print 'read file ', inread, ' does not exist. Create it'
            file_handle = open(self.read,"w")
            file_handle.write('{"read": {"user": "", "value": "False", "script": ""}}\n')
            file_handle.close()

        self.readf = None
        with open(self.read,'r') as f:
            self.readf = json.load(f)

        self.user=os.environ['USER']
        self.dicread=indic
        self.localdic=''
        self.script=''


#__________________________________________________________
    def exist(self,infile):
        if not os.path.exists(infile): return False
        return True

#__________________________________________________________
    def backup(self,code):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
        self.localdic='%s_%s_%s_%s'%(self.dicread,self.user,code,st)
        os.system('cp %s %s'%(self.dicread,self.localdic))
        self.script=code
        return


#__________________________________________________________
    def comparedics(self,nf=0,ns=0):
        size_ld=os.path.getsize(self.localdic)
        size_od=os.path.getsize(self.dicread)
        ns_local=0
        ns_read=0
        nf_local=0
        nf_read=0

        with open(self.localdic,'r') as f:
            try:
                readf = json.load(f)
                for s in readf:
                    ns_local+=1
                    for j in readf[s]:
                        nf_local+=1
            except ValueError:
                print '\033[91m ----Local dictionnary is corrupted, can not be opened----  \033[0m'
                print '\033[91m ----Please contact clement.helsens@cern.ch or michele.selvaggi@cern.ch---- \033[0m'
                return
            
            
        with open(self.dicread,'r') as f:
            try:
                readf = json.load(f)
                for s in readf:
                    ns_read+=1
                    for j in readf[s]:
                        nf_read+=1
            except ValueError:
                print '\033[91m ----Official dictionnary is corrupted, can not be opened----  \033[0m'
                print '\033[91m ----Please contact clement.helsens@cern.ch or michele.selvaggi@cern.ch---- \033[0m'
                return

        print 'ns_read ',ns_read,'  ns_local  ',ns_local,'  nf_read  ',nf_read,'  nf_local  ',nf_local
        if nf==0 and ns==0:
            if nf_read>nf_local:
                print 'entries have been correctly added. remove local dictionnary.'
                os.system('rm %s'%(self.localdic))
            elif nf_read==nf_local and ns_read==ns_local:
                print 'no entries have been added, only changed job status. Remove local dictionnary.'
                os.system('rm %s'%(self.localdic))
            else:
                print '\033[91m ----Entries have been incorrectly added, dictionnary is truncated----  \033[0m'
                print '\033[91m ----Please contact clement.helsens@cern.ch or michele.selvaggi@cern.ch---- \033[0m'

        elif nf==0 and ns!=0:
            if ns_read+ns==ns_local:
                print '%i samples have been removed. Remove local dictionnary.'%ns
                os.system('rm %s'%(self.localdic))

        else:
            if nf_read+nf>nf_local:
                print 'entries have been correctly added. remove local dictionnary.'
                os.system('rm %s'%(self.localdic))
            elif nf_read+nf==nf_local and ns_read==ns_local:
                print '%i entries have been removed, for failed jobs. Remove local dictionnary.'%nf
                os.system('rm %s'%(self.localdic))
            else:
                print '\033[91m ----Entries have been incorrectly added, dictionnary is truncated----  \033[0m'
                print '\033[91m ----Please contact clement.helsens@cern.ch or michele.selvaggi@cern.ch---- \033[0m'


        return

#__________________________________________________________
    def finalize(self):
        if self.readf['read']['value'] == "True":
            self.readf['read']['value'] = "False"
        else:
            print 'unknown value, not sure why you are here: ',self.readf['read']['value']
        self.write()


#__________________________________________________________
    def reading(self):
        if self.readf['read']['value'] == "True":
            print 'can not run jobs now!'
            print 'USER ===%s=== is running the script ===%s===, this is why the dictonary is not accessible'%(self.user, self.script)
            print 'please retry a bit later or contact ===%s=== as it is possible that the script has crashed'%(self.user)
            print 'If it continues to happend, please contact clement.helsens@cern.ch or michele.selvaggi@cern.ch'
            sys.exit(3)
        elif self.readf['read']['value'] == "False":
            self.readf['read']['value'] = "True"
            self.readf['read']['user'] = self.user
            self.readf['read']['script'] = self.script

        else:
            print 'unknown value: ',self.readf['read']['value']
        self.write()
        return
 
#__________________________________________________________
    def write(self):
        with open(self.read, 'w') as f:
            json.dump(self.readf, f)
        return


#__________________________________________________________
if __name__=="__main__":
    if sys.argv[1]!='secret':
        print 'this is not how to run the script ;0'
        sys.exit(3)

    if len(sys.argv)==4:
        if sys.argv[3]=="secret":
            import EventProducer.config.param_test as para
    else:
        import EventProducer.config.param as para



    inread=''
    if sys.argv[2]=='LHE':
        inread=para.readlhe_dic
    elif 'FCC_' in sys.argv[2]:
        version=sys.argv[2].replace('FCC_','')
        if version not in para.fcc_versions:
            print 'version of the cards should be: fcc_v01, cms'
            print '======================%s======================'%version
            sys.exit(3)
        inread=para.readfcc_dic.replace('VERSION',version)
    else:
        print 'unrecognized mode ',sys.argv[1],'  possible values are FCC or LHE'
        sys.exit(3)


    print inread
    with open(inread,'r') as f:
        inreadf = json.load(f)
        if inreadf['read']['value'] == "True":
            print 'to false'
            inreadf['read']['value'] = "False"
            with open(inread, 'w') as f2:
                json.dump(inreadf, f2)
            
