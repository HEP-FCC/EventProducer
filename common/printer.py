'''
Prints sample metadata to a text file.
'''

import sys
import os
import re
import time
import json
import yaml


class Printer:
    '''
    Prints sample metadata to a text file.
    '''
    def __init__(self,
                 yamldir: str,
                 outpath: str,
                 matching: bool,
                 is_lhe: bool,
                 para: object,
                 detector: str = '',
                 version: str = ''):
        self.yamldir = yamldir
        self.outpath_txt = outpath
        self.outpath_json = os.path.splitext(self.outpath_txt)[0] + '.json'
        self.matching = matching
        self.is_lhe = is_lhe
        self.para = para
        self.version = version
        self.detector = detector

        self.tot_size = 0
        self.ntot_events = 0
        self.ntot_files = 0
        self.ntot_bad = 0
        self.ntot_eos = 0
        self.ntot_sumw = 0

    # _____________________________________________________________________________
    def comma_me(self, amount):
        orig = amount
        new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', amount)
        if orig == new:
            return new
        return self.comma_me(new)

    # _____________________________________________________________________________
    def run(self):
        '''
        Generate the sample text file.
        '''
        process_names = next(os.walk(self.yamldir))[1]

#        checkfiles=''
#        if self.isLHE: checkfiles='%s/files.yaml'%(self.para.lhe_dir)
#        else:          checkfiles='%s/%s/files.yaml'%(self.para.delphes_dir,self.version)
#
#        tmpcheck=None
#        with open(checkfiles, 'r') as stream:
#            try:
#                tmpcheck = yaml.load(stream, Loader=yaml.FullLoader)
#            except yaml.YAMLError as exc:
#                print(exc)

        out_text = ''
        out_dict = {}
        out_dict['processes'] = []
        for process_name in process_names:
            print(f'--------------------------  {process_name}')

            mergefile_path = os.path.join(self.yamldir, process_name,
                                          'merge.yaml')

            if not os.path.isfile(mergefile_path):
                print('WARNING: Ignoring the process --- not merged yet!')
                print('         Continuing...')
                continue

            tmpf = None
            with open(mergefile_path, 'r', encoding='utf-8') as stream:
                try:
                    tmpf = yaml.load(stream, Loader=yaml.FullLoader)
                except yaml.YAMLError as exc:
                    print(exc)
                except IOError as exc:
                    print(exc)
                    print('file  ', mergefile_path)
                    time.sleep(10)
                    tmpf = yaml.load(stream, Loader=yaml.FullLoader)

            events_tot = tmpf['merge']['nevents']
            size_tot = tmpf['merge']['size']
            nfiles_bad = tmpf['merge']['nbad']
            nfiles_good = tmpf['merge']['ndone']
            # Sum of weights is made identical to number of events
            # if not found in the merge file.
            try:
                sumw_tot = float(tmpf['merge']['sumofweights'])
            except KeyError:
                sumw_tot = float(events_tot)

            # Adjust process name
            process_name_short = process_name.replace('mgp8_', 'mg_')
            process_name_short = process_name_short.replace('kkmcp8_', 'kkmc_')
            print(f'INFO: Shortening sample name to "{process_name_short}"')
            news = str(process_name_short)
            proc = str(process_name_short)

            br = 1.0
            decay = ''
            decstr = ''
            for dec in self.para.branching_ratios:
                dec_proc = proc.split('_', maxsplit=1)[-1]
                if dec in proc and dec_proc == dec:
                    br = self.para.branching_ratios[dec]
                    decay = dec
            if decay != '':
                print('decay---------- ', decay, ' ------- br ', br)
                decstr = f'_{decay}'

            ispythiaonly = False

            try:
                teststring = self.para.gridpacklist[proc][0]
            except IOError as err:
                print(f'I/O error({err.errno}): {err.strerror}')
            except ValueError:
                print("Could not convert data to an integer.")
            except KeyError as err:
                print(f'I got a KeyError 1 --- reason "{err}"')
                ssplit = proc.split('_')
                stest = ''
                ntest = 1
                if '_HT_' in proc:
                    ntest = 4
                for procn in range(0, len(ssplit) - ntest):
                    stest += ssplit[procn] + '_'

                stest = stest[0:len(stest)-1]
                proc = stest
# CLEMENT TO BE FIXED
                if decay != '':
                    proc = proc.replace(decstr, '')
                    print('--------------  ', decstr, '  --  ', proc)

                try:
                    teststringdecay = self.para.decaylist[stest][0]
                except IOError as err2:
                    print(f'I/O error({err2.errno}): {err2.strerror}')
                except ValueError:
                    print("Could not convert data to an integer.")
                except KeyError as err2:
                    print(f'I got a KeyError 2 - reason "{err2}"')
                    try:
                        teststringpythia = self.para.pythialist[news][0]
                        ispythiaonly = True
                    except IOError as e:
                        print(f'I/O error({e.errno}): {e.strerror}')
                    except ValueError:
                        print("Could not convert data to an integer.")
                    except KeyError as e:
                        print(f'I got a KeyError 3 - reason "{e}"')
                        if news.split('_', maxsplit=1)[0] == "p8":
                            ispythiaonly = True
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise

            if not ispythiaonly:
                try:
                    stupidtest = self.para.gridpacklist[proc]
                except KeyError:
                    print(f'changing process name "{proc}" to dummy')
                    proc = 'dummy'
            if ispythiaonly:
                try:
                    stupidtest = self.para.pythialist[news]
                except KeyError:
                    print('changing proc pythia:', news, '  to dummy')
                    news = 'dummy'

            nfiles_eos = 0
            if self.is_lhe:
                process_eos_dir = os.path.join(self.para.lhe_dir, proc)
            else:
                process_eos_dir = os.path.join(self.para.delphes_dir,
                                               self.version,
                                               self.detector,
                                               process_name)

                if not os.path.isdir(process_eos_dir):
                    print('WARNING: Process EOS directory not found!')
                    print(f'           - {process_eos_dir}')
                    continue

                print('INFO: Process EOS directory:')
                print(f'        - {process_eos_dir}')
                sample_files = os.listdir(process_eos_dir)
                # Remove files not ending with .stdhep.gz or .root
                sample_files = \
                    [f for f in sample_files
                     if (f.endswith('.stdhep.gz') or
                         f.endswith('.root') or
                         f.endswith('.lhe.gz'))]
                # Remove not files
                sample_files = \
                    [f for f in sample_files
                     if os.path.isfile(os.path.join(process_eos_dir, f))]
                # Count number of files
                nfiles_eos = len(sample_files)

            print(f'INFO: n-events             {events_tot}')
            print(f'      sum of weights       {sumw_tot}')
            print(f'      nfiles on eos/good   {nfiles_eos}/{nfiles_good}')
            print(f'      proc in the end      {proc}')
            print(f'      news in the end      {news}')

            marked_b = ''
            marked_e = ''
            if nfiles_eos > nfiles_good + nfiles_bad:
                marked_b = '<h2><mark>'
                marked_e = '</mark></h2>'

            cmd = ''
            process_info = {}
            if not self.matching and not ispythiaonly:
                cmd = '%s,,%s,,%s%i%s,,%i,,%s%i%s,,%.2f,,%s,,%s,,%s,,%s,,%s\n' % \
                      (process_name,
                       self.comma_me(str(events_tot)),
                       marked_b,
                       nfiles_good,
                       marked_e,
                       nfiles_bad,
                       marked_b,
                       nfiles_eos,
                       marked_e,
                       size_tot / 1e9,
                       tmpf['merge']['outdir'],
                       self.para.gridpacklist[proc][0],
                       self.para.gridpacklist[proc][1],
                       self.para.gridpacklist[proc][2],
                       self.para.gridpacklist[proc][3])
                process_info = {
                    'process-name': process_name,
                    'n-events': events_tot,
                    'n-files-good': nfiles_good,
                    'n-files-bad': nfiles_bad,
                    'n-files-eos': nfiles_eos,
                    'size': tmpf['merge']['size'],
                    'path': tmpf['merge']['outdir'],
                    'files': tmpf['merge']['outfiles'],
                    'description': self.para.gridpacklist[proc][0],
                    'comment': self.para.gridpacklist[proc][1],
                    'matching-params': self.para.gridpacklist[proc][2],
                    'cross-section': self.para.gridpacklist[proc][3]
                }
                if proc == 'dummy':
                    process_info['status'] = 'not-registered'
                else:
                    process_info['status'] = 'done'
            elif self.matching and not ispythiaonly:
                cmd = '%s,,%s,,%s,,%s%i%s,,%i,,%s%i%s,,%.2f,,%s,,%s,,%s,,%s,,%s,,%s\n' % \
                      (process_name,
                       self.comma_me(str(events_tot)),
                       self.comma_me(str(sumw_tot)),
                       marked_b,
                       nfiles_good,
                       marked_e,
                       nfiles_bad,
                       marked_b,
                       nfiles_eos,
                       marked_e,
                       size_tot / 1e9,
                       tmpf['merge']['outdir'],
                       self.para.gridpacklist[proc][0],
                       self.para.gridpacklist[proc][1],
                       str(float(self.para.gridpacklist[proc][3]) * br),
                       self.para.gridpacklist[proc][4],
                       self.para.gridpacklist[proc][5])
                process_info = {
                    'process-name': process_name,
                    'n-events': events_tot,
                    'sum-of-weights': sumw_tot,
                    'n-files-good': nfiles_good,
                    'n-files-bad': nfiles_bad,
                    'n-files-eos': nfiles_eos,
                    'size': tmpf['merge']['size'],
                    'path': tmpf['merge']['outdir'],
                    'files': tmpf['merge']['outfiles'],
                    'description': self.para.gridpacklist[proc][0],
                    'comment': self.para.gridpacklist[proc][1],
                    'cross-section': float(self.para.gridpacklist[proc][3]) * br,
                    'k-factor': self.para.gridpacklist[proc][4],
                    'matching-eff': self.para.gridpacklist[proc][5]
                }
                if proc == 'dummy':
                    process_info['status'] = 'not-registered'
                else:
                    process_info['status'] = 'done'
            elif ispythiaonly:
                cmd = '%s ,,%s,,%s,,%s%i%s,,%i,,%s%i%s,,%.2f,,%s,,%s,,%s,,%s,,%s,,%s\n' % \
                      (process_name,
                       self.comma_me(str(events_tot)),
                       self.comma_me(str(sumw_tot)),
                       marked_b,
                       nfiles_good,
                       marked_e,
                       nfiles_bad,
                       marked_b,
                       nfiles_eos,
                       marked_e,
                       size_tot / 1e9,
                       tmpf['merge']['outdir'],
                       self.para.pythialist[news][0],
                       self.para.pythialist[news][1],
                       self.para.pythialist[news][3],
                       self.para.pythialist[news][4],
                       self.para.pythialist[news][5])
                process_info = {
                    'process-name': process_name,
                    'n-events': events_tot,
                    'sum-of-weights': sumw_tot,
                    'n-files-good': nfiles_good,
                    'n-files-bad': nfiles_bad,
                    'n-files-eos': nfiles_eos,
                    'size': tmpf['merge']['size'],
                    'path': tmpf['merge']['outdir'],
                    'files': tmpf['merge']['outfiles'],
                    'description': self.para.pythialist[news][0],
                    'comment': self.para.pythialist[news][1],
                    'cross-section': self.para.pythialist[news][3],
                    'k-factor': self.para.pythialist[news][4],
                    'matching-eff': self.para.pythialist[news][5]
                }
                if news == 'dummy':
                    process_info['status'] = 'not-registered'
                else:
                    process_info['status'] = 'done'
                ispythiaonly = False
            out_text += cmd
            out_dict['processes'].append(process_info)

#     0          1            2                 3           4           5
# description/comment/matching parameters/cross section/kfactor/matching efficiency

            self.ntot_events += int(events_tot)
            self.ntot_files += int(nfiles_good)
            self.tot_size += float(size_tot)
            self.ntot_bad += float(nfiles_bad)
            self.ntot_eos += float(nfiles_eos)
            self.ntot_sumw += float(sumw_tot)
        if not self.matching:
            cmd = '%s,,%s,,%s,,%s,,%s,,%.2f,,%s,,%s\n' % \
                  ('total',
                   self.comma_me(str(self.ntot_events)),
                   self.comma_me(str(self.ntot_files)),
                   self.comma_me(str(self.ntot_bad)),
                   self.comma_me(str(self.ntot_eos)),
                   self.tot_size / 1e9,
                   '',
                   '')
            out_dict['total'] = {
                'n-events': self.ntot_events,
                'n-files-good': self.ntot_files,
                'n-files-bad': self.ntot_bad,
                'n-files-eos': self.ntot_eos,
                'size': self.tot_size
            }
        else:
            cmd = '%s,,%s,,%s,,%s,,%s,,%s,,%.2f,,%s,,%s\n' % \
                  ('total',
                   self.comma_me(str(self.ntot_events)),
                   self.comma_me(str(self.ntot_sumw)),
                   self.comma_me(str(self.ntot_files)),
                   self.comma_me(str(self.ntot_bad)),
                   self.comma_me(str(self.ntot_eos)),
                   self.tot_size / 1e9,
                   '',
                   '')
            out_dict['total'] = {
                'n-events': self.ntot_events,
                'sum-of-weights': self.ntot_sumw,
                'n-files-good': self.ntot_files,
                'n-files-bad': self.ntot_bad,
                'n-files-eos': self.ntot_eos,
                'size': self.tot_size
            }

        out_text += cmd

        print('INFO: Saving web files to:')
        print(f'        - {self.outpath_txt}')
        with open(self.outpath_txt, 'w', encoding='utf-8') as outfile:
            outfile.write(out_text)
        print(f'        - {self.outpath_json}')
        with open(self.outpath_json, 'w', encoding='utf-8') as outfile:
            json.dump(out_dict, outfile, indent=4)
