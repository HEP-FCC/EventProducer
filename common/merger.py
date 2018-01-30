import yaml
import os
import glob

class merger():

#__________________________________________________________
    def __init__(self, indir):
        self.indir  = indir

#__________________________________________________________
    def merge(self):
        
        ldir=[x[0] for x in os.walk(self.indir)]
        print ldir
       
        for l in ldir:
            outfile=l+'/merge.yaml'
            totsize=0
            totevents=0
            process=None
            outfiles=[]
            outfilesbad=[]

            ndone=0
            nbad=0
            All_files = glob.glob("%s/events_*.yaml"%l)
            if len(All_files)==0:continue

            for f in All_files:
                if not os.path.isfile(f): 
                    print 'file does not exists... %s'%f
                    continue
                
                with open(f, 'r') as stream:
                    try:
                       tmpf = yaml.load(stream)
                       if tmpf['processing']['status']!='DONE':
                           nbad+=1
                           outfilesbad.append(tmpf['processing']['out'].split('/')[-1])
                           continue
                       totsize+=tmpf['processing']['size']
                       totevents+=tmpf['processing']['nevents']
                       process=tmpf['processing']['process']
                       outfiles.append(tmpf['processing']['out'].split('/')[-1])
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
