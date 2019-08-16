#module

module_name='config/param_FCCee.py'
#eos tests
eostest='/eos/experiment/fcc/hh/tests/testfile.lhe.gz'
eostest_size=1312594

#stat
lhe_stat="/afs/cern.ch/user/h/helsens/www/data/FCCee/statlhe.html"
delphes_stat="/afs/cern.ch/user/h/helsens/www/data/FCCee/statdelphesVERSION.html"

#web
lhe_web="/afs/cern.ch/user/h/helsens/www/data/FCCee/LHEevents.txt"
delphes_web="/afs/cern.ch/user/h/helsens/www/data/FCCee/Delphesevents_VERSION.txt"

#yaml directory
yamldir='/afs/cern.ch/work/h/helsens/public/FCCDicts/yaml/FCCee/'

#heppy and proc lists
heppyList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/FCCee_heppySampleList_VERSION.py'
procList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/FCCee_procDict_VERSION.json'

##eos directory for MG5@MCatNLO gridpacks
gp_dir      = '/eos/experiment/fcc/ee/generation/gridpacks/'
##eos directory for lhe files
lhe_dir     = '/eos/experiment/fcc/ee/generation/lhe/'
##extension
lhe_ext     ='.lhe.gz'

##FCC versions
fcc_versions=['fcc_v01']

##eos directory for FCCSW pythia delphes files
delphes_dir = '/eos/experiment/fcc/ee/generation/DelphesEvents/'
##extension
delphes_ext='.root'
##name of the ttree
treename='events'

##where the delphes cards are stored
delphescards_dir = '/eos/experiment/fcc/ee/utils/delphescards/'
##where the pythia cards are stored
pythiacards_dir  = '/eos/experiment/fcc/ee/utils/pythiacards/'
##where the FCC config script is stored
fccconfig_dir    = '/eos/experiment/fcc/ee/utils/config/'

##delphes base card
delphescard_base='card.tcl'
##FCC config script name
fccconfig='PythiaDelphes_config_v01.py'

##base dir of FCCSW
##fccsw_dir='/cvmfs/fcc.cern.ch/sw/0.8.2/'
fccsw_dir='/cvmfs/fcc.cern.ch/sw/views/releases/externals/94.2.0/x86_64-centos7-gcc62-opt/'
##init script for FCCSW
#stack=fccsw_dir+'init_fcc_stack.sh'
stack=fccsw_dir+'setup.sh'
##FCCSW dir
#fccsw=fccsw_dir+'fccsw/0.8.2/x86_64-slc6-gcc62-opt/'
fccsw='/afs/cern.ch/work/v/vavolkl/public/fcc.cern.ch/sw/fccsw/v0.10/x86_64-centos7-gcc62-opt/'

#list of processes only with Pythia, meaning no LHE
pythialist={
'dummy':['','','','','',''],
'p8_ee_ZH_ecm240':['ZH ecm=240GeV','inclusive decays','','0.201037','1.0','1.0'],
'p8_ee_ZZ_ecm240':['ZZ ecm=240GeV','inclusive decays','','1.35899','1.0','1.0'],
'p8_ee_WW_ecm240':['WW ecm=240GeV','inclusive decays','','16.4385','1.0','1.0']
}



##list of possible decays of LHE files
decaylist = {
}

##list of decays branching ratios 
# from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR 
# and Particle data Group
branching_ratios = {
'hmumu':2.176E-04,
'haa':2.270E-03,
'hlla':1.533E-03*(3.363E-02 + 3.366E-02),
'hllll':1.240E-04,
'hlvlv':1.055E-02,
'hbb':5.824E-01,
'htautau':6.272E-02,
'zll':0.307,
'ztautau':0.03367,
'zbb':0.152,
'wlv':3*0.108,
'hhaabb':2*2.270E-03*5.824E-01,
'hhbbbb':5.824E-01*5.824E-01,
'znunu':0.205,
'wzlllv':0.03333,


}


##Gridpack list
##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency

gridpacklist = {
'dummy':['','','','','',''],
}

