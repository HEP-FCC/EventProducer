'''
Class to merge YAML files.
'''

import os
import glob
import time
import yaml
import EventProducer.common.utils as ut


class Merger:
    '''
    Merges info YAML files.
    '''
    # _________________________________________________________________________
    def __init__(self, process, yamldir):
        self.yamldir = yamldir
        self.process = process

    # _________________________________________________________________________
    def merge(self, force):
        '''
        Do the actual merge.
        '''
        print('INFO: Merging samples located in:')
        print(f'        - {self.yamldir}')
        ldir = next(os.walk(self.yamldir))[1]

        for process_name in ldir:
            if self.process not in ('', process_name):
                continue

            mergefile_path = os.path.join(self.yamldir, process_name,
                                          'merge.yaml')
            totsize = 0
            totevents = 0
            sumofweights = 0
            process = None
            outfiles = []
            outfilesbad = []
            outdir = None
            ndone = 0
            nbad = 0

            print(f'INFO: Processing sample: {process_name}')

            infile_pattern = os.path.join(self.yamldir, process_name,
                                          'events_*.yaml')
            all_files = glob.glob(infile_pattern)
            print('INFO: Searching for input YAML files with pattern:')
            print(f'        - {infile_pattern}')

            if len(all_files) == 0:
                if os.path.isfile(mergefile_path):
                    os.system(f'rm {mergefile_path}')
                continue

            # Continue if process has been checked
            checkfile_path = os.path.join(self.yamldir, process_name, 'check')
            if not ut.file_exist(checkfile_path) and not force:
                print('INFO: Sample already checked.')
                print('      Continuing...')
                continue

            print(f'INFO: Merging process: {process_name}')
            print(f'      Found {len(all_files)} files')
            for infile_path in all_files:
                if not os.path.isfile(infile_path):
                    print('WARNING: Input YAML file does not exists!')
                    print(f'           - {infile_path}')
                    continue

                with open(infile_path, 'r', encoding='utf-8') as stream:
                    try:
                        tmpf = yaml.load(stream, Loader=yaml.FullLoader)
                        if ut.getsize(infile_path) == 0:
                            continue
                        if tmpf['processing']['status'] == 'sending':
                            continue
                        if tmpf['processing']['status'] == 'BAD':
                            nbad += 1
                            outfilesbad.append(
                                tmpf['processing']['out'].split('/')[-1]
                            )
                            outdir = tmpf['processing']['out'].replace(
                                tmpf['processing']['out'].split('/')[-1], ''
                            )
                            process = tmpf['processing']['process']

                            continue
                        totsize += tmpf['processing']['size']
                        totevents += tmpf['processing']['nevents']

                        # need this not to break LHE merge that does not
                        # contain key 'sumofweights'
                        if 'sumofweights' in tmpf['processing']:
                            sumofweights += float(
                                    tmpf['processing']['sumofweights']
                            )
                        process = tmpf['processing']['process']
                        tmplist = [tmpf['processing']['out'].split('/')[-1],
                                   tmpf['processing']['nevents']]
                        outfiles.append(tmplist)
                        outdir = tmpf['processing']['out'].replace(
                            tmpf['processing']['out'].split('/')[-1], ''
                        )
                        ndone += 1
                    except yaml.YAMLError as exc:
                        print(exc)
                    except IOError as exc:
                        print(f'I/O error({exc.errno}): {exc.strerror}')
                        print("outfile ", infile_path)

            dic = {'merge': {
                     'process': process,
                     'nevents': totevents,
                     'sumofweights': sumofweights,
                     'outfiles': outfiles,
                     'outdir': outdir,
                     'size': totsize,
                     'ndone': ndone,
                     'nbad': nbad,
                     'outfilesbad': outfilesbad}
                   }
            try:
                with open(mergefile_path, 'w', encoding='utf-8') as outyaml:
                    yaml.dump(dic, outyaml, default_flow_style=False)
            except IOError as exc:
                print(f'I/O error({exc.errno}): {exc.strerror}')
                print("outfile ", mergefile_path)
                time.sleep(10)
                with open(mergefile_path, 'w', encoding='utf-8') as outyaml:
                    yaml.dump(dic, outyaml, default_flow_style=False)
