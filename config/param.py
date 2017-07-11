#dicts
##LHE dictionnary
lhe_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json'
##FCC events dictionnary
fcc_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_fcc_v01.json'
fcc_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_VERSION.json'

fcc_versions=['fcc_v01', 'cms']

##LHE read file true/false
readlhe_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/readLHE.json'
##FCC read file true/false
readfcc_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/readFCC.json'
readfcc_dic ='/afs/cern.ch/work/h/helsens/public/FCCDicts/readFCC_VERSION.json'

##eos directory for MG5@MCatNLO gridpacks
gp_dir      = '/eos/experiment/fcc/hh/generation/mg5_amcatnlo/gridpacks/'
##eos directory for lhe files
lhe_dir     = '/eos/experiment/fcc/hh/generation/mg5_amcatnlo/lhe/'

##eos directory for FCCSW pythia delphes files
delphes_dir = '/eos/experiment/fcc/hh/generation/DelphesEvents/'

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
'pp_Zprime_5TeV_ll':['5TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','1.043e-1','1.0','1.0'],
'pp_Zprime_10TeV_ll':['10TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','5.914e-3','1.0','1.0'],
'pp_Zprime_15TeV_ll':['15TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','7.989e-4','1.0','1.0'],
'pp_Zprime_20TeV_ll':['20TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','1.639e-4','1.0','1.0'],
'pp_Zprime_25TeV_ll':['25TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','4.437e-5','1.0','1.0'],
'pp_Zprime_30TeV_ll':['30TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','1.375e-5','1.0','1.0'],
'pp_Zprime_35TeV_ll':['35TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','4.821e-6','1.0','1.0'],
'pp_Zprime_40TeV_ll':['40TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','2.171e-6','1.0','1.0'],
'pp_Zprime_45TeV_ll':['45TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','1.165e-6','1.0','1.0'],
'pp_Zprime_50TeV_ll':['50TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','6.863e-7','1.0','1.0'],
'pp_Zprime_2TeV_ttbar':['2TeV Z\' -> ttbar','','','7.6378','1.0','1.0'],
'pp_Zprime_5TeV_ttbar':['5TeV Z\' -> ttbar','','','0.305493','1.0','1.0'],
'pp_Zprime_10TeV_ttbar':['10TeV Z\' -> ttbar','','','0.0175724','1.0','1.0'],
'pp_Zprime_15TeV_ttbar':['15TeV Z\' -> ttbar','','','0.002439429','1.0','1.0'],
'pp_Zprime_20TeV_ttbar':['20TeV Z\' -> ttbar','','','0.0004845249','1.0','1.0'],
'pp_Zprime_25TeV_ttbar':['25TeV Z\' -> ttbar','','','0.0001164359','1.0','1.0'],
'pp_Zprime_30TeV_ttbar':['30TeV Z\' -> ttbar','','','3.16759213029e-05','1.0','1.0'],
'pp_Zprime_35TeV_ttbar':['35TeV Z\' -> ttbar','','','9.65649631373e-06','1.0','1.0'],
'pp_Zprime_40TeV_ttbar':['40TeV Z\' -> ttbar','','','3.4131033281e-06','1.0','1.0'],
'pp_RSGraviton_2TeV_ww':['2TeV Z\' -> WW','','','1.811e1','1.0','1.0'],
'pp_RSGraviton_5TeV_ww':['5TeV Z\' -> WW','','','2.892e-1','1.0','1.0'],
'pp_RSGraviton_10TeV_ww':['10TeV Z\' -> WW','','','7.686e-3','1.0','1.0'],
'pp_RSGraviton_15TeV_ww':['15TeV Z\' -> WW','','','7.386e-4','1.0','1.0'],
'pp_RSGraviton_20TeV_ww':['20TeV Z\' -> WW','','','1.182e-4','1.0','1.0'],
'pp_RSGraviton_25TeV_ww':['25TeV Z\' -> WW','','','2.284e-5','1.0','1.0'],
'pp_RSGraviton_30TeV_ww':['30TeV Z\' -> WW','','','5.253e-6','1.0','1.0'],
'pp_RSGraviton_35TeV_ww':['35TeV Z\' -> WW','','','1.215e-6','1.0','1.0'],
'pp_RSGraviton_40TeV_ww':['40TeV Z\' -> WW','','','2.984e-7','1.0','1.0'],
'pp_jj_M_0_500':['di-jet','0 < M < 500','','6.517e+09','1.0','0.092'],
'pp_jj_M_500_1000':['di-jet','500 < M < 1000','','1.642e+07','1.0','0.141'],
'pp_jj_M_1000_2000':['di-jet','1000 < M < 2000','','1.673e+06','1.0','0.071'],
'pp_jj_M_2000_4000':['di-jet','2000 < M < 4000','','1.32e+05','1.0','0.057'],
'pp_jj_M_4000_7200':['di-jet','4000 < M < 7200','','7316','1.0','0.048'],
'pp_jj_M_7200_15000':['di-jet','7200 < M < 15000','','474.9','1.0','0.043'],
'pp_jj_M_15000_25000':['di-jet','15000 < M < 25000','','7.349','1.0','0.041'],
'pp_jj_M_25000_35000':['di-jet','25000 < M < 35000','','0.1759','1.0','0.041'],
'pp_jj_M_35000_100000':['di-jet','35000 < M < 100000','','0.007654','1.0','0.043'],
}


##list of possible decays of LHE files
decaylist = {
'pp_h012j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'pp_vbf_h01j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'pp_tth01j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'pp_vh012j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
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
}

##Gridpack list
##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency

gridpacklist = {
'pp_w012j_5f':['w + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','1.4995e06','1.0','0.724'],
'pp_z012j_5f':['z + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','5.1839e05','1.0','0.691'],
'pp_jjaa01j_5f':['dijet diphoton + 0,1 jets 5 flavor scheme','','xqcut = 20, qCut = 30','55.72','1.0','0.236'],
'pp_jjaa_5f':['dijet diphoton','','','17.97','1.0','1.0'],
'pp_jjja01j_5f':['photon +jets + 0,1 jets 5 flavor scheme','','xqcut = 20, qCut = 25','4.133e+05','1.0','0.143'],
'pp_jjja_5f':['photon +jets','','','1.023e05','1.0','1.0'],
'pp_jjaa_4f':['dijet diphoton 4 flavor scheme','','','431.2','1.0','1.0'],
'pp_bbja_4f':['bbja 4 flavor scheme','','','4679','1.0','1.0'],
'pp_bbaa01j_4f':['bbaa + 0,1 jets 4 flavor scheme','','xqcut = 25, qCut = 35','5.899','1.0','0.312'],
'pp_bjaa01j_4f':['bjaa + 0,1 jets 4 flavor scheme','','xqcut = 25, qCut = 35','16.9','1.0','0.335'],
'pp_z012j_5f':['z + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','5.1839e05','1.0','0.691'],
'pp_tth':['ttbar plus higgs','inclusive','','23.37','1.0','1.0'],
'pp_bbh':['bbar plus higgs','50 < mbb < 300','','0.916','1.0','1.0'],
'pp_zh':['z plus higgs production','inclusive','','7.42','1.0','1.0'],
'pp_hh':['gluon gluon fusion di-higgs','inclusive','','0.65','1.0','1.0'],
'pp_vbf_hh':['vector boson fusion di-higgs','inclusive','','0.06612','1.0','1.0'],
'pp_llll_5f':['Z/gamma* Z/gamma* to 4l','inclusive','xqcut = 40, qCut = 60','0.6045','1.0'],
'pp_llll01j_5f_HT_0_800':['Z/gamma* Z/gamma* to 4l + 0/1 jets','0 < HT < 800','xqcut = 40, qCut = 60','0.8786','1.60','0.684'],
'pp_llll01j_5f_HT_800_2000':['Z/gamma* Z/gamma* to 4l + 0/1 jets','800 < HT < 2000','xqcut = 40, qCut = 60','0.01657','1.60','0.766'],
'pp_llll01j_5f_HT_2000_4000':['Z/gamma* Z/gamma* to 4l + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','0.001004','1.60','0.785'],
'pp_llll01j_5f_HT_4000_100000':['Z/gamma* Z/gamma* to 4l + 0/1 jets','4000 < HT < 100000','xqcut = 40, qCut = 60','9.656e-05','1.60','0.781'],
'pp_llll01j_5f':['Z/gamma* Z/gamma* to 4l + 0/1 jets','inclusive','xqcut = 40, qCut = 60','0.899','1.60','0.685'],
'pp_vbf_v01j_5f_HT_0_2000':['vbf vector boson + 0/1 jets','0 < HT < 2000','xqcut = 40, qCut = 60','1.151e+07','1.20','1.0'],
'pp_vbf_v01j_5f_HT_2000_4000':['vbf vector boson + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','1.912e+04','1.20','1.0'],
'pp_vbf_v01j_5f_HT_4000_7200':['vbf vector boson + 0/1 jets','4000 < HT < 7200','xqcut = 40, qCut = 60','400.9','1.20','1.0'],
'pp_vbf_v01j_5f_HT_7200_100000':['vbf vector boson + 0/1 jets','7200 < HT < 100000','xqcut = 40, qCut = 60','72.31','1.20','1.0'],
'pp_vbf_v01j_5f':['vbf vector boson + 0/1 jets','inclusive','xqcut = 40, qCut = 60','7.081e+06','1.20','1.0'],
'pp_t123j_5f_HT_0_1900':['single top (s,t channels)+ 1/2/3 jets','0 < HT < 1900','xqcut = 40, qCut = 60','7490','2.16','0.287'],
'pp_t123j_5f_HT_1900_3500':['single top (s,t channels)+ 1/2/3 jets','1900 < HT < 3500','xqcut = 40, qCut = 60','13.65','2.16','0.194'],
'pp_t123j_5f_HT_3500_5900':['single top (s,t channels)+ 1/2/3 jets','3500 < HT < 5900','xqcut = 40, qCut = 60','1.371','2.16','0.171'],
'pp_t123j_5f_HT_5900_100000':['single top (s,t channels)+ 1/2/3 jets','5900 < HT < 100000','xqcut = 40, qCut = 60','0.175','2.16','0.158'],
'pp_t123j_5f':['single top (s,t channels)+ 1/2/3 jets','inclusive','xqcut = 40, qCut = 60','7524','2.16','0.288'],
'pp_llv01j_5f_HT_0_800':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','0 < HT < 800','xqcut = 40, qCut = 60','108.7','1.70','0.78'],
'pp_llv01j_5f_HT_800_2000':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','800 < HT < 2000','xqcut = 40, qCut = 60','0.9956','1.70','0.743'],
'pp_llv01j_5f_HT_2000_4000':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','0.07411','1.70','0.805'],
'pp_llv01j_5f_HT_4000_100000':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','4000 < HT < 100000','xqcut = 40, qCut = 60','0.008311','1.70','0.823'],
'pp_llv01j_5f':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','inclusive','xqcut = 40, qCut = 60','110.3','1.70','0.779'],
'pp_vh012j_5f_HT_0_300':['higgsstrahlung + 0/1/2 jets','0 < HT < 300','xqcut = 40, qCut = 60','25.24','1.32','0.606'],
'pp_vh012j_5f_HT_300_1400':['higgsstrahlung + 0/1/2 jets','300 < HT < 1400','xqcut = 40, qCut = 60','11.7','1.32','0.415'],
'pp_vh012j_5f_HT_1400_2900':['higgsstrahlung + 0/1/2 jets','1400 < HT < 2900','xqcut = 40, qCut = 60','0.3437','1.32','0.379'],
'pp_vh012j_5f_HT_2900_5300':['higgsstrahlung + 0/1/2 jets','2900 < HT < 5300','xqcut = 40, qCut = 60','0.03349','1.32','0.372'],
'pp_vh012j_5f_HT_5300_8800':['higgsstrahlung + 0/1/2 jets','5300 < HT < 8800','xqcut = 40, qCut = 60','0.003608','1.32','0.365'],
'pp_vh012j_5f_HT_8800_100000':['higgsstrahlung + 0/1/2 jets','8800 < HT < 100000','xqcut = 40, qCut = 60','0.0004647','1.32','0.349'],
'pp_vh012j_5f':['higgsstrahlung + 0/1/2 jets','inclusive','xqcut = 40, qCut = 60','37.43','1.32','0.544'],
'pp_tt012j_5f_HT_0_600':['top pair + 0/1/2 jets','0 < HT < 600','xqcut = 60, qCut = 90','3.207e+04','1.74','0.507'],
'pp_tt012j_5f_HT_600_1200':['top pair + 0/1/2 jets','600 < HT < 1200','xqcut = 60, qCut = 90','8883','1.74','0.351'],
'pp_tt012j_5f_HT_1200_2100':['top pair + 0/1/2 jets','1200 < HT < 2100','xqcut = 60, qCut = 90','1737','1.74','0.329'],
'pp_tt012j_5f_HT_2100_3400':['top pair + 0/1/2 jets','2100 < HT < 3400','xqcut = 60, qCut = 90','284.3','1.74','0.315'],
'pp_tt012j_5f_HT_3400_5300':['top pair + 0/1/2 jets','3400 < HT < 5300','xqcut = 60, qCut = 90','44.91','1.74','0.306'],
'pp_tt012j_5f_HT_5300_8100':['top pair + 0/1/2 jets','5300 < HT < 8100','xqcut = 60, qCut = 90','6.484','1.74','0.299'],
'pp_tt012j_5f_HT_8100_15000':['top pair + 0/1/2 jets','8100 < HT < 15000','xqcut = 60, qCut = 90','0.8583','1.74','0.294'],
'pp_tt012j_5f_HT_15000_25000':['top pair + 0/1/2 jets','15000 < HT < 25000','xqcut = 60, qCut = 90','0.0219','1.74','0.295'],
'pp_tt012j_5f_HT_25000_35000':['top pair + 0/1/2 jets','25000 < HT < 35000','xqcut = 60, qCut = 90','0.0004247','1.74','0.307'],
'pp_tt012j_5f_HT_35000_100000':['top pair + 0/1/2 jets','35000 < HT < 100000','xqcut = 60, qCut = 90','1.459e-05','1.74','0.323'],
'pp_tt012j_5f':['top pair + 0/1/2 jets','inclusive','xqcut = 60, qCut = 90','4.311e+04','1.74','0.466'],
'pp_vbf_h01j_5f_HT_0_2000':['vbf higgs + 0/1 jets','0 < HT < 2000','xqcut = 40, qCut = 60','83.91','4.3','0.188'],
'pp_vbf_h01j_5f_HT_2000_4000':['vbf higgs + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','0.07215','4.3','0.17'],
'pp_vbf_h01j_5f_HT_4000_7200':['vbf higgs + 0/1 jets','4000 < HT < 7200','xqcut = 40, qCut = 60','0.003946','4.3','0.13'],
'pp_vbf_h01j_5f_HT_7200_100000':['vbf higgs + 0/1 jets','7200 < HT < 100000','xqcut = 40, qCut = 60','0.000268','4.3','0.111'],
'pp_vbf_h01j_5f':['vbf higgs + 0/1 jets','inclusive','xqcut = 40, qCut = 60','84.17','4.3','0.187'],
'pp_vbf_hh01j_5f_HT_0_2000':['vbf di-higgs + 0/1 jets','0 < HT < 2000','xqcut = 60, qCut = 90','0.08974','1.0','1.0'],
'pp_vbf_hh01j_5f_HT_2000_4000':['vbf di-higgs + 0/1 jets','2000 < HT < 4000','xqcut = 60, qCut = 90','0.0007247','1.0','1.0'],
'pp_vbf_hh01j_5f_HT_4000_7200':['vbf di-higgs + 0/1 jets','4000 < HT < 7200','xqcut = 60, qCut = 90','7.489e-05','1.0','1.0'],
'pp_vbf_hh01j_5f_HT_7200_100000':['vbf di-higgs + 0/1 jets','7200 < HT < 100000','xqcut = 60, qCut = 90','8.888e-06','1.0','1.0'],
'pp_vbf_hh01j_5f':['vbf di-higgs + 0/1 jets','inclusive','xqcut = 60, qCut = 90','0.06453','1.0','1.0'],
'pp_tthh01j_5f':['top pair di-higgs + 0/1 jets','inclusive','xqcut = 100, qCut = 150','0.1164','1.0','1.0'],
'pp_v0123j_5f_HT_0_1500':['vector boson + 0/1/2/3 jets','0 < HT < 1500','xqcut = 30, qCut = 45','8.889e+06','1.20','0.231'],
'pp_v0123j_5f_HT_1500_2900':['vector boson + 0/1/2/3 jets','1500 < HT < 2900','xqcut = 30, qCut = 45','2868','1.20','0.257'],
'pp_v0123j_5f_HT_2900_5100':['vector boson + 0/1/2/3 jets','2900 < HT < 5100','xqcut = 30, qCut = 45','300.8','1.20','0.244'],
'pp_v0123j_5f_HT_5100_8500':['vector boson + 0/1/2/3 jets','5100 < HT < 8500','xqcut = 30, qCut = 45','30.94','1.20','0.227'],
'pp_v0123j_5f_HT_8500_100000':['vector boson + 0/1/2/3 jets','8500 < HT < 100000','xqcut = 30, qCut = 45','2.95','1.20','0.204'],
'pp_v0123j_5f':['vector boson + 0/1/2/3 jets','inclusive','xqcut = 30, qCut = 45','8.886e+06','1.20','0.232'],
'gg_aa01j_5f_HT_0_500':['gluon fusion di-photon + 0/1 jets','0 < HT < 500','xqcut = 20, qCut = 30','850.4','2.0','0.578'],
'gg_aa01j_5f_HT_500_1000':['gluon fusion di-photon + 0/1 jets','500 < HT < 1000','xqcut = 20, qCut = 30','0.5129','2.0','0.383'],
'gg_aa01j_5f_HT_1000_2000':['gluon fusion di-photon + 0/1 jets','1000 < HT < 2000','xqcut = 20, qCut = 30','0.04712','2.0','0.344'],
'gg_aa01j_5f_HT_2000_4000':['gluon fusion di-photon + 0/1 jets','2000 < HT < 4000','xqcut = 20, qCut = 30','0.002895','2.0','0.319'],
'gg_aa01j_5f_HT_4000_7200':['gluon fusion di-photon + 0/1 jets','4000 < HT < 7200','xqcut = 20, qCut = 30','8.602e-05','2.0','0.319'],
'gg_aa01j_5f_HT_7200_100000':['gluon fusion di-photon + 0/1 jets','7200 < HT < 100000','xqcut = 20, qCut = 30','4.357e-06','2.0','0.322'],
'gg_aa01j_5f':['gluon fusion di-photon + 0/1 jets','inclusive','xqcut = 20, qCut = 30','851.5','2.0','0.576'],
'pp_vv012j_4f_HT_0_300':['di-vector boson + 0/1/2 jets (4f)','0 < HT < 300','xqcut = 40, qCut = 60','3.093e+04','1.70','0.453'],
'pp_vv012j_4f_HT_300_1400':['di-vector boson + 0/1/2 jets (4f)','300 < HT < 1400','xqcut = 40, qCut = 60','2133','1.70','0.542'],
'pp_vv012j_4f_HT_1400_2900':['di-vector boson + 0/1/2 jets (4f)','1400 < HT < 2900','xqcut = 40, qCut = 60','69.23','1.70','0.534'],
'pp_vv012j_4f_HT_2900_5300':['di-vector boson + 0/1/2 jets (4f)','2900 < HT < 5300','xqcut = 40, qCut = 60','8.001','1.70','0.541'],
'pp_vv012j_4f_HT_5300_8800':['di-vector boson + 0/1/2 jets (4f)','5300 < HT < 8800','xqcut = 40, qCut = 60','0.9684','1.70','0.55'],
'pp_vv012j_4f_HT_8800_15000':['di-vector boson + 0/1/2 jets (4f)','8800 < HT < 15000','xqcut = 40, qCut = 60','0.1286','1.70','0.571'],
'pp_vv012j_4f_HT_15000_25000':['di-vector boson + 0/1/2 jets (4f)','15000 < HT < 25000','xqcut = 40, qCut = 60','0.009475','1.70','0.617'],
'pp_vv012j_4f_HT_25000_35000':['di-vector boson + 0/1/2 jets (4f)','25000 < HT < 35000','xqcut = 40, qCut = 60','0.0003517','1.70','0.69'],
'pp_vv012j_4f_HT_35000_100000':['di-vector boson + 0/1/2 jets (4f)','35000 < HT < 100000','xqcut = 40, qCut = 60','2.07e-05','1.70','0.758'],
'pp_vv012j_5f':['di-vector boson + 0/1/2 jets','inclusive','xqcut = 40, qCut = 60','3.39e+04','1.70','0.457'],
'pp_jj012j_5f_HT_0_500':['di-jet + 0/1/2 jets','0 < HT < 500','xqcut = 20, qCut = 30','6.517e+09','1.0','0.141'],
'pp_jj012j_5f_HT_500_1000':['di-jet + 0/1/2 jets','500 < HT < 1000','xqcut = 20, qCut = 30','1.642e+07','1.0','0.092'],
'pp_jj012j_5f_HT_1000_2000':['di-jet + 0/1/2 jets','1000 < HT < 2000','xqcut = 20, qCut = 30','1.673e+06','1.0','0.071'],
'pp_jj012j_5f_HT_2000_4000':['di-jet + 0/1/2 jets','2000 < HT < 4000','xqcut = 20, qCut = 30','1.32e+05','1.0','0.057'],
'pp_jj012j_5f_HT_4000_7200':['di-jet + 0/1/2 jets','4000 < HT < 7200','xqcut = 20, qCut = 30','7316','1.0','0.048'],
'pp_jj012j_5f_HT_7200_15000':['di-jet + 0/1/2 jets','7200 < HT < 15000','xqcut = 20, qCut = 30','474.9','1.0','0.043'],
'pp_jj012j_5f_HT_15000_25000':['di-jet + 0/1/2 jets','15000 < HT < 25000','xqcut = 20, qCut = 30','7.349','1.0','0.041'],
'pp_jj012j_5f_HT_25000_35000':['di-jet + 0/1/2 jets','25000 < HT < 35000','xqcut = 20, qCut = 30','0.1759','1.0','0.041'],
'pp_jj012j_5f_HT_35000_100000':['di-jet + 0/1/2 jets','35000 < HT < 100000','xqcut = 20, qCut = 30','0.007654','1.0','0.043'],
'pp_jj012j_5f':['di-jet + 0/1/2 jets','inclusive','xqcut = 20, qCut = 30','6.563e+09','1.0','0.097'],
'pp_tv012j_5f_HT_0_500':['top pair off-shell t* -> Wj + 0/1/2 jets','0 < HT < 500','xqcut = 60, qCut = 90','3000','1.34','0.488'],
'pp_tv012j_5f_HT_500_1500':['top pair off-shell t* -> Wj + 0/1/2 jets','500 < HT < 1500','xqcut = 60, qCut = 90','1124','1.34','0.396'],
'pp_tv012j_5f_HT_1500_2800':['top pair off-shell t* -> Wj + 0/1/2 jets','1500 < HT < 2800','xqcut = 60, qCut = 90','72.13','1.34','0.376'],
'pp_tv012j_5f_HT_2800_4700':['top pair off-shell t* -> Wj + 0/1/2 jets','2800 < HT < 4700','xqcut = 60, qCut = 90','7.738','1.34','0.358'],
'pp_tv012j_5f_HT_4700_7400':['top pair off-shell t* -> Wj + 0/1/2 jets','4700 < HT < 7400','xqcut = 60, qCut = 90','0.7973','1.34','0.334'],
'pp_tv012j_5f_HT_7400_100000':['top pair off-shell t* -> Wj + 0/1/2 jets','7400 < HT < 100000','xqcut = 60, qCut = 90','0.09901','1.34','0.329'],
'pp_tv012j_5f':['top pair off-shell t* -> Wj + 0/1/2 jets','inclusive','xqcut = 60, qCut = 90','4210','1.34','0.461'],
'pp_tth01j_5f_HT_0_1100':['higgs associated with top pair + 0/1 jets','0 < HT < 1100','xqcut = 80, qCut = 120','36.94','1.22','0.612'],
'pp_tth01j_5f_HT_1100_2700':['higgs associated with top pair + 0/1 jets','1100 < HT < 2700','xqcut = 80, qCut = 120','7.466','1.22','0.612'],
'pp_tth01j_5f_HT_2700_4900':['higgs associated with top pair + 0/1 jets','2700 < HT < 4900','xqcut = 80, qCut = 120','0.4224','1.22','0.634'],
'pp_tth01j_5f_HT_4900_8100':['higgs associated with top pair + 0/1 jets','4900 < HT < 8100','xqcut = 80, qCut = 120','0.0336','1.22','0.643'],
'pp_tth01j_5f_HT_8100_100000':['higgs associated with top pair + 0/1 jets','8100 < HT < 100000','xqcut = 80, qCut = 120','0.002924','1.22','0.645'],
'pp_tth01j_5f':['higgs associated with top pair + 0/1 jets','inclusive','xqcut = 80, qCut = 120','44.84','1.22','0.614'],
'pp_hh01j_5f_HT_0_300':['gluon fusion di-higgs + 0/1 jets','0 < HT < 300','xqcut = 60, qCut = 90','0.3501','3.87','0.419'],
'pp_hh01j_5f_HT_300_1400':['gluon fusion di-higgs + 0/1 jets','300 < HT < 1400','xqcut = 60, qCut = 90','0.7453','3.87','0.413'],
'pp_hh01j_5f_HT_1400_2900':['gluon fusion di-higgs + 0/1 jets','1400 < HT < 2900','xqcut = 60, qCut = 90','0.01265','3.87','0.449'],
'pp_hh01j_5f_HT_2900_5300':['gluon fusion di-higgs + 0/1 jets','2900 < HT < 5300','xqcut = 60, qCut = 90','0.0007173','3.87','0.432'],
'pp_hh01j_5f_HT_5300_8800':['gluon fusion di-higgs + 0/1 jets','5300 < HT < 8800','xqcut = 60, qCut = 90','4.124e-05','3.87','0.426'],
'pp_hh01j_5f_HT_8800_100000':['gluon fusion di-higgs + 0/1 jets','8800 < HT < 100000','xqcut = 60, qCut = 90','2.703e-06','3.87','0.413'],
'pp_hh01j_5f':['gluon fusion di-higgs + 0/1 jets','inclusive','xqcut = 60, qCut = 90','1.113','3.87','0.413'],
'pp_ttv01j_5f_HT_0_1100':['top pair + boson + 0/1 jets','0 < HT < 1100','xqcut = 80, qCut = 120','222','1.14','0.537'],
'pp_ttv01j_5f_HT_1100_2700':['top pair + boson + 0/1 jets','1100 < HT < 2700','xqcut = 80, qCut = 120','32.88','1.14','0.657'],
'pp_ttv01j_5f_HT_2700_4900':['top pair + boson + 0/1 jets','2700 < HT < 4900','xqcut = 80, qCut = 120','2.163','1.14','0.706'],
'pp_ttv01j_5f_HT_4900_8100':['top pair + boson + 0/1 jets','4900 < HT < 8100','xqcut = 80, qCut = 120','0.2143','1.14','0.73'],
'pp_ttv01j_5f_HT_8100_100000':['top pair + boson + 0/1 jets','8100 < HT < 100000','xqcut = 80, qCut = 120','0.02413','1.14','0.744'],
'pp_ttv01j_5f':['top pair + boson + 0/1 jets','inclusive','xqcut = 80, qCut = 120','258.3','1.14','0.553'],
'pp_ll012j_5f_HT_0_200':['V -> ll (l=e,mu,ve,vm,vt) + ','0 < HT < 200','xqcut = 30, qCut = 45','1.158e+04','1.20','0.85'],
'pp_ll012j_5f_HT_200_700':['V -> ll (l=e,mu,ve,vm,vt) + ','200 < HT < 700','xqcut = 30, qCut = 45','717.3','1.20','0.464'],
'pp_ll012j_5f_HT_700_1500':['V -> ll (l=e,mu,ve,vm,vt) + ','700 < HT < 1500','xqcut = 30, qCut = 45','37.04','1.20','0.448'],
'pp_ll012j_5f_HT_1500_2700':['V -> ll (l=e,mu,ve,vm,vt) + ','1500 < HT < 2700','xqcut = 30, qCut = 45','3.723','1.20','0.449'],
'pp_ll012j_5f_HT_2700_4200':['V -> ll (l=e,mu,ve,vm,vt) + ','2700 < HT < 4200','xqcut = 30, qCut = 45','0.4862','1.20','0.45'],
'pp_ll012j_5f_HT_4200_8000':['V -> ll (l=e,mu,ve,vm,vt) + ','4200 < HT < 8000','xqcut = 30, qCut = 45','0.1125','1.20','0.441'],
'pp_ll012j_5f_HT_8000_15000':['V -> ll (l=e,mu,ve,vm,vt) + ','8000 < HT < 15000','xqcut = 30, qCut = 45','0.008175','1.20','0.424'],
'pp_ll012j_5f_HT_15000_25000':['V -> ll (l=e,mu,ve,vm,vt) + ','15000 < HT < 25000','xqcut = 30, qCut = 45','0.000314','1.20','0.429'],
'pp_ll012j_5f_HT_25000_35000':['V -> ll (l=e,mu,ve,vm,vt) + ','25000 < HT < 35000','xqcut = 30, qCut = 45','8.832e-06','1.20','0.473'],
'pp_ll012j_5f_HT_35000_100000':['V -> ll (l=e,mu,ve,vm,vt) + ','35000 < HT < 100000','xqcut = 30, qCut = 45','4.069e-07','1.20','0.509'],
'pp_ll012j_5f':['V -> ll (l=e,mu,ve,vm,vt) + ','inclusive','xqcut = 30, qCut = 45','1.235e+04','1.20','0.83'],
'pp_aa012j_5f_HT_0_500':['di-photon + 0/1/2 jets','0 < HT < 500','xqcut = 20, qCut = 30','6919','2.0','0.302'],
'pp_aa012j_5f_HT_500_1000':['di-photon + 0/1/2 jets','500 < HT < 1000','xqcut = 20, qCut = 30','88.64','2.0','0.612'],
'pp_aa012j_5f_HT_1000_2000':['di-photon + 0/1/2 jets','1000 < HT < 2000','xqcut = 20, qCut = 30','13.72','2.0','0.659'],
'pp_aa012j_5f_HT_2000_4000':['di-photon + 0/1/2 jets','2000 < HT < 4000','xqcut = 20, qCut = 30','1.424','2.0','0.679'],
'pp_aa012j_5f_HT_4000_7200':['di-photon + 0/1/2 jets','4000 < HT < 7200','xqcut = 20, qCut = 30','0.01786','2.0','0.446'],
'pp_aa012j_5f_HT_7200_100000':['di-photon + 0/1/2 jets','7200 < HT < 100000','xqcut = 20, qCut = 30','4.859e-05','2.0','0.151'],
'pp_aa012j_5f':['di-photon + 0/1/2 jets','inclusive','xqcut = 20, qCut = 30','7030','2.0','0.307'],
'pp_aj012j_5f_HT_0_500':['photon + jet + 0/1/2 jets','0 < HT < 500','xqcut = 20, qCut = 30','6.722e+06','1.0','0.132'],
'pp_aj012j_5f_HT_500_1000':['photon + jet + 0/1/2 jets','500 < HT < 1000','xqcut = 20, qCut = 30','3.222e+04','1.0','0.266'],
'pp_aj012j_5f_HT_1000_2000':['photon + jet + 0/1/2 jets','1000 < HT < 2000','xqcut = 20, qCut = 30','4045','1.0','0.26'],
'pp_aj012j_5f_HT_2000_4000':['photon + jet + 0/1/2 jets','2000 < HT < 4000','xqcut = 20, qCut = 30','399','1.0','0.257'],
'pp_aj012j_5f_HT_4000_7200':['photon + jet + 0/1/2 jets','4000 < HT < 7200','xqcut = 20, qCut = 30','14.68','1.0','0.253'],
'pp_aj012j_5f_HT_7200_100000':['photon + jet + 0/1/2 jets','7200 < HT < 100000','xqcut = 20, qCut = 30','0.467','1.0','0.231'],
'pp_aj012j_5f':['photon + jet + 0/1/2 jets','inclusive','xqcut = 20, qCut = 30','6.759e+06','1.0','0.132'],
'pp_h012j_5f_HT_0_100':['gluon fusion higgs (finite mt) + 0/1/2 jets','0 < HT < 100','xqcut = 30, qCut = 45','312.9','3.76','0.403'],
'pp_h012j_5f_HT_100_400':['gluon fusion higgs (finite mt) + 0/1/2 jets','100 < HT < 400','xqcut = 30, qCut = 45','220.4','3.76','0.317'],
'pp_h012j_5f_HT_400_1000':['gluon fusion higgs (finite mt) + 0/1/2 jets','400 < HT < 1000','xqcut = 30, qCut = 45','47.28','3.76','0.312'],
'pp_h012j_5f_HT_1000_1900':['gluon fusion higgs (finite mt) + 0/1/2 jets','1000 < HT < 1900','xqcut = 30, qCut = 45','3.587','3.76','0.31'],
'pp_h012j_5f_HT_1900_4400':['gluon fusion higgs (finite mt) + 0/1/2 jets','1900 < HT < 4400','xqcut = 30, qCut = 45','0.277','3.76','0.296'],
'pp_h012j_5f_HT_4400_8500':['gluon fusion higgs (finite mt) + 0/1/2 jets','4400 < HT < 8500','xqcut = 30, qCut = 45','0.003902','3.76','0.275'],
'pp_h012j_5f_HT_8500_100000':['gluon fusion higgs (finite mt) + 0/1/2 jets','8500 < HT < 100000','xqcut = 30, qCut = 45','6.368e-05','3.76','0.28'],
'pp_h012j_5f':['gluon fusion higgs (finite mt) + 0/1/2 jets','inclusive','xqcut = 30, qCut = 45','587.5','3.76','0.364'],
'pp_vvv01j_5f_HT_0_1200':['tri-vector boson + 0/1 jets','0 < HT < 1200','xqcut = 60, qCut = 90','73.04','1.05','0.515'],
'pp_vvv01j_5f_HT_1200_3000':['tri-vector boson + 0/1 jets','1200 < HT < 3000','xqcut = 60, qCut = 90','2.093','1.05','0.838'],
'pp_vvv01j_5f_HT_3000_6000':['tri-vector boson + 0/1 jets','3000 < HT < 6000','xqcut = 60, qCut = 90','0.2028','1.05','0.872'],
'pp_vvv01j_5f_HT_6000_100000':['tri-vector boson + 0/1 jets','6000 < HT < 100000','xqcut = 60, qCut = 90','0.02111','1.05','0.893'],
'pp_vvv01j_5f':['tri-vector boson + 0/1 jets','inclusive','xqcut = 60, qCut = 90','75.87','1.05','0.525'],
#DM signals Caterina Doglioni
'pp_DMSimp_V_jj_gq0p25_gdm1p00_mDM0p01_mMed30p00':['30TeV DM mediator','di-jet','','1','1','1.0'],
}
