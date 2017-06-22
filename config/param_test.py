#dicts
##LHE dictionnary
lhe_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict_MYTEST.json'
##FCC events dictionnary
fcc_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_fcc_v01_MYTEST.json'

##LHE read file true/false
readlhe_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/readLHE_MYTEST.json'
##FCC read file true/false
readfcc_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/readFCC_MYTEST.json'

##eos directory for MG5@MCatNLO gridpacks
gp_dir      = '/eos/experiment/fcc/hh/generation/mg5_amcatnlo/gridpacks_MYTEST/'
##eos directory for lhe files
lhe_dir     = '/eos/experiment/fcc/hh/generation/mg5_amcatnlo/lhe_MYTEST/'

##eos directory for FCCSW pythia delphes files
delphes_dir = '/eos/experiment/fcc/hh/generation/DelphesEvents/MYTEST/'

##where the delphes cards are stored
delphescards_dir = '/eos/experiment/fcc/hh/delphescards/'
##where the pythia cards are stored
pythiacards_dir  = '/eos/experiment/fcc/hh/pythiacards/'
##where the FCC config script is stored
fccconfig_dir    = '/eos/experiment/fcc/hh/config/'

##muom momentum delphes resolution card
delphescard_mmr='muonMomentumResolutionVsP.tcl'
##momentum resolution delphes card
delphescard_mr='momentumResolutionVsP.tcl'
##delphes base card
delphescard_base='card.tcl'
##FCC config script name
fccconfig='PythiaDelphes_config.py'

##base dir of FCCSW
fccsw_dir='/cvmfs/fcc.cern.ch/sw/0.8.1/'
##init script for FCCSW
stack=fccsw_dir+'init_fcc_stack.sh'
##FCCSW dir
fccsw=fccsw_dir+'fccsw/0.8.1/x86_64-slc6-gcc49-opt/'

#list of processes only with Pythia, meaning no LHE
pythialist={
# keep a simple example
'pp_Zprime_5TeV_ll':['5TeV Z\' -> ll (l=e,mu,tau)','','','4.751e-4','1.0','1.0'],
}

##list of possible decays of LHE files
decaylist = {
# keep a simple example
'pp_h012j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
}

##list of decays branching ratios 
# from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR 
# and Particle data Group

branching_ratios = {
# keep a simple example
'hmumu':2.176E-04,
}

##Gridpack list
##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency

gridpacklist = {
# keep a simple example
'pp_h012j_5f':['gluon fusion higgs (finite mt) + 0/1/2 jets','inclusive','xqcut = 30, qCut = 45','587.5','3.76','0.364'],

}
