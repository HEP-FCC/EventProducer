import os
import sys
import yaml
import EventProducer.common.utils as ut


class CheckerEOS:
    '''
    Check files on EOS.
    '''
    # _________________________________________________________________________
    def __init__(self, yamldir, eosdir, process):
        self.process = process
        self.yamldir = yamldir
        self.eosdir = eosdir

    # _________________________________________________________________________
    def touch(self, path):
        with open(path, 'a', encoding='utf-8'):
            os.utime(path, None)

    # _________________________________________________________________________
    def check(self, para):
        if self.process:
            process_names = [self.process]
        else:
            process_names = next(os.walk(self.eosdir))[1]

        if not ut.testeos(para.eostest, para.eostest_size):
            print('ERROR: EOS seems to have problems!')
            print('       Aborting...')
            sys.exit(3)

        dic = {}
        for process_name in process_names:
            # Exclude directories with "wrong" names
            if process_name in ('BADPYTHIA',
                                'lhe',
                                '__restored_files__',
                                'backup'):
                continue

            print('--------------------- ', process_name)

            nfileseos = 0
            process_eos_dir = os.path.join(self.eosdir, process_name)
            process_yaml_dir = os.path.join(self.yamldir, process_name)

            if os.path.isdir(process_eos_dir):
                listeos = [x for x in os.listdir(process_eos_dir)
                           if 'events' in x]
                nfileseos = len(listeos)

            if nfileseos == 0:
                continue

            mergefile_path = os.path.join(self.yamldir, process_name,
                                          'merge.yaml')
            print('INFO: Merge file:')
            print(f'        - {mergefile_path}')
            checkfile_path = os.path.join(self.yamldir, process_name, 'check')
            print('INFO: Check file:')
            print(f'        - {checkfile_path}')
            if not ut.file_exist(mergefile_path):
                if not ut.dir_exist(process_yaml_dir):
                    os.system(f'mkdir -p {process_yaml_dir}')
                self.touch(checkfile_path)
                continue

            if not os.path.isdir(self.yamldir):
                os.system(f'mkdir {self.yamldir}')

            tmpf = None
            with open(mergefile_path, 'r', encoding='utf-8') as stream:
                try:
                    tmpf = yaml.load(stream, Loader=yaml.FullLoader)
                except yaml.YAMLError as exc:
                    print(exc)

            bad_tot = tmpf['merge']['nbad']
            files_tot = tmpf['merge']['ndone']

            ntot_files = bad_tot + files_tot
            print("tot files  ", ntot_files, "  files eos  ", nfileseos)
            dic[process_name] = {'neos': nfileseos, 'nmerged': ntot_files}
            print(checkfile_path)
            if ntot_files < nfileseos:
                self.touch(checkfile_path)
            elif ntot_files > nfileseos:
                os.system(f'rm -f {process_yaml_dir}/events*.yaml')
                os.system(f'rm -f {mergefile_path}')
            else:
                if ut.file_exist(checkfile_path):
                    os.system(f'rm -f {checkfile_path}')

        outfile = os.path.join(self.yamldir, 'files.yaml')
        with open(outfile, 'w', encoding='utf-8') as outyaml:
            yaml.dump(dic, outyaml, default_flow_style=False)
