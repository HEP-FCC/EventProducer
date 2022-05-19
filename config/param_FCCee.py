#module
module_name='config/param_FCCee.py'
#eos tests
eostest='/eos/experiment/fcc/hh/tests/testfile.lhe.gz'
eostest_size=1312594

#stat
lhe_stat     = "/afs/cern.ch/user/h/helsens/www/data/FCCee/statlhe.html"
delphes_stat = "/afs/cern.ch/user/h/helsens/www/data/FCCee/statdelphesVERSION_DETECTOR.html"
stdhep_stat  = "/afs/cern.ch/user/h/helsens/www/data/FCCee/statstdhep.html"


#web
lhe_web      = "/afs/cern.ch/user/h/helsens/www/data/FCCee/LHEevents.txt"
delphes_web  = "/afs/cern.ch/user/h/helsens/www/data/FCCee/Delphesevents_VERSION_DETECTOR.txt"
stdhep_web   = "/afs/cern.ch/user/h/helsens/www/data/FCCee/STDHEPevents.txt"

#yaml directory
yamldir      = "/afs/cern.ch/work/h/helsens/public/FCCDicts/yaml/FCCee/"


#heppy and proc lists
heppyList    = "/afs/cern.ch/work/h/helsens/public/FCCDicts/FCCee_heppySampleList_VERSION_DETECTOR.py"
procList     = "/afs/cern.ch/work/h/helsens/public/FCCDicts/FCCee_procDict_VERSION_DETECTOR.json"


##eos directory for MG5@MCatNLO gridpacks
gp_dir       = "/eos/experiment/fcc/ee/generation/gridpacks/"
##eos directory for lhe files
lhe_dir      = "/eos/experiment/fcc/ee/generation/lhe/"
##extension
lhe_ext      = ".lhe.gz"
##eos directory for stdhep files
stdhep_dir   = "/eos/experiment/fcc/ee/generation/stdhep/"
##extension
stdhep_ext   = ".stdhep.gz"

##FCC versions
fcc_versions = ['spring2021','spring2021_training','dev' ]

##eos directory for FCCSW pythia delphes files
delphes_dir  = "/eos/experiment/fcc/ee/generation/DelphesEvents/"
##extension
delphes_ext  = ".root"
##name of the ttree
treename     = "events"


##where the delphes cards are stored
delphescards_dir = "/eos/experiment/fcc/ee/generation/FCC-config/_VERSION_/FCCee/Delphes/"
##where the pythia cards are stored
pythiacards_dir  = "/eos/experiment/fcc/ee/generation/FCC-config/_VERSION_/FCCee/Generator/Pythia8/"
##where the EVTGEN card are stored
evtgencards_dir  = "/eos/experiment/fcc/ee/generation/FCC-config/_VERSION_/FCCee/Generator/EvtGen/"
##where the WHIZARD cards are stored
whizardcards_dir = "/eos/experiment/fcc/ee/generation/FCC-config/_VERSION_/FCCee/Generator/Whizard/"
##where the KKMC cards are stored
kkmccards_dir = "/eos/experiment/fcc/ee/generation/FCC-config/_VERSION_/FCCee/Generator/KKMC/"
# /cvmfs/fcc.cern.ch/sw/latest/setup.sh 
##delphes base card detector
detectors = ['IDEA', 'IDEA_3T', 'IDEA_FullSilicon']



##init script for Key4Hep
stack  = '/cvmfs/sw.hsf.org/key4hep/setup.sh'
stack  = '/cvmfs/sw.hsf.org/spackages2/key4hep-stack/2021-05-12/x86_64-centos7-gcc8.3.0-opt/iyafnfo5muwvpbxcoa4ygwoxi2smkkwa/setup.sh'
#list of processes only with Pythia, meaning no LHE
pythialist={
    'dummy':['','','','','',''],
    'p8_ee_ZH_ecm240':['ZH ecm=240GeV','inclusive decays','','0.201868','1.0','1.0'],       #    Pythia 8.303, noBES (Used 0.201037 before)
    'p8_ee_ZZ_ecm240':['ZZ ecm=240GeV','inclusive decays','','1.35899','1.0','1.0'],
    'p8_ee_WW_ecm240':['WW ecm=240GeV','inclusive decays','','16.4385','1.0','1.0'],
    'p8_ee_Zqq_ecm240':['Z/Gamma* ecm=240GeV','hadronic decays','','52.6539','1.0','1.0'],  # Pythia 8.303, noBES (was 53.188 before spring2021)
    'p8_ee_Zll_ecm240':['Z/Gamma* ecm=240GeV','leptonic decays (e/mu/tau)','','13.7787','1.0','1.0'],  # Pythia 8.303, noBES 

    'p8_ee_ZH_mH-higher-100MeV_ecm240':['ZH ecm=240GeV, vary mH','inclusive decays','','0.201316','1.0','1.0'],  	# Pythia 8.303, noBES
    'p8_ee_ZH_mH-higher-50MeV_ecm240':['ZH ecm=240GeV, vary mH','inclusive decays','','0.201673','1.0','1.0'],		# Pythia 8.303, noBES
    'p8_ee_ZH_mH-lower-50MeV_ecm240':['ZH ecm=240GeV, vary mH','inclusive decays','','0.202169','1.0','1.0'],		# Pythia 8.303, noBES
    'p8_ee_ZH_mH-lower-100MeV_ecm240':['ZH ecm=240GeV, vary mH','inclusive decays','','0.20253','1.0','1.0'],		# Pythia 8.303, noBES

    'p8_ee_ZZ_Zll_ecm240':['ZZ ecm=240GeV','Z to e, mu, tau','','0.027','1.0','1.0'], 

    'p8_ee_WW_mumu_ecm240':['WW ecm=240GeV','W->mu and W ->tau->mu','','0.25792','1.0','1.0'],
    'p8_noBES_ee_WW_mumu_ecm240':['WW ecm=240GeV','W->mu and W ->tau->mu','','0.25792','1.0','1.0'],

    'p8_noBES_ee_ZH_ecm240':['ZH ecm=240GeV, no BES','inclusive decays','','0.201037','1.0','1.0'],
    'p8_noBES_ee_ZZ_ecm240':['ZZ ecm=240GeV, no BES','inclusive decays','','1.35899','1.0','1.0'],
    'p8_noBES_ee_WW_ecm240':['WW ecm=240GeV, no BES','inclusive decays','','16.4385','1.0','1.0'],

    'p8_ee_ZH_ecm365':['ZH ecm=365GeV','inclusive decays','','0.1173','1.0','1.0'],
    'p8_ee_ZZ_ecm365':['ZZ ecm=365GeV','inclusive decays','','0.6428','1.0','1.0'],
    'p8_ee_WW_ecm365':['WW ecm=365GeV','inclusive decays','','10.7165','1.0','1.0'],
    'p8_ee_tt_ecm365':['tt ecm=365GeV','inclusive decays','','0.800','1.0','1.0'],

    'p8_ee_WW_mumu_ecm365':['WW ecm=365GeV','W->mu and W ->tau->mu','','0.1785','1.0','1.0'],
    'p8_ee_Zqq_ecm365':['Z/Gamma* ecm=365GeV','hadronic decays','','21.4149','1.0','1.0'],  

    'p8_ee_tt_fullhad_ecm365':['tt ecm=365GeV','hadronic decays','','0.363528','1.0','1.0'],
    'p8_ee_ZZ_fullhad_ecm365':['ZZ ecm=365GeV','hadronic decays','','0.31417','1.0','1.0'],
    'p8_ee_WW_fullhad_ecm365':['WW ecm=365GeV','hadronic decays','','4.86969','1.0','1.0'],

    'p8_ee_ZH2_mH2-200GeV_ecm365':['Z BSM Higgs ecm=365GeV', 'inclusive decays', '', '1.0', '1.0', '1.0'],

    'p8_ee_H_Hbb_ecm125':['H ecm=125GeV','Higgs to bb','','0.000164','1.0','1.0'],
    'p8_ee_H_Hgg_ecm125':['H ecm=125GeV','Higgs to gluon','','0.000023','1.0','1.0'],
    'p8_ee_H_Hcc_ecm125':['H ecm=125GeV','Higgs to cc','','0.000008','1.0','1.0'],
    'p8_ee_H_Htautau_ecm125':['H ecm=125GeV','Higgs to tau','','0.0000065','1.0','1.0'],
    'p8_noBES_ee_H_Hbb_ecm125':['H ecm=125GeV','Higgs to bb','','0.000164','1.0','1.0'],
    'p8_noBES_ee_H_Hgg_ecm125':['H ecm=125GeV','Higgs to gluon','','0.000023','1.0','1.0'],
    'p8_noBES_ee_H_Hcc_ecm125':['H ecm=125GeV','Higgs to cc','','0.000008','1.0','1.0'],
    'p8_noBES_ee_H_Htautau_ecm125':['H ecm=125GeV','Higgs to tau','','0.0000065','1.0','1.0'],
    
    'p8_ee_Z_Zbb_ecm125':['bb ecm=125GeV','bb','','81.','1.0','1.0'],
    'p8_ee_Z_Zcc_ecm125':['cc ecm=125GeV','cc','','73.','1.0','1.0'],
    'p8_ee_Z_Zqq_ecm125':['qq ecm=125GeV','qq','','237.','1.0','1.0'],
    'p8_ee_Z_Ztautau_ecm125':['tautau ecm=125GeV','tautau','','26.','1.0','1.0'],
    'p8_ee_ZZ_ecm125':['ZZ ecm=125GeV','inclusive','','1.','0.','1.0'],
    'p8_ee_WW_ecm125':['WW ecm=125GeV','inclusive','','0.0558','1.0','1.0'],



#once we have Z -> bb
#we need a factor of 7.9e-5 for Bc production
#then a factor 0.0236 for Bc -> tau nu BF
#then 0.098 for tau -> 3π nu

    
    'p8_ee_Zbb_ecm91':['Z/Gamma* ecm=91.188GeV to bb','inclusive decays','','6645.46','1.0','1.0'],
    'p8_ee_Zcc_ecm91':['Z/Gamma* ecm=91.188GeV to cc','inclusive decays','','5215.46','1.0','1.0'],
    'p8_ee_Zuds_ecm91':['Z/Gamma* ecm=91.188GeV to uds','inclusive decays','','18616.5','1.0','1.0'],
    'p8_ee_Ztautau_ecm91':['Z/Gamma* ecm=91.188GeV to tautau','inclusive decays','','1476.58','1.0','1.0'],    
    'p8_ee_Zee_ecm91':['Z/Gamma* ecm=91.188GeV','Z decays to ee','','1462.09','1.0','1.0'],
    'p8_ee_Zmumu_ecm91':['Z/Gamma* ecm=91.188GeV','Z decays to mumu','','1462.08','1.0','1.0'],


    'p8_ee_Zbb_ecm91_EvtGen':['Z/Gamma* ecm=91.188GeV to bb','inclusive decays using EvtGen','','6645.46','1.0','1.0'],


    'p8_ee_Zbb_ecm91_EvtGen_Bu2D0Pi':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+/- -> D0(KPi)Pi','','1.3290920','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstTauTau':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) tau+ tau-, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstTauTauTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) tau+ tau-, tau -> 3pi nu TAUHADNU model','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2D0PiPi':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> D0 p+ p-','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2MuMu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> mu mu','','3.029000668e-07','1.0','1.0'],
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
    'p8_ee_Zbb_ecm91_EvtGen_Bc2TauNuTau23PiPi0NuTAUOLA':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> tau+ nu, tau -> 3pi pi0 nu TAUOLA model','','0.01','1.0','1.0'],#0.0931 for the tau decay, it is 0.0462
    'p8_ee_Zbb_ecm91_EvtGen_Bc2MuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> mu+ nu','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931                                         
    'p8_ee_Zbb_ecm91_EvtGen_Bc2TauNuTau2MuNuNuPHOTOSTAULNUNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> tau+ nu, tau -> mu nu nu','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931   
    'p8_ee_Zbb_ecm91_EvtGen_Bu2MuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+ -> mu+ nu','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931                                         
    'p8_ee_Zbb_ecm91_EvtGen_Bu2TauNuTau2MuNuNuPHOTOSTAULNUNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+ -> tau+ nu, tau -> mu nu nu','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931   


    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsK':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs+ -> D*K','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2TauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+ -> tau+ nu, tau -> 3pi nu TAUHADNU model','','0.05799621863924','1.0','1.0'],#6645.46*2*0.43*0.000109*0.0931
    'p8_ee_Zbb_ecm91_EvtGen_Bu2TauNuTau23PiPi0NuTAUOLA':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bu+ -> tau+ nu, tau -> 3pi pi0 nu TAUOLA model','','0.01','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_BuCocktail':['Z/Gamma* ecm=91.188GeV to bb','Bc2TaNu Bu cocktail','','877.26717','1.0','1.0'],#6645.46*0.13201
    'p8_ee_Zbb_ecm91_EvtGen_BdCocktail':['Z/Gamma* ecm=91.188GeV to bb','Bc2TaNu Bd cocktail','','691.52657','1.0','1.0'],#6645.46*0.10406
    'p8_ee_Zbb_ecm91_EvtGen_BsCocktail':['Z/Gamma* ecm=91.188GeV to bb','Bc2TaNu Bs cocktail','','155.02529','1.0','1.0'],#6645.46*0.023328
    'p8_ee_Zbb_ecm91_EvtGen_LbCocktail':['Z/Gamma* ecm=91.188GeV to bb','Bc2TaNu Lb cocktail','','75.485780','1.0','1.0'],#6645.46*0.011359


    'p8_ee_Zbb_ecm91_EvtGen_Bd2Kstee':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2Kstee','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KsteeBTOSLLBALL':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2KsteeBTOSLLBALL','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2Kstmm':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2Kstmm','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstmmBTOSLLBALL':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2KstmmBTOSLLBALL','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2Rhomm':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2Rhomm','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2Rhoee':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2Rhoee','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bs2Kstee':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2Kstee','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2KsteeBTOSLLBALL':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2KsteeBTOSLLBALL','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bs2Kstmm':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2Kstmm','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2KstmmBTOSLLBALL':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2KstmmBTOSLLBALL','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bu2Piee':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bu2Piee','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Pimm':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bu2Pimm','','1.0','1.0','1.0'],


    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2KstNuNu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2PhiNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2PhiNuNu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2KNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bu2KNuNu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LbNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Lb2LbNuNu','','1.0','1.0','1.0'],
    
    'p8_ee_Zbb_ecm91_EvtGen_Bd2D3Pi'    :['Z/Gamma* ecm=91.188GeV to bb','Bd2D3Pi','','17.1452868','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DDs'     :['Z/Gamma* ecm=91.188GeV to bb','Bd2DDs','','20.57434416','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DTauNu'  :['Z/Gamma* ecm=91.188GeV to bb','Bd2DTauNu','','30.861516240000004','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2Dst3Pi'  :['Z/Gamma* ecm=91.188GeV to bb','Bd2Dst3Pi','','20.602919638','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstDs'   :['Z/Gamma* ecm=91.188GeV to bb','Bd2DstDs','','22.8603824','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstDsst' :['Z/Gamma* ecm=91.188GeV to bb','Bd2DstDsst','','50.57859606','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstTauNu':['Z/Gamma* ecm=91.188GeV to bb','Bd2DstTauNu','','44.86350046','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bs2Ds3Pi'    :['Z/Gamma* ecm=91.188GeV to bb','Bs2Ds3Pi','','3.891581376','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsDs'     :['Z/Gamma* ecm=91.188GeV to bb','Bs2DsDs','','2.8070423040000003','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsTauNu'  :['Z/Gamma* ecm=91.188GeV to bb','Bs2DsTauNu','','15.502529088000001','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2Dsst3Pi'  :['Z/Gamma* ecm=91.188GeV to bb','Bs2Dsst3Pi','','4.5997215936','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstDs'   :['Z/Gamma* ecm=91.188GeV to bb','Bs2DsstD','','8.867701824','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstDsst' :['Z/Gamma* ecm=91.188GeV to bb','Bs2DsstDsst','','9.186683904','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstTauNu':['Z/Gamma* ecm=91.188GeV to bb','Bs2DsstTauNu','','10.335019392','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bu2D03Pi'    :['Z/Gamma* ecm=91.188GeV to bb','Bu2D03Pi','','16.00226768','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2D0Ds'     :['Z/Gamma* ecm=91.188GeV to bb','Bu2D0Ds','','25.717930199999998','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2D0TauNu'  :['Z/Gamma* ecm=91.188GeV to bb','Bu2D0TauNu','','22.003118060000002','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst03Pi'  :['Z/Gamma* ecm=91.188GeV to bb','Bu2Dsst3Pi','','29.43274234','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst0Ds'   :['Z/Gamma* ecm=91.188GeV to bb','Bu2DsstD','','21.71736328','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst0Dsst' :['Z/Gamma* ecm=91.188GeV to bb','Bu2DsstDsst','','48.86406738','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst0TauNu':['Z/Gamma* ecm=91.188GeV to bb','Bu2DsstTauNu','','53.721898640000006','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Lb2Lc3Pi'    :['Z/Gamma* ecm=91.188GeV to bb','Lb2Ds3Pi','','1.893291554','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcDs'     :['Z/Gamma* ecm=91.188GeV to bb','Lb2DsDs','','2.7047022199999997','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcTauNu'  :['Z/Gamma* ecm=91.188GeV to bb','Lb2DsTauNu','','8.040342054','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2Lcst3Pi'  :['Z/Gamma* ecm=91.188GeV to bb','Lb2Dsst3Pi','','1.893291554','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcstDs'   :['Z/Gamma* ecm=91.188GeV to bb','Lb2DsstD','','2.7047022199999997','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcstDsst' :['Z/Gamma* ecm=91.188GeV to bb','Lb2DsstDsst','','2.7047022199999997','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcstTauNu':['Z/Gamma* ecm=91.188GeV to bb','Lb2DsstTauNu','','8.040342054','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstarTauTau':['Z/Gamma* ecm=91.188GeV to bb','B to K* tautau decay, with  taus decaying into 3 pions','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2pipipipi0':['Z/Gamma* ecm=91.188GeV to bb','B0 -> (Ds+ ->  pi+  pi+  pi-  pi0) (Ds- -> pi-  pi-  pi+  pi0) (K*0 -> K+ pi-)','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2Taunu':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds+ Ds- K*0, K*0 forced to K+ pi-, Ds forced to tau nu','','1','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2TaunuDs2pipipipi0':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds+ Ds- K*0, K*0 forced to K+ pi-, Ds forced to tau nu or 3pi1pi0','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2pipipipi0pi0':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds+ Ds- K*0, K*0 forced to K+ pi-, Ds forced to pipipipipi0','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsKstarTauNuDs2TauNu':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds K*0 tau nu, K*0 forced to K+ pi-, Ds forced to tau nu','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsstarDsKstarDs2TaunuDsstar2Dsgamma':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds*+ Ds- K*0, K*0 forced to K+ pi-, Ds forced to tau nu, D*s+ forced in Ds gamma','','1','1.0','1.0'],
#Bu = 0.307 * 0.43 = 0.13201
#Bd = 0.242 * 0.43 = 0.10406
#Bs = 0.243 * 0.096 = 0.023328
#Lb = 0.307 * 0.037 = 0.011359
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsK':['Z/Gamma* ecm=91.188GeV to bb','B0 to Ds K, Ds to Phi pi or Phi rho','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2Dsstarpi':['Z/Gamma* ecm=91.188GeV to bb','B0 to Ds* pi, Ds* to gamma Phi pi or gamma Phi rho','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsK':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds K, Ds to Phi pi or Phi rho','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsKstar':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds K*, Ds to Phi pi or Phi rho, K* to K pi0','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2Dspi':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds pi, Ds to Phi pi or Phi rho','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2Dsrho':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds rho, Ds to Phi pi','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstarK':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds* K, Ds* to gamma Phi pi or gamma Phi rho','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2Dsstarpi':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds* pi, Ds* to gamma Phi pi or gamma Phi rho','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2Dsp':['Z/Gamma* ecm=91.188GeV to bb','Lambda0 to Ds p, Ds to Phi pi or Phi rho','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2Dsstarp':['Z/Gamma* ecm=91.188GeV to bb','Lambda0 to Ds* p, Ds* to gamma Phi pi or gamma Phi rho','','1','1.0','1.0'],

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
    'mg_ee_zhh_ecm365':['e+e- -> ZHH', 'LO', '', '2.0e-5', '1.0', '1.0'],

    'wzp6_ee_mumuH_ecm240':['mumuH ecm=240 GeV','inclusive Higgs decays','','6.7643e-3','1.0','1.0'],
    'wzp6_ee_mumuH_noISR_ecm240':['mumuH ecm=240 GeV, no ISR','inclusive Higgs decays','','7.9757e-3','1.0','1.0'],
    'wzp6_ee_mumuH_ISRnoRecoil_ecm240':['mumuH ecm=240 GeV, ISR  pT=0','inclusive Higgs decays','','6.7223e-3','1.0','1.0'],
    'wzp6_noBES_ee_mumuH_ecm240':['mumuH ecm=240 GeV','inclusive Higgs decays','','6.7626e-3','1.0','1.0'],
    'wzp6_ee_mumuH_mH-higher-100MeV_ecm240':['mumuH ecm=240 GeV, vary mH','inclusive Higgs decays','','6.7393e-3','1.0','1.0'],
    'wzp6_ee_mumuH_mH-higher-50MeV_ecm240':['mumuH ecm=240 GeV, vary mH','inclusive Higgs decays','','6.7488e-3','1.0','1.0'],
    'wzp6_ee_mumuH_mH-lower-50MeV_ecm240':['mumuH ecm=240 GeV, vary mH','inclusive Higgs decays','','6.7738e-3','1.0','1.0'],
    'wzp6_ee_mumuH_mH-lower-100MeV_ecm240':['mumuH ecm=240 GeV, vary mH','inclusive Higgs decays','','6.7849e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-higher-6pc_ecm240':['mumuH ecm=240 GeV, vary BES','inclusive Higgs decays','','6.76052e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-lower-6pc_ecm240':['mumuH ecm=240 GeV, vary BES','inclusive Higgs decays','','6.76602e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-higher-1pc_ecm240':['mumuH ecm=240 GeV, vary BES','inclusive Higgs decays','','6.76140e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-lower-1pc_ecm240':['mumuH ecm=240 GeV, vary BES','inclusive Higgs decays','','6.76093e-3','1.0','1.0'],
    'wzp6_ee_mumuH_noFSR_ecm240':['mumuH ecm=240 GeV, no FSR','inclusive Higgs decays','','6.7602e-3','1.0','1.0'],


    'wzp6_ee_tautauH_ecm240':['tautauH ecm=240 GeV','inclusive Higgs decays','','6.7518e-3','1.0','1.0'],
    'wzp6_ee_eeH_ecm240':['eeH ecm=240 GeV','inclusive Higgs decays','','7.1611e-3','1.0','1.0'],
    'wzp6_ee_nunuH_ecm240':['nunuH ecm=240 GeV (all nu flavours)','inclusive Higgs decays','','46.191e-3','1.0','1.0'],
    'wzp6_ee_qqH_ecm240':['qqH ecm=240 GeV, q = u,d,s,c,b','inclusive Higgs decays','','136.35e-3','1.0','1.0'],

    'wzp6_egamma_eZ_Zmumu_ecm240':['e(e)Z EPA, e- gamma, ecm=240 GeV','Z to mumu','','103.68e-3','1.0','1.0'],
    'wzp6_gammae_eZ_Zmumu_ecm240':['e(e)Z EPA, e+ gamma, ecm=240 GeV','Z to mumu','','103.68e-3','1.0','1.0'],
    'wzp6_egamma_eZ_Zbb_ecm240':['e(e)Z EPA, e- gamma, ecm=240 GeV','Z to bb','','455.7e-3','1.0','1.0'],
    'wzp6_gammae_eZ_Zbb_ecm240':['e(e)Z EPA, e+ gamma, ecm=240 GeV','Z to bb','','455.7e-3','1.0','1.0'],
    'wzp6_egamma_eZ_Zqq_ecm240':['e(e)Z EPA, e- gamma, ecm=240 GeV','Z to qq, q=udsc','','1.6369','1.0','1.0'],
    'wzp6_gammae_eZ_Zqq_ecm240':['e(e)Z EPA, e+ gamma, ecm=240 GeV','Z to qq, q=udsc','','1.6369','1.0','1.0'],
    'wzp6_egamma_tbnu_ecm240':['nu_e t b (e) EPA, e- gamma, ecm=240 GeV','inc. top decays','','1.0753e-5','1.0','1.0'],
    'wzp6_gammae_tbnu_ecm240':['nu_e t b (e) EPA, e+ gamma, ecm=240 GeV','inc. top decays','','1.0753e-5','1.0','1.0'],


    'wzp6_gaga_mumu_60_ecm240':['gammagamma to mumu, M(mumu) > 60 GeV,  ecm=240 GeV','','','1.5523','1.0','1.0'],
    'wzp6_gaga_tautau_60_ecm240':['gammagamma to tautau, M(tautau) > 60 GeV,  ecm=240 GeV','','','0.836','1.0','1.0'],
   
    'wzp6_ee_mumu_ecm240':['Z/gamma* to mumu, ecm=240 GeV','full phase space','','5.288','1.0','1.0'],
    'wzp6_ee_mumu_noFSR_ecm240':['Z/gamma* to mumu, ecm=240 GeV, no FSR','full phase space','','5.301','1.0','1.0'],

    'wzp6_ee_tautau_ecm240':['Z/gamma* to tautau, ecm=240 GeV','full phase space','','4.668','1.0','1.0'],
    'wzp6_ee_ee_Mee_30_150_ecm240':['ee (s and t), ecm=240 GeV','30 < Mee < 150 GeV, 15 < theta < 165 deg','','8.305','1.0','1.0'],

    'kkmc_ee_mumu_ecm240':['Z/gamma* to mumu, ecm=240 GeV','full phase space','','5.24619','1.0','1.0'],
    'kkmc_ee_mumu_noFSR_ecm240':['Z/gamma* to mumu, ecm=240 GeV, no FSR','full phase space','','5.77305','1.0','1.0'],

    'wzp6_ee_gammagamma_ecm91':['diphoton production','|cos(theta)| < 0.95 for the two leading photons','','45.454','1.0','1.0'],

    'wzp6_ee_ZZ_test_ecm240':['ZZ ecm=240 GeV','inclusive Z decays by Pythia','','1.11','1.0','1.0'],

    'wzp6_ee_nuenueZ_ecm240':['Z nue nuebar, W-exchange only','inclusive Z decays by Pythia','','3.3274e-2','1.0','1.0'],

# for Higgs, sqrts = 365 GeV:
    'wzp6_ee_mumuH_ecm365':['mumuH ecm=365 GeV','inclusive Higgs decays','','4.185e-3','1.0','1.0'],
    'wzp6_ee_tautauH_ecm365':['tautauH ecm=365 GeV','inclusive Higgs decays','','4.172e-3','1.0','1.0'],
    'wzp6_ee_eeH_ecm365':['eeH ecm=365 GeV','inclusive Higgs decays','','7.390e-3','1.0','1.0'],
    'wzp6_ee_nunuH_ecm365':['nunuH ecm=365 GeV (all nu flavours)','inclusive Higgs decays','','53.94e-3','1.0','1.0'],
    'wzp6_ee_qqH_ecm365':['qqH ecm=365 GeV, q = u,d,s,c,b','inclusive Higgs decays','','84.307e-3','1.0','1.0'],

    'wzp6_egamma_eZ_Zmumu_ecm365':['e(e)Z EPA, e- gamma, ecm=365 GeV','Z to mumu','','140.0e-3','1.0','1.0'],
    'wzp6_gammae_eZ_Zmumu_ecm365':['e(e)Z EPA, e+ gamma, ecm=365 GeV','Z to mumu','','140.0e-3','1.0','1.0'],

    'wzp6_gaga_mumu_60_ecm365':['gammagamma to mumu, M(mumu) > 60 GeV,  ecm=365 GeV','','','2.843','1.0','1.0'],
    'wzp6_gaga_tautau_60_ecm365':['gammagamma to tautau, M(tautau) > 60 GeV,  ecm=365 GeV','','','1.537','1.0','1.0'],

    'wzp6_ee_mumu_ecm365':['Z/gamma* to mumu, ecm=365 GeV','full phase space','','2.287','1.0','1.0'],
    'wzp6_ee_tautau_ecm365':['Z/gamma* to tautau, ecm=365 GeV','full phase space','','2.017','1.0','1.0'],
    'wzp6_ee_ee_Mee_30_150_ecm365':['ee (s and t), ecm=365 GeV','30 < Mee < 150 GeV, 15 < theta < 165 deg','','1.53','1.0','1.0'],











}

