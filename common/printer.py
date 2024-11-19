'''
Prints sample metadata to a text file.
'''

import sys
import os.path
import re
import time
import yaml


class Printer:
    '''
    Prints sample metadata to a text file.
    '''
    def __init__(self, yamldir, outpath, matching, is_lhe, para,
                 detector='', version=''):
        self.yamldir = yamldir
        self.outpath = outpath
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
        for process_name in process_names:
            print(f'--------------------------  {process_name}')

            mergefile_path = os.path.join(self.yamldir, process_name,
                                          'merge.yaml')

            if not os.path.isfile(mergefile_path):
                print(f'WARNING: Ignoring process "{process_name}" --- '
                      'not merged yet.')
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
            size_tot = tmpf['merge']['size'] / 1000000000.
            bad_tot = tmpf['merge']['nbad']
            files_tot = tmpf['merge']['ndone']
            # Sum of weights is identical to number of events
            # TODO: introduce loading of sum of weights
            sumw_tot = float(tmpf['merge']['nevents'])

            # Adjust process name
            process_name_short = process_name.replace('mgp8_', 'mg_')
            process_name_short = process_name_short.replace('kkmcp8_', 'kkmc_')
            print(f'INFO: Shortening sample name to "{process_name_short}"')
            news = str(process_name_short)
            proc = str(process_name_short)

            br = 1
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
                sample_eos_dir = os.path.join(self.para.lhe_dir, proc)
            else:
                sample_eos_dir = os.path.join(self.para.delphes_dir,
                                              self.version,
                                              self.detector,
                                              process_name)

                if not os.path.isdir(sample_eos_dir):
                    print('WARNING: Sample EOS directory not found!')
                    print(f'           - {sample_eos_dir}')
                    continue

                print('INFO: Sample EOS directory:')
                print(f'        - {sample_eos_dir}')
                sample_files = os.listdir(sample_eos_dir)
                # Remove files not ending with .stdhep.gz or .root
                sample_files = \
                    [f for f in sample_files
                     if (f.endswith('.stdhep.gz') or
                         f.endswith('.root') or
                         f.endswith('.lhe.gz'))]
                # Remove not files
                sample_files = \
                    [f for f in sample_files
                     if os.path.isfile(os.path.join(sample_eos_dir, f))]
                # Count number of files
                nfiles_eos = len(sample_files)

            print('nevents              : %i' % events_tot)
            print('nfiles on eos/checked: %i/%i' % (nfiles_eos, files_tot))
            print('proc in the end      : ', proc)
            print('news in the end      : ', news)

            marked_b = ''
            marked_e = ''
            if nfiles_eos > files_tot + bad_tot:
                marked_b = '<h2><mark>'
                marked_e = '</mark></h2>'

            cmd = ''
            if not self.matching and not ispythiaonly:
                cmd = '%s,,%s,,%s%i%s,,%i,,%s%i%s,,%.2f,,%s,,%s,,%s,,%s,,%s\n' % \
                      (process_name,
                       self.comma_me(str(events_tot)),
                       marked_b,
                       files_tot,
                       marked_e,
                       bad_tot,
                       marked_b,
                       nfiles_eos,
                       marked_e,
                       size_tot,
                       tmpf['merge']['outdir'],
                       self.para.gridpacklist[proc][0],
                       self.para.gridpacklist[proc][1],
                       self.para.gridpacklist[proc][2],
                       self.para.gridpacklist[proc][3])
            elif self.matching and not ispythiaonly:
                cmd = '%s,,%s,,%s,,%s%i%s,,%i,,%s%i%s,,%.2f,,%s,,%s,,%s,,%s,,%s,,%s\n' % \
                      (process_name,
                       self.comma_me(str(events_tot)),
                       self.comma_me(str(sumw_tot)),
                       marked_b,
                       files_tot,
                       marked_e,
                       bad_tot,
                       marked_b,
                       nfiles_eos,
                       marked_e,
                       size_tot,
                       tmpf['merge']['outdir'],
                       self.para.gridpacklist[proc][0],
                       self.para.gridpacklist[proc][1],
                       str(float(self.para.gridpacklist[proc][3]) * br),
                       self.para.gridpacklist[proc][4],
                       self.para.gridpacklist[proc][5])
            elif ispythiaonly:
                cmd = '%s ,,%s,,%s,,%s%i%s,,%i,,%s%i%s,,%.2f,,%s,,%s,,%s,,%s,,%s,,%s\n' % \
                      (process_name,
                       self.comma_me(str(events_tot)),
                       self.comma_me(str(sumw_tot)),
                       marked_b,
                       files_tot,
                       marked_e,
                       bad_tot,
                       marked_b,
                       nfiles_eos,
                       marked_e,
                       size_tot,
                       tmpf['merge']['outdir'],
                       self.para.pythialist[news][0],
                       self.para.pythialist[news][1],
                       self.para.pythialist[news][3],
                       self.para.pythialist[news][4],
                       self.para.pythialist[news][5])
                ispythiaonly = False
            out_text += cmd

#     0          1            2                 3           4           5
# description/comment/matching parameters/cross section/kfactor/matching efficiency

            self.ntot_events += int(events_tot)
            self.ntot_files += int(files_tot)
            self.tot_size += float(size_tot)
            self.ntot_bad += float(bad_tot)
            self.ntot_eos += float(nfiles_eos)
            self.ntot_sumw += float(sumw_tot)
        if not self.matching:
            cmd = '%s,,%s,,%s,,%s,,%s,,%.2f,,%s,,%s\n' % \
                  ('total',
                   self.comma_me(str(self.ntot_events)),
                   self.comma_me(str(self.ntot_files)),
                   self.comma_me(str(self.ntot_bad)),
                   self.comma_me(str(self.ntot_eos)),
                   self.tot_size,
                   '',
                   '')
        else:
            cmd = '%s,,%s,,%s,,%s,,%s,,%s,,%.2f,,%s,,%s\n' % \
                  ('total',
                   self.comma_me(str(self.ntot_events)),
                   self.comma_me(str(self.ntot_sumw)),
                   self.comma_me(str(self.ntot_files)),
                   self.comma_me(str(self.ntot_bad)),
                   self.comma_me(str(self.ntot_eos)),
                   self.tot_size,
                   '',
                   '')

        out_text += cmd

        print('INFO: Saving web file to:')
        print(f'        - {self.outpath}')
        with open(self.outpath, 'w', encoding='utf-8') as outfile:
            outfile.write(out_text)
