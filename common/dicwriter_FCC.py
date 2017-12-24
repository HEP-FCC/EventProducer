import os,sys
import json
class dicwriter():
    def __init__(self,outname):
        self.outname=outname
        self.fexist=self.exist()
        if not self.fexist: 
            print 'dictionnary ', outname, ' does not exist. Create it'
            file_handle = open(self.outname,"w")
            file_handle.write('{}\n')
            file_handle.close()
        self.mydict = None
        with open(outname) as f:
            self.mydict = json.load(f)
        
    def exist(self):
        if not os.path.exists(self.outname): return False
        return True


    def jobexits(self,sample,jobid):
        if len(self.mydict)==0:return False
        for s in self.mydict:
            if s==sample: 
                for j in self.mydict[sample]:
                    if jobid==j['jobid']: return True
        return False

    def addjob(self,sample,jobid,queue,nevents,status,log,out,batchid,script,inputlhe,plots):
        if self.jobexits(sample,jobid): 
            print 'job already exist ',sample,'   ',jobid
            return
        exist=False
        for s in self.mydict:
            if s==sample: 
                exist=True
                self.mydict[sample].append({'jobid':jobid,'queue':queue,'nevents':nevents,'status':status,'log':log,'out':out,'batchid':batchid,'script':script,'inputlhe':inputlhe,'plots':plots})
        if not exist:
            self.mydict[sample]=[{'jobid':jobid,'queue':queue,'nevents':nevents,'status':status,'log':log,'out':out,'batchid':batchid,'script':script,'inputlhe':inputlhe,'plots':plots}]
        return
    
    def write(self):
        with open(self.outname, 'w') as f:
            json.dump(self.mydict, f)
        return
        

