import yaml
import os
import glob
import EventProducer.common.utils as ut

class merger():

#__________________________________________________________
    def __init__(self, para, process, yamldir, yamlcheck):
        self.indir = yamldir
        self.yamlcheck = yamlcheck
        self.process = process
#__________________________________________________________
    def merge(self, force):
        
        ldir=next(os.walk(self.indir))[1]
        print self.indir,'  ====  ',self.process
        #ldir=[x[0] for x in os.walk(self.indir)]
       
        for l in ldir:
            if self.process!='' and self.process!=l: 
                continue
            outfile=self.indir+'/'+l+'/merge.yaml'
            totsize=0
            totevents=0
            process=None
            outfiles=[]
            outfilesbad=[]
            outdir=None
            ndone=0
            nbad=0
            All_files = glob.glob("%s/%s/events_*.yaml"%(self.indir,l))
            if len(All_files)==0:continue

            #continue if process has been checked
            if ut.yamlcheck(self.yamlcheck, l) and not force:continue

            print 'merging process %s  %i files'%(l,len(All_files))
            for f in All_files:
                if not os.path.isfile(f): 
                    print 'file does not exists... %s'%f
                    continue
                
                with open(f, 'r') as stream:
                    try:
                        tmpf = yaml.load(stream)
                        if tmpf['processing']['status']=='sending': continue
                        if tmpf['processing']['status']=='BAD':
                            nbad+=1
                            outfilesbad.append(tmpf['processing']['out'].split('/')[-1])
                            outdir=tmpf['processing']['out'].replace(tmpf['processing']['out'].split('/')[-1],'')

                            continue
                        totsize+=tmpf['processing']['size']
                        totevents+=tmpf['processing']['nevents']
                        process=tmpf['processing']['process']
                        tmplist=[tmpf['processing']['out'].split('/')[-1], tmpf['processing']['nevents']]
                        outfiles.append(tmplist)
                        outdir=tmpf['processing']['out'].replace(tmpf['processing']['out'].split('/')[-1],'')
                        ndone+=1
                    except yaml.YAMLError as exc:
                        print(exc)
                        
            dic = {'merge':{
                    'process':process, 
                    'nevents':totevents,
                    'outfiles':outfiles,
                    'outdir':outdir,
                    'size':totsize,
                    'ndone':ndone,
                    'nbad':nbad,
                    'outfilesbad':outfilesbad,
                    }
                   }
            with open(outfile, 'w') as outyaml:
                yaml.dump(dic, outyaml, default_flow_style=False) 
            if ndone+nbad==len(All_files):
                ut.yamlstatus(self.yamlcheck, process, True)
