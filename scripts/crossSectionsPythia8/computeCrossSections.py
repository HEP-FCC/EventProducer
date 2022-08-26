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
   print '====================  ',line
   # copy cmd file locally

   cmd = 'cp %s .'%line
   print 'cmd ',cmd
   os.system(cmd)
   loc_fname = os.path.basename(line)
   print 'loc_fname  ',loc_fname
   
   # append new params
   with open(loc_fname, 'a') as f:
        f.write(parpy8)

   # now run py8 code
   print 'loc_fname  ',loc_fname
   print 'param      ',param
   cmd ='./py8crossSection.exe %s %s'%(loc_fname,  param)
   os.system(cmd)

   # now erase py8 cmd file
   cmd ='rm %s'%loc_fname
   os.system(cmd)
