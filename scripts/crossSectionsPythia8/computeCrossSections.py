import os, sys

inputList = sys.argv[1]

# params to be appended to regular cards

parpy8="""

! switch off all things that slow down p8
Random:setSeed = off
Main:numberOfEvents = 10000 

PartonLevel:all = off
HadronLevel:all = off
Print:quiet = off 
"""

param = 'param.txt'


with open(inputList) as f:
   lines = [line.rstrip('\n') for line in f]

for line in lines:

   # copy cmd file locally
   cmd = 'cp {} .'.format(line)
   os.system(cmd)
   loc_fname = os.path.basename(line)
   print loc_fname
   
   # append new params
   with open(loc_fname, 'a') as f:
        f.write(parpy8)

   # now run py8 code
   cmd ='./py8crossSection.exe {} {}'.format(loc_fname,  param)
   os.system(cmd)

   # now erase py8 cmd file
   cmd ='rm {}'.format(loc_fname)
   os.system(cmd)
