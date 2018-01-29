import yaml
import os
import EventProducer.common.utils as ut

def makeyaml(outdir, uid):

    if not ut.dir_exist(outdir):
        os.system("mkdir %s"%outdir)
    
    if  outdir[-1]!='/':
        outdir+='/'

    outfile='%sevents_%s.yaml'%(outdir,uid)
    if ut.file_exist(outfile): return False

    data = {
        'processing' : {
            'status' : 'sending'
            } 
        }

    with open(outfile, 'w') as outyaml:
        yaml.dump(data, outyaml, default_flow_style=False) 
        
    return True
