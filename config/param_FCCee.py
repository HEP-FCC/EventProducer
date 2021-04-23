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
fcc_versions=['fcc_v01','fcc_v02','fcc_v03','fcc_tmp','fcc_tmp_v02','fcc_tmp_v03','fcc_tmp_training']

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
# /cvmfs/fcc.cern.ch/sw/latest/setup.sh 
##delphes base card
delphescard_base='card.tcl'
##FCC config script name
fccconfig='PythiaDelphes_config_v02.py'

##base dir of FCCSW
##fccsw_dir='/cvmfs/fcc.cern.ch/sw/0.8.2/'
#fccsw_dir='/cvmfs/fcc.cern.ch/sw/views/releases/externals/94.2.0/x86_64-centos7-gcc62-opt/'
##init script for FCCSW
#stack=fccsw_dir+'init_fcc_stack.sh'
#stack=fccsw_dir+'setup.sh'
#stack='/cvmfs/fcc.cern.ch/sw/views/releases/externals/94.3.0/x86_64-centos7-gcc62-opt/setup.sh'
stack='/cvmfs/fcc.cern.ch/sw/latest/setup.sh'
stack='/cvmfs/sw.hsf.org/spackages/setup_bash-20200930.sh'
#hack EDM4Hep donal
stack='/cvmfs/fcc.cern.ch/sw/latest/setup.sh'

##FCCSW dir
#fccsw=fccsw_dir+'fccsw/0.8.2/x86_64-slc6-gcc62-opt/'
fccsw='/afs/cern.ch/work/v/vavolkl/public/fcc.cern.ch/sw/fccsw/v0.10/x86_64-centos7-gcc62-opt/'
fccsw='/afs/cern.ch/user/h/helsens/FCCsoft/FCCSW/'
fccsw='/cvmfs/sw.hsf.org/spackages/linux-centos7-broadwell/gcc-8.3.0/fccsw-0.13-l3w7dyet52qlriu74jtk5l66kap6ggmn/scripts/'
fccsw='/cvmfs/sw.hsf.org/spackages/linux-centos7-broadwell/gcc-8.3.0/fccsw-develop-q57ahua7lm65fvxnzekozih4mgvzptlx/scripts/'
fccsw=''


#list of processes only with Pythia, meaning no LHE
pythialist={
    'dummy':['','','','','',''],
    'p8_ee_ZH_ecm240':['ZH ecm=240GeV','inclusive decays','','0.201037','1.0','1.0'],
    'p8_ee_ZZ_ecm240':['ZZ ecm=240GeV','inclusive decays','','1.35899','1.0','1.0'],
    'p8_ee_WW_ecm240':['WW ecm=240GeV','inclusive decays','','16.4385','1.0','1.0'],
    'p8_ee_Zqq_ecm240':['Z/Gamma* ecm=240GeV','hadronic decays','','53.188','1.0','1.0'],

    'p8_ee_ZH_ecm365':['ZH ecm=365GeV','inclusive decays','','0.1173','1.0','1.0'],
    'p8_ee_ZZ_ecm365':['ZZ ecm=365GeV','inclusive decays','','0.6428','1.0','1.0'],
    'p8_ee_WW_ecm365':['WW ecm=365GeV','inclusive decays','','10.7165','1.0','1.0'],
    'p8_ee_tt_ecm365':['tt ecm=365GeV','inclusive decays','','0.800','1.0','1.0'],

    'p8_ee_tt_fullhad_ecm365':['tt ecm=365GeV','hadronic decays','','0.363528','1.0','1.0'],
    'p8_ee_ZZ_fullhad_ecm365':['ZZ ecm=365GeV','hadronic decays','','0.31417','1.0','1.0'],
    'p8_ee_WW_fullhad_ecm365':['WW ecm=365GeV','hadronic decays','','4.86969','1.0','1.0'],

    'p8_ee_H_Hbb_ecm125':['H ecm=125GeV','Higgs to bb','','0.000164','1.0','1.0'],
    'p8_ee_H_Hgg_ecm125':['H ecm=125GeV','Higgs to gluon','','0.000023','1.0','1.0'],
    'p8_ee_H_Hcc_ecm125':['H ecm=125GeV','Higgs to cc','','0.000008','1.0','1.0'],
    'p8_ee_H_Htautau_ecm125':['H ecm=125GeV','Higgs to tau','','0.0000065','1.0','1.0'],

    
    'p8_ee_Z_Zbb_ecm125':['bb ecm=125GeV','bb','','81.','1.0','1.0'],
    'p8_ee_Z_Zcc_ecm125':['cc ecm=125GeV','cc','','73.','1.0','1.0'],
    'p8_ee_Z_Zqq_ecm125':['qq ecm=125GeV','qq','','237.','1.0','1.0'],
    'p8_ee_Z_Ztautau_ecm125':['tautau ecm=125GeV','tautau','','26.','1.0','1.0'],
    'p8_ee_ZZ_ecm125':['ZZ ecm=125GeV','inclusive','','1.','0.','1.0'],
    'p8_ee_WW_ecm125':['WW ecm=125GeV','inclusive','','0.0558','1.0','1.0'],

#ok, so once you have Z -> bb
#you need a factor of 7.9e-5 for Bc production
#then a factor 0.0236 for Bc -> tau nu BF
#then 0.098 for tau -> 3π nu


    
    'p8_ee_Zbb_ecm91':['Z/Gamma* ecm=91.188GeV to bb','inclusive decays','','6645.46','1.0','1.0'],
    'p8_ee_Zcc_ecm91':['Z/Gamma* ecm=91.188GeV to cc','inclusive decays','','5215.46','1.0','1.0'],
    'p8_ee_Zuds_ecm91':['Z/Gamma* ecm=91.188GeV to uds','inclusive decays','','18616.5','1.0','1.0'],
    'p8_ee_Ztautau_ecm91':['Z/Gamma* ecm=91.188GeV to tautau','inclusive decays','','1476.58','1.0','1.0'],    

    'p8_ee_Zbb_ecm91_EvtGen_Bu2D0Pi':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+/- -> D0(KPi)Pi','','1.3290920','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstTauTau':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) tau+ tau-, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstTauTauTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) tau+ tau-, tau -> 3pi nu TAUHADNU model','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2D0PiPi':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> D0 p+ p-','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2MuMu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> mu mu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstTauNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (D*- -> (D0b -> K+ pi-) pi-) tau+ nu, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstTauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (D*- -> (D0b -> K+ pi-) pi-) tau+ nu, tau -> 3pi nu TAUHADNU model','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DTauNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (D- -> K+ pi- pi-) tau+ nu, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DTauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (D- -> K+ pi- pi-) tau+ nu, tau -> 3pi nu TAUHADNU model','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstEE':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) e+ e-','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_BdKstNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) nu nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KsPi0':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (Ks0 -> pi pi) pi0','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2PhiGamma':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs0 -> (phi -> K+ K-) gamma','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2TauTau':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs0 -> tau+ tau-, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2TauTauTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs0 -> tau+ tau-, tau -> 3pi nu TAUHADNU model','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bc2TauNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> tau+ nu, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bc2TauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> tau+ nu, tau -> 3pi nu TAUHADNU model','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsK':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs+ -> D*K','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2TauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+ -> tau+ nu, tau -> 3pi nu TAUHADNU model','','0.05799621863924','1.0','1.0'],#6645.46*2*0.43*0.000109*0.0931


    
    'p8_ee_Ztautau_ecm91_EvtGen_Tau2MuMuMu':['Z/Gamma* ecm=91.188GeV to tautau','EvtGen tau -> 3mu','','1.0','1.0','1.0'],    
    'p8_ee_Ztautau_ecm91_EvtGen_Tau2MuGamma':['Z/Gamma* ecm=91.188GeV to tautau','EvtGen tau -> mu gamma','','1.0','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_D2PiPi0':['Z/Gamma* ecm=91.188GeV to cc','EvtGen D+ -> pi+ pi0','','1.0','1.0','1.0'],
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
    'mg_ee_tt_ecm350':['tt','tt inclusive','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tH_ecm365':['tt','tt inclusive','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tcz_ecm365':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tua_ecm240':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tua_ecm365':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tuz_ecm240':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tuz_ecm365':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tca_ecm240':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tca_ecm365':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tcz_ecm240':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tca_ecm365':['ttbar FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tua_ecm365':['ttbar FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tuz_ecm365':['ttbar FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tcz_ecm365':['ttbar FCNC','to be added','','1.0','1.0','1.0'],

}

