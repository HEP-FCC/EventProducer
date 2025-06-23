import gzip
import glob

total = 0
filelist = glob.glob('/eos/home-o/oarakji/tth/lhe/mg_pp_tth_5f_50TeV/events_*.lhe.gz')

for fname in filelist:
    with gzip.open(fname, 'rt') as f:
        for line in f:
            if '<event>' in line:
                total += 1

print(f'Total number of events: {total}')