import yaml
import os
import glob
import time
import EventProducer.common.utils as ut

class merger():

#__________________________________________________________
    def __init__(self, process, yamldir):
        self.indir = yamldir
        self.process = process
#__________________________________________________________
    def merge(self, force):
        
        ldir=next(os.walk(self.indir))[1]
        print (self.indir,'  ====  ',self.process)
        #ldir=[x[0] for x in os.walk(self.indir)]
       
        for l in ldir:
            if self.process!='' and self.process!=l: 
                continue
            outfile=self.indir+'/'+l+'/merge.yaml'
            totsize=0
            totevents=0
            sumofweights=0
            process=None
            outfiles=[]
            outfilesbad=[]
            outdir=None
            ndone=0
            nbad=0
            All_files = glob.glob("%s/%s/events_*.yaml"%(self.indir,l))
            print ("%s/%s/events_*.yaml"%(self.indir,l))

            if len(All_files)==0:
                if os.path.isfile("%s/%s/merge.yaml"%(self.indir,l)):
                    os.system("rm %s/%s/merge.yaml"%(self.indir,l))
                continue
            
            #continue if process has been checked
            print ('%s/%s/check'%(self.indir,l))
            if not ut.file_exist('%s/%s/check'%(self.indir,l)) and not force: continue

            print ('merging process %s  %i files'%(l,len(All_files)))
            for f in All_files:
                if not os.path.isfile(f): 
                    print ('file does not exists... %s'%f)
                    continue
                
                with open(f, 'r') as stream:
                    try:
                        tmpf = yaml.load(stream, Loader=yaml.FullLoader)
                        if ut.getsize(f)==0: continue
                        if tmpf['processing']['status']=='sending': continue
                        if tmpf['processing']['status']=='BAD':
                            nbad+=1
                            outfilesbad.append(tmpf['processing']['out'].split('/')[-1])
                            outdir=tmpf['processing']['out'].replace(tmpf['processing']['out'].split('/')[-1],'')
                            process=tmpf['processing']['process']

                            continue
                        totsize+=tmpf['processing']['size']
                        totevents+=tmpf['processing']['nevents']
                        
			## need this not to break LHE merge that does not contain key 'sumofweights'
                        if 'sumofweights' in tmpf['processing']:
                            sumofweights+=float(tmpf['processing']['sumofweights'])
                        process=tmpf['processing']['process']
                        tmplist=[tmpf['processing']['out'].split('/')[-1], tmpf['processing']['nevents']]
                        outfiles.append(tmplist)
                        outdir=tmpf['processing']['out'].replace(tmpf['processing']['out'].split('/')[-1],'')
                        ndone+=1
                    except yaml.YAMLError as exc:
                        print(exc)
                    except IOError as exc:
                        print ("I/O error({0}): {1}".format(exc.errno, exc.strerror))
                        print ("outfile ",f)
                        
            dic = {'merge':{
                    'process':process, 
                    'nevents':totevents,
                    'sumofweights':sumofweights,
                    'outfiles':outfiles,
                    'outdir':outdir,
                    'size':totsize,
                    'ndone':ndone,
                    'nbad':nbad,
                    'outfilesbad':outfilesbad,
                    }
                   }
            try:
                with open(outfile, 'w') as outyaml:
                    yaml.dump(dic, outyaml, default_flow_style=False) 
            except IOError as exc:
                print ("I/O error({0}): {1}".format(exc.errno, exc.strerror))
                print ("outfile ",outfile)
                time.sleep(10)
                with open(outfile, 'w') as outyaml:
                    yaml.dump(dic, outyaml, default_flow_style=False)

