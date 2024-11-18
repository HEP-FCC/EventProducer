import os
import sys
import glob
import time
import uuid
import ROOT
import yaml
import EventProducer.common.utils as ut

ROOT.gROOT.SetBatch(True)

class CheckerYAML:
    # _________________________________________________________________________
    def __init__(self, indir, para, fext, process, yamldir):
        self.indir = indir
        self.para = para
        self.fext = fext
        self.process = process
        self.yamldir = yamldir
        self.filecounting_dir = f'/tmp/fcc_filecounting_{uuid.uuid4().hex[:14]}'
        self.count = 0

        if not os.path.isdir(self.filecounting_dir):
            os.system(f'mkdir {self.filecounting_dir}')
            print('INFO: Created temporary file counting directory:')
            print(f'        - {self.filecounting_dir}')

    # _________________________________________________________________________
    def checkFile_stdhep(self, f):

        hack = True
        # hack = False

        size = os.path.getsize(f)
        if size == 0:
            self.count += 1
            print('file size is 0, job is bad')
            return -1, False

        # Clear all STDHEP file from the temporary directory
        os.system(f'rm -f {self.filecounting_dir}/*stdhep*')

        if hack:
           cmd = 'cp /dev/null %s/%s' % (self.filecounting_dir,
                                         f.split('/')[-1])
        else:
           cmd = 'cp %s %s' % (f, self.filecounting_dir)

        outputCMD = ut.getCommandOutput(cmd)
        fcount = '%s/%s' % (self.filecounting_dir, f.split('/')[-1])
        if os.path.isfile(fcount):
            cmd = 'gunzip %s'%(fcount)
            stderr = ''
            if not hack:
                outputCMD = ut.getCommandOutput(cmd)
                stderr = outputCMD["stderr"]
            if len(stderr) > 0:
                print('can not unzip the file, try again (count %i)'%self.count)
                self.count += 1
                os.system('rm %s'%(fcount))
                return -1, False

            nevts = 100000 # temporary hack !!
            if not hack:
                if os.path.isfile('tmp.slcio'):
                    os.system('rm tmp.slcio')
                cmd='stdhepjob %s tmp.slcio 1000000000 | grep \"written to LCIO\" ' %(fcount.replace('.gz',''))
                outputCMD = ut.getCommandOutput(cmd)
                if len( outputCMD["stdout"].split() ) < 2:
                    print('... problem in checkFile_stdhep with stdhepjob')
                snevts = outputCMD["stdout"].split()[1]
                nevts=int(snevts)
                os.system('rm tmp.slcio')
                if nevts==0:
                    print ('no events in the file, job is bad')
                    os.system('rm %s'%(fcount.replace('.gz','')))
                    return 0,False
                else:
                    print ('%i events in file %s, job is good'%(nevts,f))
                    os.system('rm %s'%(fcount.replace('.gz','')))
            return nevts,True
        else:
            print ('file not properly copied... try again (count %i)'%self.count)
            if not ut.testeos(self.para.eostest,self.para.eostest_size):
                print ('eos seems to have problems, should check, will exit')
                sys.exit(3)
            self.count+=1
            return -1, False

    # _________________________________________________________________________
    def checkFile_lhe(self, filepath):
        # Check file size
        size = os.path.getsize(filepath)
        if size == 0:
            self.count += 1
            print(f'File "{filepath}" is empty, job is bad!')
            return -1, False

        # Clear temporary directory from LHE files
        os.system(f'rm -f {self.filecounting_dir}/*lhe*')

        # Copy zipped LHE file to temporary directory
        cmd = 'cp %s %s' % (filepath, self.filecounting_dir)
        outputCMD = ut.getCommandOutput(cmd)

        filepath_local = '%s/%s' % (self.filecounting_dir, filepath.split('/')[-1])
        if os.path.isfile(filepath_local):
            cmd = f'gunzip {filepath_local}'
            outputCMD = ut.getCommandOutput(cmd)
            stderr = outputCMD["stderr"]
            if len(stderr) > 0:
                print('Can not unzip the file, try again (count %i)' %self.count)
                self.count += 1
                os.system('rm %s' % (filepath_local))
                return -1, False

            cmd = 'grep \"<event>\" %s | wc -l' % (filepath_local.replace('.gz', ''))
            outputCMD = ut.getCommandOutput(cmd)
            stdoutplit = outputCMD["stdout"].split(' ')
            nevts = int(stdoutplit[0])
            if nevts == 0:
                print('no events in the file, job is bad')
                os.system('rm %s' % (filepath_local.replace('.gz', '')))
                return 0, False
            print(f'{nevts} events in file "{filepath}", job is good')
            os.system('rm %s' % (filepath_local.replace('.gz', '')))
            return nevts, True
        else:
            print('file not properly copied... try again (count %i)' % self.count)
            if not ut.testeos(self.para.eostest, self.para.eostest_size):
                print('eos seems to have problems, should check, will exit')
                sys.exit(3)
            self.count += 1
            return -1, False

    # _________________________________________________________________________
    def checkFile_root(self, infile_path, ttree_name):
        try:
            tf = ROOT.TFile.Open(infile_path, 'READ')
        except IOError as err:
            print("I/O error({0}): {1}".format(err.errno, err.strerror))
            print('file ===%s=== must be deleted' % infile_path)
            return -1, -1, False
        except ValueError:
            print("Could not read the file")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print('file ===%s=== must be deleted' % infile_path)
            # os.system('rm %s'%f)
            return -1, -1, False

        tt = None
        try:
            tt = tf.Get(ttree_name)
            if tt is None:
                print('file ===%s=== must be deleted' % infile_path)
                # os.system('rm %s'%f)
                return -1, -1, False
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            print('file ===%s=== must be deleted' % infile)
            return -1, -1, False
        except ValueError:
            print ("Could read the file")
        except OSError:  # for root 6.24
            print('file ===%s=== must be deleted' % infile_path)
            # os.system('rm %s'%f)
            return -1, -1, False
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print('file ===%s=== must be deleted' % infile_path)
        # os.system('rm %s'%f)
            return -1, -1, False

        if not ut.isValidROOTfile(infile_path):
            return -1, -1, False

        nentries = tt.GetEntries()
        weight_sum = float(nentries)

        if nentries == 0:
            print('WARNING: Input ROOT file has 0 entries!')
            print('         File must be deleted...')
            return 0, 0, False

        # Weights are recent addition to DelphesEdm4hep converted
        # files -> use a flag to ensure backwards compatibility
        if hasattr(self.para, "do_weighted"):
            do_weighted = self.para.do_weighted
        else:
            do_weighted = False

        if not do_weighted:
            return int(nentries), weight_sum, True

        # Compute sum of weights
        if not tt.GetBranch("EventHeader.weight"):
            print("WARNING: EventHeader.weight is missing or corrupted!")
            print('         File must be deleted...')
            return -1, -1, False

        hist_name = infile_path.split('/')
        hist_name = hist_name[-2] + '_' + hist_name[-1].replace('.root', '')
        try:
            tt.Draw(f'EventHeader.weight[0]>>{hist_name}')
        except:
            print("WARNING: EventHeader.weight is missing or corrupted!")
            print('         Ignoring the file...')
            return -1, -1, False

        histo = ROOT.gDirectory.Get(f'{hist_name}')

        try:
            weight_sum = float(nentries) * histo.GetMean()
        except AttributeError as e:
            print("error ", e)
            if nentries != 100000 and nentries != 10000:
                print('WARNING: File with irregular number of entries:',
                      nentries)

        return int(nentries), weight_sum, True

    # _________________________________________________________________________
    def check(self, force, statfile):
        ldir = next(os.walk(self.indir))[1]

        if not ut.testeos(self.para.eostest, self.para.eostest_size):
            print('ERROR: EOS seems to have problems!')
            print('       Aborting...')
            sys.exit(3)

        for l in ldir:
            if self.process != '' and self.process != l:
                continue
            # continue if process has been checked
            if l == 'BADPYTHIA' or l == 'lhe' or l=="__restored_files__" or l=="backup":
                continue

            process = l
            print('--------------------- ', process)

            checkfile_path = os.path.join(self.yamldir, l, 'check')
            if not ut.file_exist(checkfile_path) and not force:
                print('INFO: Sample already checked.')
                print('      Continuing...')
                continue

            search_pattern = os.path.join(self.indir, process, f'events_*{self.fext}')
            print('INFO: Searching for sample input files with pattern:')
            print(f'        - {search_pattern}')
            all_files = glob.glob(search_pattern)
            print('INFO: Number of files: ', len(all_files))
            if len(all_files) < 1:
                print('WARNING: No files found!')
                print('         Continuing...')
                continue

            # Create YAML output directory
            outdir = os.path.join(self.yamldir, process)
            if not ut.dir_exist(outdir):
                os.system(f'mkdir -p {outdir}')
            hasbeenchecked = False
            nevents_tot = 0
            sumweights_tot = 0
            njobsdone_tot = 0
            njobsbad_tot = 0
            userjobs = []
            for idx, infile in enumerate(all_files):
                self.count = 0
                if not os.path.isfile(infile):
                    print('WARNING: File does not exists!')
                    print(f'           - {infile}')
                    print('         Continuing...')
                    continue

                jobid = infile.split('_')[-1]
                jobid = jobid.replace(self.fext, '')
                userid = ut.find_owner(infile)

                # Check if YAML output file is not empty
                outfile = os.path.join(outdir, f'events_{jobid}.yaml')
                if ut.getsize(outfile) == 0:
                    print('WARNING: Size of output YAML file is 0!')
                    print(f'           - {outfile}')
                    print('         Removing it...')
                    os.system(f'rm -f {outfile}')

                if ut.file_exist(outfile) and ut.getsize(outfile) > 100 and not force:
                    doc = None
                    with open(outfile, 'r', encoding='utf-8') as ftmp:
                        try:
                            doc = yaml.load(ftmp, Loader=yaml.FullLoader)
                        except yaml.YAMLError as exc:
                            print(exc)
                        except IOError as exc:
                            print("I/O error({0}): {1}".format(exc.errno, exc.strerror))
                            print("outfile ",outfile)
                        try:
                            if doc != None:
                                value = doc['processing']['status']
                            if value == 'DONE':
                                # print('INFO: Output file already exists and is valid.')
                                # print(f'        -  {outfile}')
                                continue
                        except KeyError as e:
                            print('status %s does not exist' % str(e))

                hasbeenchecked = True
                print(f'----------- {idx+1} / {len(all_files)}')
                print('INFO: Input file:')
                print(f'        - {infile}')

                if '.root' in self.fext:
                    nevts, sumw, check = self.checkFile_root(infile, self.para.treename)
                    status = 'DONE'
                    if not check:
                        status = 'BAD'

                    print(f'INFO: File status: {status}')
                    print(f'      Number of events: {nevts}')
                    print(f'      Sum of weights: {sumw:g}')

                    if status == 'DONE':
                        nevents_tot += nevts
                        sumweights_tot += sumw
                        njobsdone_tot += 1
                        if userid not in userjobs:
                            userjobs.append(userid)
                    else:
                        njobsbad_tot += 1

                    dic = {'processing': {
                             'process': process,
                             'jobid': jobid,
                             'nevents': nevts,
                             'sumofweights': sumw,
                             'status': status,
                             'out': infile,
                             'size': os.path.getsize(infile),
                             'user': userid
                             }}
                    try:
                        with open(outfile, 'w', encoding='utf-8') as outyaml:
                            yaml.dump(dic, outyaml, default_flow_style=False)
                        continue
                    except IOError as exc:
                        print("I/O error({0}): {1}".format(exc.errno, exc.strerror))
                        print("outfile ", outfile)
                        time.sleep(10)
                        with open(outfile, 'w', encoding='utf-8') as outyaml:
                            yaml.dump(dic, outyaml, default_flow_style=False)
                        continue

                elif '.lhe.gz' in self.fext:
                    nevts, check = self.checkFile_lhe(infile)
                    while nevts == -1 and not check:
                        nevts, check = self.checkFile_lhe(infile)
                        if self.count == 10:
                            print('can not copy or unzip the file, declare it wrong')
                            break

                    status = 'DONE'
                    if not check:
                        status = 'BAD'

                    if status == 'DONE':
                        nevents_tot += nevts
                        njobsdone_tot += 1
                    else:
                        njobsbad_tot += 1

                    dic = {'processing': {
                             'process': process,
                             'jobid': jobid,
                             'nevents': nevts,
                             'status': status,
                             'out': infile,
                             'size': os.path.getsize(infile),
                             'user': userid}}
                    with open(outfile, 'w', encoding='utf-8') as outyaml:
                        yaml.dump(dic, outyaml, default_flow_style=False)
                    continue

                elif '.stdhep.gz' in self.fext:
                    nevts, check = self.checkFile_stdhep(infile)
                    while nevts == -1 and not check:
                        nevts, check = self.checkFile_lhe(infile)
                        if self.count == 10:
                            print('can not copy or unzip the file, declare it wrong')
                            break

                    status = 'DONE'
                    if not check:
                        status = 'BAD'

                    if status == 'DONE':
                        nevents_tot += nevts
                        njobsdone_tot += 1
                    else:
                        njobsbad_tot += 1

                    dic = {'processing': {
                             'process': process,
                             'jobid': jobid,
                             'nevents': nevts,
                             'status': status,
                             'out': infile,
                             'size': os.path.getsize(infile),
                             'user': userid}}
                    with open(outfile, 'w', encoding='utf-8') as outyaml:
                        yaml.dump(dic, outyaml, default_flow_style=False)
                    continue

                else:
                    print('WARNING: Found file with unknown extension!')
                    print('         Continuing...')

            if hasbeenchecked:
                userstmp = ''
                for u in userjobs:
                    if userstmp == '':
                        userstmp = u
                    else:
                        userstmp += ',' + u

                cmdp = f'<tr><td>{ut.getdate_str()}</td>'
                cmdp += f'<td>{ut.gettime_str()}</td>'
                cmdp += f'<td>{njobsdone_tot}</td>'
                cmdp += f'<td>{nevents_tot}</td>'
                cmdp += f'<td>{sumweights_tot}</td>'
                cmdp += f'<td>{njobsbad_tot}</td>'
                cmdp += f'<td>{process}</td>'
                cmdp += f'<td>{userstmp}</td></tr>\n'
                stat_exist = ut.file_exist(statfile)
                with open(statfile, 'a', encoding='utf-8') as myfile:
                    if not stat_exist:
                        table_header = '<tr><th>Date</th>'
                        table_header += '<th>Time</th>'
                        table_header += '<th>Njobs</th>'
                        table_header += '<th>Nevents</th>'
                        table_header += '<th>sumofweights</th>'
                        table_header += '<th>njobbad</th>'
                        table_header += '<th>process</th>'
                        table_header += '<th>users</th></tr>\n'
                        myfile.write(table_header)

                    myfile.write(cmdp)

                print ('date=%s  time=%s  njobs=%i  nevents=%i  sumofweights=%f  njobbad=%i  process=%s users=%s'%(ut.getdate_str(),ut.gettime_str() ,njobsdone_tot,nevents_tot,sumweights_tot, njobsbad_tot,process,userstmp))
