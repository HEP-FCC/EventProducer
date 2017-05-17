#!/usr/bin/env python

#################################################################################
#
#  this script produces validation plots for the HT binning procedure
#  to run it :
#
#  python validateHtBinning.py -p [process] -n [nevents]
#
#  e. g
#
#  python validateHtBinning.py -p pp_h012j_5f -n 100000
#
##################################################################################

from __future__ import division
import sys
import ROOT
import math
from LHEevent import *
from LHEfile import *
import EventProducer.config.param as para
import json
import ntpath
import os
import argparse

eos = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select'

#______________________________________________________________________________
def create_parser(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--process", type=str, default='.', help="process to validate")
    parser.add_argument("-n", "--nevents", type=int, default='1000', help="number of events")
    return parser

#__________________________________________________________
def main(parser):    

    options  = parser.parse_args()

    process = options.process
    nEventsMax = options.nevents
    
    #processName = '{}_HT'.format(process)
    processName = process
    
    lhe = para.lhe_dic
    lheDict=None
    with open(lhe) as f:
        lheDict = json.load(f)

    htLin = ROOT.TH1D("htLin", "htLin",100, 0., 30000.)
    htLog = ROOT.TH1D("htLog", "htLog",100, 2., 5.)
           
    htLin.GetXaxis().SetTitle("H_{T} [GeV]")
    htLin.GetYaxis().SetTitle("a.u.")

    htLog.GetXaxis().SetTitle("log H_{T}")
    htLog.GetYaxis().SetTitle("a.u.")

    histoFILE = ROOT.TFile('{}.root'.format(process),"RECREATE")
    
    htLinBin = {}
    htLogBin = {}
    
    histosLin = []
    histosLog = []
    
    legLin = ROOT.TLegend(0.60,0.60,0.93,0.88)
    legLin.SetFillColor(0)
    legLin.SetFillStyle(0)
    legLin.SetLineColor(0)
    
    legLog = legLin.Clone()
    
    index = 0
    for proc in para.gridpacklist:
        
        # loop over bins
        if processName in proc:
            
            nlhe = 0
            xsec = float(para.gridpacklist[proc][3])
            
            htLinBin[proc] = htLin.Clone()
            htLogBin[proc] = htLog.Clone()
            
            htLinBin[proc].Reset()
            htLogBin[proc].Reset()
            
            if len(proc.split('HT')) > 1:
	        htstring = proc.split('HT')[1]
                htmin = htstring.split('_')[1]
                htmax = htstring.split('_')[2]
                nMax = nEventsMax
	    else:
	        htstring = ''
	        htmin = ''
                htmax = ''
	        nMax = nEventsMax*100
		inc_id = index
	    
            htLinBin[proc].SetName("htLin{}".format(htstring))
            htLogBin[proc].SetName("htLog{}".format(htstring))
            
            htLinBin[proc].SetTitle('{} < H_{{T}} < {}'.format(htmin, htmax))
            htLogBin[proc].SetTitle('{} < H_{{T}} < {}'.format(htmin, htmax))
            
            # loop over lhe file for given bin
            for joblhe in lheDict[proc]:
                if joblhe['status']== 'done':
                    nlhe += int(joblhe['nevents'])
                    eoslhe = joblhe['out']
                    eoslhebase = ntpath.basename(eoslhe)
                    lhename = os.path.splitext(eoslhebase)[0]
                    if os.path.isfile(lhename):
                        os.system('/bin/rm {}'.format(lhename))
                    os.system('{} cp {} {}'.format(eos, eoslhe, eoslhebase))
                    os.system('/bin/gunzip {}'.format(eoslhebase))
                    fillHtHistos(lhename, htLinBin[proc], htLogBin[proc])
                    os.system('/bin/rm {}'.format(lhename))
                    		    
                    if nlhe >= nMax:
                        break

            htLinBin[proc].Scale(xsec/nlhe)
            htLogBin[proc].Scale(xsec/nlhe)
            
            histosLin.append(htLinBin[proc])
            histosLog.append(htLogBin[proc])

            htLinBin[proc].Write()
            htLogBin[proc].Write()

            index +=1

    htLin = histosLin[inc_id].Clone()
    htLog = histosLog[inc_id].Clone()

    del histosLin[inc_id]
    del histosLog[inc_id]

    histosLin.sort(key=lambda x: x.GetMean())
    histosLog.sort(key=lambda x: x.GetMean())

    for h in histosLin:
       legLin.AddEntry(h, h.GetTitle(),"f")
    for h in histosLog:
       legLog.AddEntry(h, h.GetTitle(),"f")

    htLin.Write()
    htLog.Write()
    
    legLin.AddEntry(htLin, 'inclusive',"l")
    legLog.AddEntry(htLog, 'inclusive',"l")
    
    drawMultiHisto('{}_lin'.format(process), legLin, 'png', [htLin] + histosLin)
    drawMultiHisto('{}_log'.format(process), legLog, 'png', [htLog] + histosLog)

#__________________________________________________________
def fillHtHistos(lheFile, htLin, htLog):

    myLHEfile = LHEfile(lheFile)
    myLHEfile.setMax(99999)
    eventsReadIn = myLHEfile.readEvents()

    for oneEvent in eventsReadIn:
        # read the event content
        myLHEevent = LHEevent()
        
        myLHEevent.fillEvent(oneEvent)
        
        ht = 0.0
        for i in range(0,len(myLHEevent.Particles)):
            p = myLHEevent.Particles[i]
            
            if p['Status'] == 1: 
               ht += math.sqrt(p['Px']**2 + p['Py']**2)
        
        if ht > 1.0:
            htLin.Fill(ht)
            htLog.Fill(math.log10(ht))

#__________________________________________________________
def printCanvas(canvas, name, format):
    if format != "":
        outFile = name + "." + format
        canvas.Print(outFile)

#__________________________________________________________
def drawMultiHisto(name, legend, format, histos):
    
    canvas = ROOT.TCanvas(name, name, 800, 600) 
    canvas.SetLogy(1)

    # define font (TNR)
    font = 132

    # style for this canvas
    ROOT.gPad.SetLeftMargin(0.20)
    ROOT.gPad.SetRightMargin(0.10)
    ROOT.gPad.SetBottomMargin(0.20)
    ROOT.gStyle.SetOptStat(0000000)
    ROOT.gStyle.SetTextFont(font)    

    # define colors
    colors = []
    colors.append(ROOT.kBlue);
    colors.append(ROOT.kCyan);
    colors.append(ROOT.kGreen+1);
    colors.append(ROOT.kOrange);
    colors.append(ROOT.kRed);
    colors.append(ROOT.kMagenta);
    colors.append(ROOT.kOrange-6);

    # define stacked histo
    hStack = ROOT.THStack("hstack","")
 
    # first retrieve maximum
    maxes = []
    for h in histos:
       maxes.append(h.GetMaximum())
    maxh = max(maxes)

    histos[1].SetLineWidth(0)
    histos[1].SetFillColor(colors[0])
    
    hStack.Add(histos[1])

    # now loop over other bins (skipping first)
    iterh = iter(histos)
    next(iterh)
    next(iterh)
    
    k = 1
    for h in iterh:
       h.SetLineWidth(0)
       h.SetFillColor(colors[k])
       hStack.Add(h)
       k += 1
  
    # finally add signal on top
    histos[0].SetLineWidth(3)
    histos[0].SetLineColor(ROOT.kBlack)

    hStack.Draw("hist")

    # setup and draw first histogram 
    hStack.GetXaxis().SetTitleFont(font)
    hStack.GetXaxis().SetLabelFont(font)
    hStack.GetYaxis().SetTitleFont(font)
    hStack.GetYaxis().SetLabelFont(font)
    hStack.GetXaxis().SetTitleOffset(1.5)
    hStack.GetYaxis().SetTitleOffset(1.6)
    hStack.GetXaxis().SetLabelOffset(0.02)
    hStack.GetYaxis().SetLabelOffset(0.02)
    hStack.GetXaxis().SetTitleSize(0.06)
    hStack.GetYaxis().SetTitleSize(0.06)
    hStack.GetXaxis().SetLabelSize(0.06)
    hStack.GetYaxis().SetLabelSize(0.06)
    hStack.GetXaxis().SetNdivisions(505);
    hStack.GetYaxis().SetNdivisions(505);
    hStack.GetXaxis().SetTitle(histos[0].GetXaxis().GetTitle());
    hStack.GetYaxis().SetTitle(histos[0].GetYaxis().GetTitle());
   
    hStack.SetMaximum(1e+3*maxh) 
    hStack.SetMinimum(1e-9*maxh) 
    hStack.SetTitle("") 

    # re-draw first histo 
    histos[0].Draw("same hist")

    # draw legend and text
    legend.SetTextFont(font) 
    legend.Draw() 

    # print histogram to file
    printCanvas(canvas, name, format) 

#______________________________________________________________________________
if __name__ == '__main__':
    parser = create_parser()
    main(parser)

