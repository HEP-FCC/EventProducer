import os
import sys
import json
import yaml
import EventProducer.common.utils as ut


class MakeSampleList:
    '''
    Generate sample list.
    Resulting procDict.json contains a skimmed dictionary containing
    information for physics analysis.

    Updates also parameters file with matching efficiencies.
    '''

# _____________________________________________________________________________
    def __init__(self, para, version, detector):
        self.para = para
        self.outpaths = []
        for fpath in self.para.procList:
            filepath = fpath.replace('VERSION', version)
            filepath = filepath.replace('DETECTOR', detector)
            filepath = filepath.replace('_.', '.')
            self.outpaths.append(filepath)
        self.version = version
        self.detector = detector

# _____________________________________________________________________________
    def addEntry(self, process, yaml_lhe, yaml_reco, xsec, kf, proc_dict,
                 proc_param=''):
        processhad = process
        if 'mgp8_' in process:
            processhad = process.replace('mgp8_', 'mg_')
        # elif 'wzp6_' in process:
        #     processhad = process.replace('wzp6_', 'wz_')
        elif 'wzp8_' in process:
            processhad = process.replace('wzp8_', 'wz_')
        elif 'pwp8_' in process:
            processhad = process.replace('pwp8_', 'pw_')
        elif 'kkmcp8_' in process:
            processhad = process.replace('kkmcp8_', 'kkmc_')

        if proc_param != '':
            processhad = proc_param.replace('mgp8_', 'mg_')
            processhad = proc_param.replace('kkmcp8_', 'kkmc_')

        yaml_lhe = os.path.join(yaml_lhe, processhad, 'merge.yaml')
        print('INFO: LHE yaml:', yaml_lhe)
        print('INFO: Reco. yaml:', yaml_reco)

        if not ut.file_exist(yaml_lhe):
            print(f'WARNING: No merged LHE file for process "{process}"\n'
                  'Skipping...')
            # sys.exit(3)
            return 1.0

        nmatched = 0
        nweights = 0
        nlhe = 0

        matching_eff = 1.0

        ylhe = None
        with open(yaml_lhe, 'r', encoding='utf-8') as stream:
            try:
                ylhe = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)

        yreco = None
        with open(yaml_reco, 'r', encoding='utf-8') as stream:
            try:
                yreco = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)

        nmatched += int(yreco['merge']['nevents'])
        try:
            nweights += float(yreco['merge']['sumofweights'])
        except KeyError as e:
            print('there is a KeyError:  ', e)
        for f in ylhe['merge']['outfiles']:

            if any(f[0].replace('.lhe.gz', '') in
                   s[0] for s in yreco['merge']['outfiles']):
                nlhe += int(f[1])

            if any(f[0].replace('.stdhep.gz', '') in
                   s[0] for s in yreco['merge']['outfiles']):
                nlhe += int(f[1])

        # skip process if do not find corresponding lhes
        if nlhe == 0:
            print('did not find any LHE event for process', process)
            return matching_eff

        if nmatched == 0:
            print('did not find any FCCSW event for process', process)
            return matching_eff

        # compute matching efficiency ( for FCC-pp only )
        if 'FCCee' not in self.para.module_name:
            matching_eff = round(float(nmatched)/nlhe, 3)
        if nweights == 0:
            nweights = nmatched
        entry = '   "{}": {{"numberOfEvents": {}, "sumOfWeights": {}, "crossSection": {}, "kfactor": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, nweights, xsec, kf, matching_eff)
        print('N: {}, Nw:{}, xsec: {} , kf: {} pb, eff: {}'.format(nmatched, nweights, xsec, kf, matching_eff))

        proc_dict.write(entry)

        return matching_eff

    # _________________________________________________________________________
    def addEntryPythia(self, process, xsec, kf, yamldir_reco, proc_dict):

        nmatched = 0
        nweights = 0
        matching_eff = 1.0

        yreco = None
        with open(yamldir_reco, 'r', encoding='utf-8') as stream:
            try:
                yreco = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)

        nmatched += int(yreco['merge']['nevents'])

        if nmatched == 0:
            print('did not find any FCCSW event for process', process)
            return matching_eff

        if nweights == 0:
            nweights = nmatched
        entry = '   "{}": {{"numberOfEvents": {}, "sumOfWeights": {}, "crossSection": {}, "kfactor": {}, "matchingEfficiency": {}}},\n'.format(process, nmatched, nweights, xsec, kf, matching_eff)
        print('N: {}, Nw:{}, xsec: {} , kf: {} pb, eff: {}'.format(nmatched, nweights, xsec, kf, matching_eff))
        print('entry : ', entry)
        proc_dict.write(entry)

        return matching_eff

    # _________________________________________________________________________
    def makelist(self):
        '''
        Generate procDict JSON.
        '''
        yamldir_reco = os.path.join(self.para.yamldir,
                                    self.version, self.detector)

        uid = self.para.module_name.replace('.py', '').split('/')[1]
        proc_dict = open(f'tmp_{uid}.json', 'w', encoding='utf-8')
        proc_dict.write('{\n')

        # Load parameters file as text
        with open(self.para.module_name, 'r', encoding='utf-8') as infile:
            param_text = infile.readlines()

        ldir = next(os.walk(yamldir_reco))[1]

        training = False
        if 'training' in self.version:
            training = True

        extension = ""
        if not ('spring2021' in self.version or
                'pre_fall2022' in self.version or
                'dev' in self.version):  # winter2023 and later
            extension = self.version.replace("_training", "")

        if 'FCChh' in self.para.module_name:
            extension = ''

        for l in ldir:
            processhad = None
            process = l
            if 'mgp8_' in process or \
               'pwp8_' in process or \
               'kkmcp8_' in process:
                yamldir_lhe = os.path.join(self.para.yamldir, 'lhe', extension)
            elif 'wzp6_' in process or 'wzp8_' in process or 'wz_' in process:
                yamldir_lhe = os.path.join(self.para.yamldir,
                                           'stdhep', extension)
                if training:
                    yamldir_lhe = os.path.join(self.para.yamldir, 'stdhep',
                                               extension+'training')

            yaml_reco = os.path.join(yamldir_reco, l, 'merge.yaml')
            if not ut.file_exist(yaml_reco):
                print(f'no merged yaml for process {l} continue')
                continue

            # if process!='mgp8_pp_z0123j_4f_HT_5000_100000':continue
            print('')
            print('------ process: ', process, '-------------')
            print('')

            if 'mgp8_' in process:
                processhad = process.replace('mgp8_', 'mg_')
            elif 'pwp8_' in process:
                processhad = process.replace('pwp8_', 'pw_')
            # elif 'wzp6_' in process:
            #     processhad=process.replace('wzp6_', 'wz_')
            elif 'wzp8_' in process:
                processhad = process.replace('wzp8_', 'wz_')
            elif 'kkmcp8_' in process:
                processhad = process.replace('kkmcp8_', 'kkmc_')
            else:
                processhad = process

            # Maybe this was a decayed process, so it cannot be found as such
            # in in the param file
            br = 1.0
            decay = ''
            for dec in self.para.branching_ratios:
                dec_proc = processhad.split('_')[-1]
                if dec in processhad and dec_proc == dec:
                    br = self.para.branching_ratios[dec]
                    decay = dec
            if decay != '':
                print('decay---------- ')
                decstr = f'_{decay}'
                proc_param = processhad.replace(decstr, '')
                print('--------------  ', decstr, '  --  ', proc_param)

                try:
                    xsec = float(self.para.gridpacklist[proc_param][3]) * br
                    kf = float(self.para.gridpacklist[proc_param][4])
                    matching_eff = self.addEntry(process,
                                                 yamldir_lhe, yaml_reco,
                                                 xsec, kf, proc_dict,
                                                 proc_param)
                except KeyError:
                    print(f'process "{process}" does not exist in the list')

            elif process in self.para.pythialist:
                xsec = float(self.para.pythialist[process][3])
                kf = float(self.para.pythialist[process][4])
                matching_eff = self.addEntryPythia(process, xsec, kf,
                                                   yaml_reco, proc_dict)

            elif processhad not in self.para.gridpacklist:
                print('process:', processhad,
                      f'not found in {self.para.module_name}',
                      '--> skipping process')
                continue
            else:
                print('self.para.gridpacklist[processhad][3]:',
                      self.para.gridpacklist[processhad][3])
                print('self.para.gridpacklist[processhad][4]:',
                      self.para.gridpacklist[processhad][4])
                xsec = float(self.para.gridpacklist[processhad][3])
                kf = 1
                if self.para.gridpacklist[processhad][4] != '':
                    kf = float(self.para.gridpacklist[processhad][4])
                matching_eff = self.addEntry(process, yamldir_lhe, yaml_reco,
                                             xsec, kf, proc_dict)
                # Replace process line with updated matching efficiency
                pass_gp = False
                for line_idx, line in enumerate(param_text):
                    if 'gridpacklist' in line:
                        pass_gp = True
                    if pass_gp is False:
                        continue
                    if not line:
                        continue
                    if line.strip().startswith('#'):
                        continue

                    process_line_head = \
                        line.rsplit(':', 1)[0].replace("'", "")
                    if processhad == process_line_head.strip():
                        print(line[:-2])
                        line_elems = line.rsplit(',')
                        if '\'' in line_elems[-2]:
                            matching_eff_elems = line_elems[-2].rsplit('\'')
                            matching_eff_elems[-2] = str(matching_eff)
                            line_elems[-2] = '\''.join(matching_eff_elems)
                        if '"' in line_elems[-2]:
                            matching_eff_elems = line_elems[-2].rsplit('"')
                            matching_eff_elems[-2] = str(matching_eff)
                            line_elems[-2] = '"'.join(matching_eff_elems)
                        param_text[line_idx] = ','.join(line_elems)
                        print(param_text[line_idx][:-2])
        proc_dict.close()

        # strip last comma and check the validity of JSON
        with open(f'tmp_{uid}.json', 'r', encoding='utf-8') as infile:
            data = infile.read()
            if len(data) > 2:
                proc_dict_string = data[:-2]
            else:
                proc_dict_string = data
            proc_dict_string += '\n}'

            try:
                proc_dict_json = json.loads(proc_dict_string)
            except json.decoder.JSONDecodeError:
                print('ERROR: Resulting procDict is not valid JSON!')
                print('       Aborting...')
                sys.exit(3)

        # save procDict to file(s)
        print('INFO: Saving procDict JSON into:')
        for filepath in self.outpaths:
            print(f'  - {filepath}')
            with open(filepath, 'w', encoding='utf-8') as outfile:
                json.dump(proc_dict_json, outfile, indent=4)
        os.system(f'rm -f tmp_{uid}.json')

        # Save temporary version of the parameters file
        with open(f'tmp_{uid}.py', "w", encoding='utf-8') as f1:
            f1.writelines(param_text)

        # Replace existing parameters file if different
        retval = os.system(f'diff tmp_{uid}.py {self.para.module_name}')
        if retval > 0:
            retval = os.system(f'cp tmp_{uid}.py {self.para.module_name}')

            if retval > 0:
                print('ERROR: Update of parameter file unsuccessful!')
                return
        os.system(f'rm -f tmp_{uid}.py')
