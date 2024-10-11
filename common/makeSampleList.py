#!/usr/bin/env python3
# this script updates param.py with matching efficiencies and produces one file:
# - "procDict.json" contains a skimmed dictionary containing information for physics analysis in FCCAnalyses

import json
import ast
import os
import sys
import yaml
import EventProducer.common.utils as ut


class makeSampleList():

#__________________________________________________________
    def __init__(self, para, version, detector):
        self.para = para
        self.procList = []
        for fpath in self.para.procList:
            filepath = fpath.replace('VERSION', version)
            filepath = filepath.replace('DETECTOR', detector)
            self.procList.append(filepath)
        self.version   = version
        self.detector  = detector
#______________________________________________________________________________________________________
    def addEntry(self, process, yaml_lhe, yaml_reco, xsec, kf, procDict,proc_param=''):
        processhad=process
        if 'mgp8_' in process:
            processhad=process.replace('mgp8_','mg_')
        #elif 'wzp6_' in process:
        #    processhad=process.replace('wzp6_','wz_')
        elif 'wzp8_' in process:
            processhad=process.replace('wzp8_','wz_')
        elif 'pwp8_' in process:
            processhad=process.replace('pwp8_','pw_')
        elif 'kkmcp8_' in process:
            processhad=process.replace('kkmcp8_','kkmc_')

            
        if  proc_param!='':
            processhad=proc_param.replace('mgp8_','mg_')
            processhad=proc_param.replace('kkmcp8_','kkmc_')

        yaml_lhe=yaml_lhe+'/'+processhad+'/merge.yaml'
        print ('lhe yaml    ',yaml_lhe)
        print ('reco yaml    ',yaml_reco)

        if not ut.file_exist(yaml_lhe): 
            print ('no merged file lhe for process %s continue'%process)
            #sys.exit(3)
            return 1.0

        nmatched = 0
        nweights = 0
        nlhe = 0
 
        matchingEff = 1.0
        
        ylhe=None
        with open(yaml_lhe, 'r') as stream:
            try:
                ylhe = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)

        yreco=None
        with open(yaml_reco, 'r') as stream:
            try:
                yreco = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)

        print (yaml_reco)
        nmatched+= int(yreco['merge']['nevents'])
        try:
            nweights+= float(yreco['merge']['sumofweights'])
        except KeyError as e:
            print ('there is a KeyError  :  ',e)
        for f in ylhe['merge']['outfiles']:
           
            if any(f[0].replace('.lhe.gz','') in s[0] for s in yreco['merge']['outfiles']):
                nlhe+=int(f[1])
                    
            if any(f[0].replace('.stdhep.gz','') in s[0] for s in yreco['merge']['outfiles']):
                nlhe+=int(f[1])
               
                    
        # skip process if do not find corresponding lhes
        if nlhe == 0:
            print ('did not find any LHE event for process', process)
            return matchingEff
       
        if nmatched == 0:
            print ('did not find any FCCSW event for process', process)
            return matchingEff

        # compute matching efficiency ( for FCC-pp only )
        if not 'FCCee' in self.para.module_name:
            matchingEff = round(float(nmatched)/nlhe, 3)
        if nweights==0: nweights=nmatched
        entry = '   "{}": {{"numberOfEvents": {}, "sumOfWeights": {}, "crossSection": {}, "kfactor": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, nweights, xsec, kf, matchingEff)
        print ('N: {}, Nw:{}, xsec: {} , kf: {} pb, eff: {}'.format(nmatched, nweights, xsec, kf, matchingEff))

        procDict.write(entry)

        return matchingEff

#______________________________________________________________________________________________________
    def addEntryPythia(self,process, xsec, kf, yamldir_reco, procDict):

       nmatched = 0
       nweights = 0
       matchingEff = 1.0

       yreco=None
       with open(yamldir_reco, 'r') as stream:
           try:
               yreco = yaml.load(stream, Loader=yaml.FullLoader)
           except yaml.YAMLError as exc:
               print(exc)

       nmatched+= int(yreco['merge']['nevents'])
       
       if nmatched == 0:
           print ('did not find any FCCSW event for process', process)
           return matchingEff

       if nweights==0: nweights=nmatched
       entry = '   "{}": {{"numberOfEvents": {}, "sumOfWeights": {}, "crossSection": {}, "kfactor": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, nweights, xsec, kf, matchingEff)
       print ('N: {}, Nw:{}, xsec: {} , kf: {} pb, eff: {}'.format(nmatched, nweights, xsec, kf, matchingEff))
       print ('entry : ',entry)
       procDict.write(entry)
       return matchingEff
   
#_______________________________________________________________________________________________________
    def makelist(self):

        yamldir_reco=self.para.yamldir+self.version+'/'+self.detector+'/'

        nmatched = 0
        nlhe = 0
        tmpexist=False

        uid=self.para.module_name.replace('.py','').split('/')[1]
        procDict = open('tmp_{}.json'.format(uid), 'w')
        procDict.write('{\n')

        # parse param file
        infile=None
        with open(self.para.module_name) as f:
            infile = f.readlines()

        ldir=next(os.walk(yamldir_reco))[1]
 
        training=False
        if 'training' in self.version: training=True

        extension=""
        if not ( 'spring2021' in self.version or 'pre_fall2022' in self.version or 'dev' in self.version):  # winter2023 and later 
            prodtag = self.version.replace("_training","")
            extension='/'+prodtag+'/'

        if 'FCChh' in self.para.module_name:
            extension = ''

        for l in ldir:
            processhad=None
            process=l
            if 'mgp8_' in process or 'pwp8_' in process or 'kkmcp8_' in process:
                yamldir_lhe=self.para.yamldir+'lhe/'+extension
            elif 'wzp6_' in process or 'wzp8_' in process or 'wz_' in process :
                yamldir_lhe=self.para.yamldir+'stdhep/'+extension
                if training:
                    yamldir_lhe=self.para.yamldir+'stdhep/'+extension+'training/'
                
            yaml_reco=yamldir_reco+'/'+l+'/merge.yaml'
            if not ut.file_exist(yaml_reco): 
                print ('no merged yaml for process %s continue'%l)
                continue

            #if process!='mgp8_pp_z0123j_4f_HT_5000_100000':continue
            print ('')
            print ('------ process: ', process, '-------------')
            print ('')
            
            if 'mgp8_' in process:
                processhad=process.replace('mgp8_','mg_')
            elif 'pwp8_' in process:
                processhad=process.replace('pwp8_','pw_')
            #elif 'wzp6_' in process:
            #    processhad=process.replace('wzp6_','wz_')
            elif 'wzp8_' in process:
                processhad=process.replace('wzp8_','wz_')
            elif 'kkmcp8_' in process:
                processhad=process.replace('kkmcp8_', 'kkmc_')
                
            else: processhad=process
            # maybe this was a decayed process, so it cannot be found as such in in the param file
            br = 1.0
            decay = ''
            for dec in self.para.branching_ratios:
                dec_proc = processhad.split('_')[-1]
                if dec in processhad and dec_proc == dec:
                    br = self.para.branching_ratios[dec]
                    decay = dec
            if decay != '':
                print ('decay---------- ')
                decstr = '_{}'.format(decay)
                proc_param = processhad.replace(decstr,'')
                print ('--------------  ',decstr,'  --  ',proc_param)
                
                try: 
                   xsec = float(self.para.gridpacklist[proc_param][3])*br
                   kf = float(self.para.gridpacklist[proc_param][4])
                   matchingEff = self.addEntry(process, yamldir_lhe, yaml_reco, xsec, kf, procDict,proc_param)
                except KeyError:
                   print ('process {} does not exist in the list'.format(process))

            elif process in self.para.pythialist:
                xsec = float(self.para.pythialist[process][3])
                kf = float(self.para.pythialist[process][4])
                matchingEff = self.addEntryPythia(process, xsec, kf, yaml_reco, procDict)
 

            elif processhad not in self.para.gridpacklist:
                print ('process :', processhad, 'not found in %s --> skipping process'%self.para.module_name)
                continue
            else: 
                print ('self.para.gridpacklist[processhad][3]   ',self.para.gridpacklist[processhad][3])
                print ('self.para.gridpacklist[processhad][4]   ',self.para.gridpacklist[processhad][4])
                xsec = float(self.para.gridpacklist[processhad][3])
                kf=1
                if self.para.gridpacklist[processhad][4]!='':
                    kf = float(self.para.gridpacklist[processhad][4])
                matchingEff = self.addEntry(process, yamldir_lhe, yaml_reco, xsec, kf, procDict)
                # parse new param file
                with open(self.para.module_name) as f:
                    lines = f.readlines()
                    isgp=False
                    for line in range(len(lines)):
                        if 'gridpacklist' in str(lines[line]): isgp=True
                        if isgp==False: continue
                        if processhad == lines[line].rsplit(':', 1)[0].replace("'", ""):
                            ll = ast.literal_eval(lines[line].rsplit(':', 1)[1][:-2])
                            print ('ll   : ',ll)
                            print ('line : ',line)
                            print ('phad : ',processhad)
                            print ('meff : ',matchingEff)
                            infile[line] = "'{}':['{}','{}','{}','{}','{}','{}'],\n".format(processhad, ll[0],ll[1],ll[2],ll[3],ll[4], matchingEff)
                            print ('new line ',infile[line])
                with open("tmp_{}.py".format(uid), "w") as f1:
                   f1.writelines(infile)
                   tmpexist=True
        procDict.close()

        # strip last comma and check the validity of JSON
        print('Loading data from: ', 'tmp_{}.json'.format(uid))
        with open('tmp_{}.json'.format(uid), 'r') as infile:
            data = infile.read()
            proc_dict_string = data[:-2] + '}'

            try:
                proc_dict_json = json.loads(proc_dict_string)
            except json.decoder.JSONDecodeError:
                print('----> Error: Resulting procDict is not valid JSON!')
                sys.exit(3)

        # save procDict to file(s)
        for filepath in self.procList:
            with open(filepath, 'w', encoding='utf-8') as outfile:
                json.dump(proc_dict_json, outfile, indent=4)

        # replace existing param.py file
        if tmpexist:
            retval = os.system(f'diff tmp_{uid}.py {self.para.module_name}')
            if retval > 0:
                retval = os.system(f'cp tmp_{uid}.py {self.para.module_name}')

                if retval > 0:
                    print('ERROR: Update of parameter file unsuccessfull!')
                    return
        os.system('rm -f tmp_{uid}.json')
        os.system('rm -f tmp_{uid}.py')
