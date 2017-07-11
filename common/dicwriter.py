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
                    if jobid==int(j['jobid']): return True
        return False

    def addjob(self,sample,jobid,queue,nevents,status,log,out,batchid,script):
        if self.jobexits(sample,jobid): 
            return
        exist=False
        for s in self.mydict:
            if s==sample: 
                exist=True
                self.mydict[sample].append({'jobid':jobid,'queue':queue,'nevents':nevents,'status':status,'log':log,'out':out,'batchid':batchid,'script':script})
        if not exist:
            self.mydict[sample]=[{'jobid':jobid,'queue':queue,'nevents':nevents,'status':status,'log':log,'out':out,'batchid':batchid,'script':script}]
        return
    


    def addjob_new(self, dic):
        if self.jobexits(dic['sample'],dic['jobid']): 
            return

        toadd={}
        for k, v in dic.iteritems():
            toadd.update({'%s'%k:'%s'%v})
 
        exist=False
        for s in self.mydict:
            if s==dic['sample']: 
                exist=True
                self.mydict[dic['sample']].append(toadd)
        if not exist:
            self.mydict[dic['sample']]=[toadd]
        return

    def write(self):
        with open(self.outname, 'w') as f:
            json.dump(self.mydict, f)
        return
        

