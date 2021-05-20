#!/usr/bin/env python

# this script updates param.py with matching efficiencies and produces two files:
# - "heppySampleList.py" contains the list of FCCSW root files properly formatted for heppy
# - "procDict.json" contains a skimmed dictionary containing information for physics analysis
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
        self.heppyList = self.para.heppyList.replace('VERSION',version).replace('DETECTOR',detector)
        self.procList  = self.para.procList.replace('VERSION',version).replace('DETECTOR',detector)
        self.version   = version
        self.detector  = detector
#______________________________________________________________________________________________________
    def addEntry(self, process, yaml_lhe, yaml_reco, xsec, kf, heppyFile, procDict,proc_param=''):
        processhad=process
        if 'mgp8_' in process:
            processhad=process.replace('mgp8_','mg_')
        if  proc_param!='':
            processhad=proc_param.replace('mgp8_','mg_')

        yaml_lhe=yaml_lhe+'/'+processhad+'/merge.yaml'
        print ('lhe yaml    ',yaml_lhe)
        print ('reco yaml    ',yaml_reco)

        if not ut.file_exist(yaml_lhe): 
            print ('no merged file lhe for process %s continue'%process)
            sys.exit(3)
            return 1.0

        

        nmatched = 0
        nweights = 0
        nlhe = 0
 
        heppyFile.write('{} = cfg.MCComponent(\n'.format(process))
        heppyFile.write("    \'{}\',\n".format(process))
        heppyFile.write('    files=[\n')

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
                if yreco['merge']['outdir'][-1]!='/':
                    heppyFile.write("           '/{}/{}',\n".format(yreco['merge']['outdir'],f[0].replace('.lhe.gz','.root')))
                else:
                    heppyFile.write("           '/{}{}',\n".format(yreco['merge']['outdir'],f[0].replace('.lhe.gz','.root')))

        heppyFile.write(']\n')
        heppyFile.write(')\n')
        heppyFile.write('\n')

        # skip process if do not find corresponding lhes
        if nlhe == 0:
            print ('did not find any LHE event for process', process)
            return matchingEff
       
        if nmatched == 0:
            print ('did not find any FCCSW event for process', process)
            return matchingEff

        # compute matching efficiency
        matchingEff = round(float(nmatched)/nlhe, 3)
        if nweights==0: nweights=nmatched
        entry = '   "{}": {{"numberOfEvents": {}, "sumOfWeights": {}, "crossSection": {}, "kfactor": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, nweights, xsec, kf, matchingEff)
        print ('N: {}, Nw:{}, xsec: {} , kf: {} pb, eff: {}'.format(nmatched, nweights, xsec, kf, matchingEff))

        procDict.write(entry)

        return matchingEff

#______________________________________________________________________________________________________
    def addEntryPythia(self,process, xsec, kf, yamldir_reco, heppyFile, procDict):

       heppyFile.write('{} = cfg.MCComponent(\n'.format(process))
       heppyFile.write("    \'{}\',\n".format(process))
       heppyFile.write('    files=[\n')     

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
       for f in yreco['merge']['outfiles']:
           if yreco['merge']['outdir'][-1]!='/':
               heppyFile.write("           '/{}/{}',\n".format(yreco['merge']['outdir'],f[0]))
           else: 
               heppyFile.write("           '/{}{}',\n".format(yreco['merge']['outdir'],f[0]))

       heppyFile.write(']\n')
       heppyFile.write(')\n')
       heppyFile.write('\n')
       
       if nmatched == 0:
           print ('did not find any FCCSW event for process', process)
           return matchingEff

       if nweights==0: nweights=nmatched
       entry = '   "{}": {{"numberOfEvents": {}, "sumOfWeights": {}, "crossSection": {}, "kfactor": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, nweights, xsec, kf, matchingEff)
       print ('N: {}, Nw:{}, xsec: {} , kf: {} pb, eff: {}'.format(nmatched, nweights, xsec, kf, matchingEff))
       procDict.write(entry)
       return matchingEff
   
#_______________________________________________________________________________________________________
    def makelist(self):

        yamldir_lhe=self.para.yamldir+'lhe/'
        yamldir_reco=self.para.yamldir+self.version+'/'+self.detector+'/'

        nmatched = 0
        nlhe = 0
        tmpexist=False
        # write header for heppy file
        procDict = open('tmp.json', 'w')
        procDict.write('{\n')

        # write header for heppy file
        heppyFile = open(self.heppyList, 'w')
        heppyFile.write('import heppy.framework.config as cfg\n')
        heppyFile.write('\n')

        # parse param file
        infile=None
        with open(self.para.module_name) as f:
            infile = f.readlines()

        ldir=next(os.walk(yamldir_reco))[1]

        for l in ldir:
            processhad=None
            process=l

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
                   matchingEff = self.addEntry(process, yamldir_lhe, yaml_reco, xsec, kf, heppyFile, procDict,proc_param)
                except KeyError:
                   print ('process {} does not exist in the list'.format(process))

            elif process in self.para.pythialist:
                xsec = float(self.para.pythialist[process][3])
                kf = float(self.para.pythialist[process][4])
                matchingEff = self.addEntryPythia(process, xsec, kf, yaml_reco, heppyFile, procDict)
 

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
                matchingEff = self.addEntry(process, yamldir_lhe, yaml_reco, xsec, kf, heppyFile, procDict)
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
                with open("tmp.py", "w") as f1:
                   f1.writelines(infile)
                   tmpexist=True
        procDict.close()
        # parse param file

        # strip last comma
        with open('tmp.json', 'r') as myfile:
            data=myfile.read()
            newdata = data[:-2]

        # close header for heppy file
        procDict = open(self.procList, 'w')
        procDict.write(newdata)
        procDict.write('\n')
        procDict.write('}\n')
        
        # replace existing param.py file
        if tmpexist:
            os.system("mv tmp.py %s"%self.para.module_name)
        os.system("rm tmp.json")
