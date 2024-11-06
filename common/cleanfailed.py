'''
Clean failed jobs
'''

import os
import glob
import os.path
import sys
import yaml
import EventProducer.common.utils as ut


class CleanFailed:
    '''
    Clean failed jobs.
    '''

    # _________________________________________________________________________
    def __init__(self, indir: str, yamldir: str, sample_name: str = ''):
        self.indir = os.path.join(indir, sample_name)
        self.yamldir = os.path.join(yamldir, sample_name)
        self.process = sample_name

    #__________________________________________________________________________
    def clean(self):
        '''
        Do the cleaning.
        '''
        nfailed = 0
        all_files = []
        if self.process == '':
            all_files = glob.glob("%s/*/merge.yaml" % self.yamldir)
        else:
            all_files = glob.glob("%s/merge.yaml" % self.yamldir)

        print("========================= %s/merge.yaml" % self.yamldir)
        for f in all_files:
            print('=====================    ', f)
            with open(f, 'r', encoding='utf-8') as stream:
                try:
                    tmpf = yaml.load(stream, Loader=yaml.FullLoader)
                    if tmpf['merge']['nbad'] == 0:
                        continue
                    nfailed += tmpf['merge']['nbad']
                    for r in tmpf['merge']['outfilesbad']:
                        cmd = "rm %s/%s" % (tmpf['merge']['outdir'], r)
                        print('remove  file  %s   from process  %s' %
                              (r, tmpf['merge']['process']))
                        os.system(cmd)

                        if self.process == '':
                            cmd = "rm %s/%s/%s" % (self.yamldir,
                                                   tmpf['merge']['process'],
                                                   r.replace('.lhe.gz', '.yaml').replace('.root', '.yaml'))
                            os.system(cmd)

                        else:
                            cmd = "rm %s/%s" % (self.yamldir,
                                                r.replace('.lhe.gz', '.yaml').replace('.root', '.yaml'))
                            os.system(cmd)

                except yaml.YAMLError as exc:
                    print(exc)
                except IOError as exc:
                    print("I/O error({0}): {1}".format(exc.errno, exc.strerror))

        print(f'INFO: Removed {nfailed} files.')

    # _________________________________________________________________________
    def cleanoldjobs(self):
        ldir = []
        if self.process == '':
            ldir = next(os.walk(self.yamldir))[1]
        else:
            ldir = [self.process]

        for l in ldir:
            all_files = []
            if self.process == '':
                all_files = glob.glob("%s/%s/events_*.yaml" % (self.yamldir, l))
            else:
                all_files = glob.glob("%s/events_*.yaml" % (self.yamldir))
                print ("%s/events_*.yaml" % (self.yamldir))
            if len(all_files) == 0:
                continue
            process = l
            if self.process != '' and self.process != process:
                print(process)
                continue

            print('process from the input directory ', process)

            for f in all_files:
                if not os.path.isfile(f):
                    print ('file does not exists... %s'%f)
                    continue

                if ut.getsize(f) == 0:
                    print('file size 0 %s  will delete the yaml' % (f))
                    cmd = "rm %s" % (f)
                    print(cmd)
                    os.system(cmd)
                    continue

                with open(f, 'r') as stream:
                    try:
                        tmpf = yaml.load(stream, Loader=yaml.FullLoader)
                        if tmpf['processing']['status'] == 'sending':
                            # from datetime import datetime
                            # import time
                            # ts = time.time()
                            # print(ts)
                            # ds=str(tmpf['processing']['timestamp'])
                            # d = datetime(int(ds[0:4]), int(ds[5:6]), int(ds[7:8]), int(ds[9:10]), int(ds[11:12]))
                            # print int(ds[0:4]), int(ds[4:6]), int(ds[6:8]), int(ds[8:10]), int(ds[10:12])
                            # dt=datetime.timestamp()
                            # print dt

                            if ut.gettimestamp() - tmpf['processing']['timestamp'] > 18000:
                                print('job %s is running since too long  %i  , will delete the yaml' %
                                     (f,ut.gettimestamp() - tmpf['processing']['timestamp']))
                                cmd = "rm %s" % (f)
                                print(cmd)
                                os.system(cmd)

                    except yaml.YAMLError as exc:
                        print(exc)
                    except IOError as e:
                        print(e)
