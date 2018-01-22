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
                    if int(jobid)==int(j['jobid']): return True
        return False

 
    def addjob(self, dic):
        if self.jobexits(dic['process'],dic['jobid']): 
            print 'job already exists in the dic'
            return

        toadd={}
        for k, v in dic.iteritems():
            if k=='process':continue
            toadd.update({'%s'%k:'%s'%v})
 
        exist=False
        for s in self.mydict:
            if s==dic['process']: 
                exist=True
                self.mydict[dic['process']].append(toadd)
        if not exist:
            self.mydict[dic['process']]=[toadd]
        return

    def write(self):
        with open(self.outname, 'w') as f:
            json.dump(self.mydict, f)
        return
        

