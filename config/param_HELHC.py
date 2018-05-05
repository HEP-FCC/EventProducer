#module
module_name='config/param_HELHC.py'

#eos tests
eostest='/eos/experiment/fcc/hh/tests/testfile.lhe.gz'
eostest_size=1312594

#stat
lhe_stat="/afs/cern.ch/user/h/helsens/www/data/statlhe_HELHC.html"
delphes_stat="/afs/cern.ch/user/h/helsens/www/data/statdelphesVERSION_HELHC.html"

#web
lhe_web="/afs/cern.ch/user/h/helsens/www/data/LHEevents_helhc.txt"
delphes_web="/afs/cern.ch/user/h/helsens/www/data/Delphesevents_VERSION.txt"

#yaml directory
yamldir='/afs/cern.ch/work/h/helsens/public/FCCDicts/yaml/HELHC/'
yamlcheck_lhe='/afs/cern.ch/work/h/helsens/public/FCCDicts/yaml/HELHC/lhe/check.yaml'
yamlcheck_reco='/afs/cern.ch/work/h/helsens/public/FCCDicts/yaml/HELHC/VERSION/check.yaml'

#heppy and proc lists
heppyList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/HELHC_heppySampleList_VERSION.py'
procList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/HELHC_procDict_VERSION.json'

##eos directory for MG5@MCatNLO gridpacks
gp_dir      = '/eos/experiment/fcc/helhc/generation/gridpacks/'
##eos directory for lhe files
lhe_dir     = '/eos/experiment/fcc/helhc/generation/lhe/'
##extension
lhe_ext     ='.lhe.gz'

##FCC versions
fcc_versions=['helhc_v01']

##eos directory for FCCSW pythia delphes files
delphes_dir = '/eos/experiment/fcc/helhc/generation/DelphesEvents/'
##extension
delphes_ext='.root'
##name of the ttree
treename='events'

##where the delphes cards are stored
delphescards_dir = '/eos/experiment/fcc/helhc/utils/delphescards/'
##where the pythia cards are stored
pythiacards_dir  = '/eos/experiment/fcc/helhc/utils/pythiacards/'
##where the FCC config script is stored
fccconfig_dir    = '/eos/experiment/fcc/helhc/utils/config/'

##muom momentum delphes resolution card
delphescard_mmr='muonMomentumResolutionVsP.tcl'
##momentum resolution delphes card
delphescard_mr='momentumResolutionVsP.tcl'
##delphes base card
delphescard_base='card.tcl'
##FCC config script name
fccconfig='PythiaDelphes_config_v02.py'

##base dir of FCCSW
fccsw_dir='/cvmfs/fcc.cern.ch/sw/0.8.2/'
##init script for FCCSW
stack=fccsw_dir+'init_fcc_stack.sh'
##FCCSW dir
fccsw=fccsw_dir+'fccsw/0.8.2/x86_64-slc6-gcc62-opt/'

#list of processes only with Pythia, meaning no LHE
pythialist={
'dummy':['','','','','',''],

'p8_pp_ZprimePSI_1TeV_ll':['','','','1.26327','1.0','1.0'],
'p8_pp_ZprimePSI_2TeV_ll':['','','','0.085362','1.0','1.0'],
'p8_pp_ZprimePSI_4TeV_ll':['','','','0.00336506','1.0','1.0'],
'p8_pp_ZprimePSI_6TeV_ll':['','','','0.000319221','1.0','1.0'],
'p8_pp_ZprimePSI_8TeV_ll':['','','','4.16344e-05','1.0','1.0'],
'p8_pp_ZprimePSI_10TeV_ll':['','','','6.47563e-06','1.0','1.0'],
'p8_pp_ZprimePSI_12TeV_ll':['','','','1.39881e-06','1.0','1.0'],
'p8_pp_ZprimePSI_14TeV_ll':['','','','4.60545e-07','1.0','1.0'],
'p8_pp_ZprimePSI_16TeV_ll':['','','','2.25108e-07','1.0','1.0'],
'p8_pp_ZprimeI_1TeV_ll':['','','','2.30174','1.0','1.0'],
'p8_pp_ZprimeI_2TeV_ll':['','','','0.153677','1.0','1.0'],
'p8_pp_ZprimeI_4TeV_ll':['','','','0.00582704','1.0','1.0'],
'p8_pp_ZprimeI_6TeV_ll':['','','','0.000515749','1.0','1.0'],
'p8_pp_ZprimeI_8TeV_ll':['','','','6.57607e-05','1.0','1.0'],
'p8_pp_ZprimeI_10TeV_ll':['','','','1.17107e-05','1.0','1.0'],
'p8_pp_ZprimeI_12TeV_ll':['','','','3.37889e-06','1.0','1.0'],
'p8_pp_ZprimeI_14TeV_ll':['','','','1.46041e-06','1.0','1.0'],
'p8_pp_ZprimeI_16TeV_ll':['','','','7.89383e-07','1.0','1.0'],
'p8_pp_ZprimeCHI_1TeV_ll':['','','','2.72389','1.0','1.0'],
'p8_pp_ZprimeCHI_2TeV_ll':['','','','0.181617','1.0','1.0'],
'p8_pp_ZprimeCHI_4TeV_ll':['','','','0.00703298','1.0','1.0'],
'p8_pp_ZprimeCHI_6TeV_ll':['','','','0.000658995','1.0','1.0'],
'p8_pp_ZprimeCHI_8TeV_ll':['','','','8.70986e-05','1.0','1.0'],
'p8_pp_ZprimeCHI_10TeV_ll':['','','','1.57176e-05','1.0','1.0'],
'p8_pp_ZprimeCHI_12TeV_ll':['','','','4.46175e-06','1.0','1.0'],
'p8_pp_ZprimeCHI_14TeV_ll':['','','','1.89368e-06','1.0','1.0'],
'p8_pp_ZprimeCHI_16TeV_ll':['','','','1.02383e-06','1.0','1.0'],
'p8_pp_ZprimeLRM_1TeV_ll':['','','','0.715268','1.0','1.0'],
'p8_pp_ZprimeLRM_2TeV_ll':['','','','0.0484138','1.0','1.0'],
'p8_pp_ZprimeLRM_4TeV_ll':['','','','0.0018759','1.0','1.0'],
'p8_pp_ZprimeLRM_6TeV_ll':['','','','0.000176737','1.0','1.0'],
'p8_pp_ZprimeLRM_8TeV_ll':['','','','2.25296e-05','1.0','1.0'],
'p8_pp_ZprimeLRM_10TeV_ll':['','','','3.46554e-06','1.0','1.0'],
'p8_pp_ZprimeLRM_12TeV_ll':['','','','7.60703e-07','1.0','1.0'],
'p8_pp_ZprimeLRM_14TeV_ll':['','','','2.53854e-07','1.0','1.0'],
'p8_pp_ZprimeLRM_16TeV_ll':['','','','1.25292e-07','1.0','1.0'],
'p8_pp_ZprimeSSM_1TeV_ll':['','','','4.43703','1.0','1.0'],
'p8_pp_ZprimeSSM_2TeV_ll':['','','','0.299201','1.0','1.0'],
'p8_pp_ZprimeSSM_4TeV_ll':['','','','0.0125426','1.0','1.0'],
'p8_pp_ZprimeSSM_6TeV_ll':['','','','0.00127705','1.0','1.0'],
'p8_pp_ZprimeSSM_8TeV_ll':['','','','0.000204715','1.0','1.0'],
'p8_pp_ZprimeSSM_10TeV_ll':['','','','4.76451e-05','1.0','1.0'],
'p8_pp_ZprimeSSM_12TeV_ll':['','','','1.6009e-05','1.0','1.0'],
'p8_pp_ZprimeSSM_14TeV_ll':['','','','7.50234e-06','1.0','1.0'],
'p8_pp_ZprimeSSM_16TeV_ll':['','','','4.1616e-06','1.0','1.0'],
'p8_pp_ZprimeETA_1TeV_ll':['','','','1.43422','1.0','1.0'],
'p8_pp_ZprimeETA_2TeV_ll':['','','','0.0975244','1.0','1.0'],
'p8_pp_ZprimeETA_4TeV_ll':['','','','0.0038843','1.0','1.0'],
'p8_pp_ZprimeETA_6TeV_ll':['','','','0.000373203','1.0','1.0'],
'p8_pp_ZprimeETA_8TeV_ll':['','','','4.90595e-05','1.0','1.0'],
'p8_pp_ZprimeETA_10TeV_ll':['','','','8.00358e-06','1.0','1.0'],
'p8_pp_ZprimeETA_12TeV_ll':['','','','1.80172e-06','1.0','1.0'],
'p8_pp_ZprimeETA_14TeV_ll':['','','','6.12268e-07','1.0','1.0'],
'p8_pp_ZprimeETA_16TeV_ll':['','','','3.03296e-07','1.0','1.0'],

'p8_pp_Zprime_2TeV_ttbar':['2TeV Z\' -> ttbar','','','7.6378','1.0','1.0'],
'p8_pp_Zprime_4TeV_ttbar':['4TeV Z\' -> ttbar','','','-9999','1.0','1.0'],
'p8_pp_Zprime_5TeV_ttbar':['5TeV Z\' -> ttbar','','','0.305493','1.0','1.0'],
'p8_pp_Zprime_6TeV_ttbar':['6TeV Z\' -> ttbar','','','-9999','1.0','1.0'],
'p8_pp_Zprime_8TeV_ttbar':['8TeV Z\' -> ttbar','','','-9999','1.0','1.0'],
'p8_pp_Zprime_10TeV_ttbar':['10TeV Z\' -> ttbar','','','0.0175724','1.0','1.0'],
'p8_pp_Zprime_12TeV_ttbar':['12TeV Z\' -> ttbar','','','-9999','1.0','1.0'],
'p8_pp_Zprime_14TeV_ttbar':['14TeV Z\' -> ttbar','','','-9999','1.0','1.0'],
'p8_pp_Zprime_15TeV_ttbar':['15TeV Z\' -> ttbar','','','0.002439429','1.0','1.0'],

'p8_pp_RSGraviton_2TeV_ww':['2TeV Z\' -> WW','','','1.811e1','1.0','1.0'],
'p8_pp_RSGraviton_4TeV_ww':['4TeV Z\' -> WW','','','-9999','1.0','1.0'],
'p8_pp_RSGraviton_5TeV_ww':['5TeV Z\' -> WW','','','2.892e-1','1.0','1.0'],
'p8_pp_RSGraviton_6TeV_ww':['6TeV Z\' -> WW','','','-9999','1.0','1.0'],
'p8_pp_RSGraviton_8TeV_ww':['8TeV Z\' -> WW','','','-9999','1.0','1.0'],
'p8_pp_RSGraviton_10TeV_ww':['10TeV Z\' -> WW','','','7.686e-3','1.0','1.0'],
'p8_pp_RSGraviton_12TeV_ww':['12TeV Z\' -> WW','','','-9999','1.0','1.0'],
'p8_pp_RSGraviton_14TeV_ww':['14TeV Z\' -> WW','','','-9999','1.0','1.0'],
'p8_pp_RSGraviton_15TeV_ww':['15TeV Z\' -> WW','','','7.386e-4','1.0','1.0'],

}


##list of possible decays of LHE files

decaylist = {
'mg_pp_h012j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_hh01j_5f':['hhaabb'],
'mg_pp_vbf_h01j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau', 'hnunununu'],
'mg_pp_tth01j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_vh012j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_v0123j_5f':['znunu'],
'mg_pp_z0123j_4f':['zll'],
'mg_pp_w0123j_4f':['wlv'],
'mg_pp_ttz_5f':['znunu'],
'mg_pp_hh_lambda050_5f':['haa'],
'mg_pp_hh_lambda090_5f':['haa'],
'mg_pp_hh_lambda095_5f':['haa'],
'mg_pp_hh_lambda100_5f':['haa'],
'mg_pp_hh_lambda105_5f':['haa'],
'mg_pp_hh_lambda110_5f':['haa'],
'mg_pp_hh_lambda150_5f':['haa'],
'mg_pp_hhj_lambda090_5f':['hhbbbb'],
'mg_pp_hhj_lambda095_5f':['hhbbbb'],
'mg_pp_hhj_lambda100_5f':['hhbbbb'],
'mg_pp_hhj_lambda105_5f':['hhbbbb'],
'mg_pp_hhj_lambda110_5f':['hhbbbb'],
'mg_pp_hhj_lambda150_5f':['hhbbbb'],
'mg_pp_hhj_lambda050_5f':['hhbbbb'],

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
'wlv':3*0.108,
'hhaabb':2*2.270E-03*5.824E-01,
'hhbbbb':5.824E-01*5.824E-01,
'znunu':0.205,
}


##Gridpack list for MG5@MC@NLO
##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency

gridpacklist = {
'dummy':['','','','','',''],
'mg_pp_ee_lo':['di-electron','pT(e)>1TeV','','0.000621','1.0','1.0'],
'mg_pp_ee_5f_HT_500_1000':['ee','500 < HT < 1000','no matching','0.1267','2.00','1.0'],
'mg_pp_ee_5f_HT_1000_2000':['ee','1000 < HT < 2000','no matching','0.01034','2.00','1.0'],
'mg_pp_ee_5f_HT_2000_5000':['ee','2000 < HT < 5000','no matching','0.0006172','2.00','1.0'],
'mg_pp_ee_5f_HT_5000_10000':['ee','5000 < HT < 10000','no matching','2.603e-06','2.00','1.0'],
'mg_pp_ee_5f_HT_10000_27000':['ee','10000 < HT < 27000','no matching','6.65e-09','2.00','1.0'],

'mg_pp_mumu_lo':['di-muon','pT(mu)>1TeV','','0.000621','1.0','1.0'],
'mg_pp_mumu_5f_HT_500_1000':['mumu','500 < HT < 1000','no matching','0.1267','2.00','1.0'],
'mg_pp_mumu_5f_HT_1000_2000':['mumu','1000 < HT < 2000','no matching','0.01034','2.00','1.0'],
'mg_pp_mumu_5f_HT_2000_5000':['mumu','2000 < HT < 5000','no matching','0.0006172','2.00','1.0'],
'mg_pp_mumu_5f_HT_5000_10000':['mumu','5000 < HT < 10000','no matching','2.603e-06','2.00','1.0'],
'mg_pp_mumu_5f_HT_10000_27000':['mumu','10000 < HT < 27000','no matching','6.65e-09','2.00','1.0'],

'mg_pp_tautau_5f_HT_500_1000':['tautau','500 < HT < 1000','no matching','0.1267','2.00','1.0'],
'mg_pp_tautau_5f_HT_1000_2000':['tautau','1000 < HT < 2000','no matching','0.01034','2.00','1.0'],
'mg_pp_tautau_5f_HT_2000_5000':['tautau','2000 < HT < 5000','no matching','0.0006172','2.00','1.0'],
'mg_pp_tautau_5f_HT_5000_10000':['tautau','5000 < HT < 10000','no matching','2.603e-06','2.00','1.0'],
'mg_pp_tautau_5f_HT_10000_27000':['tautau','10000 < HT < 27000','no matching','6.65e-09','2.00','1.0'],

'mg_pp_tt_lo':['top pair','pT(t)>0.5TeV','','11.09','1.0','1.0'],
'mg_pp_tt_5f_HT_500_1000':['di top','500 < HT < 1000','no matching','164.4','2.00','1.0'],
'mg_pp_tt_5f_HT_1000_2000':['di top','1000 < HT < 2000','no matching','10.72','2.00','1.0'],
'mg_pp_tt_5f_HT_2000_5000':['di top','2000 < HT < 5000','no matching','0.3235','2.00','1.0'],
'mg_pp_tt_5f_HT_5000_10000':['di top','5000 < HT < 10000','no matching','0.0008756','2.00','1.0'],
'mg_pp_tt_5f_HT_10000_27000':['di top','10000 < HT < 27000','no matching','1.214e-06','2.00','1.0'],

'mg_pp_jj_lo':['di-jet','pT(j)>0.5TeV','','3871','1.0','1.0'],
'mg_pp_jj_5f_HT_500_1000':['di jet 5f','500 < HT < 1000','no matching','9.202e+04','2.00','1.0'],
'mg_pp_jj_5f_HT_1000_2000':['di jet 5f','1000 < HT < 2000','no matching','3966','2.00','1.0'],
'mg_pp_jj_5f_HT_2000_5000':['di jet 5f','2000 < HT < 5000','no matching','118','2.00','1.0'],
'mg_pp_jj_5f_HT_5000_10000':['di jet 5f','5000 < HT < 10000','no matching','0.3968','2.00','1.0'],
'mg_pp_jj_5f_HT_10000_27000':['di jet 5f','10000 < HT < 27000','no matching','0.0008586','2.00','1.0'],


'mg_pp_tth01j_5f':['higgs associated with top pair + 0/1 jets','inclusive','xqcut = 80, qCut = 120','3.274','1.22','0.612'],
'mg_pp_jjaa_5f':['dijet diphoton','','','5.941','1.0','1.0'],
'mg_pp_jjja_5f':['photon +jets','','','1.125e+04','1.0','1.0'],
'mg_pp_hh_5f_kl_0500':['HH, H->bb, H undec., kl = ','inclusive','','0.1612','1.0','1.0'],
'mg_pp_hh_5f_kl_0750':['HH, H->bb, H undec., kl = ','inclusive','','0.1349','1.0','1.0'],
'mg_pp_hh_5f_kl_0800':['HH, H->bb, H undec., kl = ','inclusive','','0.1307','1.0','1.0'],
'mg_pp_hh_5f_kl_0850':['HH, H->bb, H undec., kl = ','inclusive','','0.1253','1.0','1.0'],
'mg_pp_hh_5f_kl_0875':['HH, H->bb, H undec., kl = ','inclusive','','0.1231','1.0','1.0'],
'mg_pp_hh_5f_kl_0900':['HH, H->bb, H undec., kl = ','inclusive','','0.1213','1.0','1.0'],
'mg_pp_hh_5f_kl_0925':['HH, H->bb, H undec., kl = ','inclusive','','0.1192','1.0','1.0'],
'mg_pp_hh_5f_kl_0950':['HH, H->bb, H undec., kl = ','inclusive','','0.1169','1.0','1.0'],
'mg_pp_hh_5f_kl_0975':['HH, H->bb, H undec., kl = ','inclusive','','0.1148','1.0','1.0'],
'mg_pp_hh_5f_kl_1000':['HH, H->bb, H undec., kl = ','inclusive','','0.1127','1.0','1.0'],
'mg_pp_hh_5f_kl_1025':['HH, H->bb, H undec., kl = ','inclusive','','0.11','1.0','1.0'],
'mg_pp_hh_5f_kl_1050':['HH, H->bb, H undec., kl = ','inclusive','','0.1084','1.0','1.0'],
'mg_pp_hh_5f_kl_1075':['HH, H->bb, H undec., kl = ','inclusive','','0.1059','1.0','1.0'],
'mg_pp_hh_5f_kl_1100':['HH, H->bb, H undec., kl = ','inclusive','','0.1039','1.0','1.0'],
'mg_pp_hh_5f_kl_1125':['HH, H->bb, H undec., kl = ','inclusive','','0.1019','1.0','1.0'],
'mg_pp_hh_5f_kl_1150':['HH, H->bb, H undec., kl = ','inclusive','','0.1005','1.0','1.0'],
'mg_pp_hh_5f_kl_1200':['HH, H->bb, H undec., kl = ','inclusive','','0.09671','1.0','1.0'],
'mg_pp_hh_5f_kl_1250':['HH, H->bb, H undec., kl = ','inclusive','','0.09307','1.0','1.0'],
'mg_pp_hh_5f_kl_1500':['HH, H->bb, H undec., kl = ','inclusive','','0.07687','1.0','1.0'],


'mg_pp_bbh_4f':['bbar plus higgs','50 < mbb < 300','','1.0','1.0','1.0'],

'mg_pp_vj_lo':['boson+1jet','pT(v,j)>0.5TeV','','18.54','1.0','1.0'],
'mg_pp_vv_lo':['di-boson','pT(v)>0.5TeV','','0.1562','1.0','1.0'],
'mg_pp_vv_5f_HT_500_1000':['di boson','500 < HT < 1000','no matching','1.74','2.00','1.0'],
'mg_pp_vv_5f_HT_1000_2000':['di boson','1000 < HT < 2000','no matching','0.1483','2.00','1.0'],
'mg_pp_vv_5f_HT_2000_5000':['di boson','2000 < HT < 5000','no matching','0.008341','2.00','1.0'],
'mg_pp_vv_5f_HT_5000_10000':['di boson','5000 < HT < 10000','no matching','4.367e-05','2.00','1.0'],
'mg_pp_vv_5f_HT_10000_27000':['di boson','10000 < HT < 27000','no matching','7.496e-08','2.00','1.0'],

'mg_pp_vj_5f_HT_500_1000':['v+jet 5f','500 < HT < 1000','no matching','277.3','2.00','1.0'],
'mg_pp_vj_5f_HT_1000_2000':['v+jet 5f','1000 < HT < 2000','no matching','18.03','2.00','1.0'],
'mg_pp_vj_5f_HT_2000_5000':['v+jet 5f','2000 < HT < 5000','no matching','0.7608','2.00','1.0'],
'mg_pp_vj_5f_HT_5000_10000':['v+jet 5f','5000 < HT < 10000','no matching','0.003244','2.00','1.0'],
'mg_pp_vj_5f_HT_10000_27000':['v+jet 5f','10000 < HT < 27000','no matching','4.769e-06','2.00','1.0'],



}


