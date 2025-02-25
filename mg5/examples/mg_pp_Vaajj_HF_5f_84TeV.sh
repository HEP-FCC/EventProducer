import model sm-no_b_mass

define l+ = e+ mu+ ta+ 
define vl = ve vm vt
define l- = e- mu- ta- 
define vl~ = ve~ vm~ vt~

generate p p > l+ vl a a b  b~ 
add process p p > l- vl~ a a b b~ 
add process p p > l- l+ a a b b~ 

add process p p > l+ vl a a c  c~ 
add process p p > l- vl~ a a c c~ 
add process p p > l- l+ a a c c~ 

output DUMMYPROCESS

######## DELIMITER (!!! NEED THIS LINE !!!) ##################

set lhapdf /afs/cern.ch/work/b/bistapf/lhapdf/LHAPDF-6.1.6/install/bin/lhapdf-config

launch DUMMYPROCESS
set iseed DUMMYSEED
set nevents DUMMYNEVENTS

set ebeam1 42000
set ebeam2 42000

set pdlabel lhapdf
set lhaid 260000

set ickkw 0

set bwcutoff 50.0

set mmaa 105.0
set mmaamax 145.0

set ptj 5.0
set ptb 5.0
set pta 5.0
set ptl 5.0

set etaj 8.0
set etab 8.0
set etaa 8.0
set etal 8.0

set drbb 0.001 
set drll 0.001 
set draa 0.001 
set drbj 0.001 
set drbl 0.001  
set draj 0.3
set dral 0.3 

set maxjetflavor 5

set use_syst False