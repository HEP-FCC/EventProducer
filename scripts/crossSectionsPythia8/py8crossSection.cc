/*
To compile:

./init.sh

*/

#include "Pythia8/Pythia.h"
#include <ios>
#include <fstream>

using namespace Pythia8;

//==========================================================================

int main(int argc, char** argv) {

  if (argc != 3) {
      cout <<"Usage: ./py8crossSection.exe [pythia.cmd] [outputParamFile]" <<endl;
      return 0;
  }

  // Generator. Shorthand for the event.
  Pythia pythia;

  // Read in commands from external file.

  pythia.readFile(argv[1]);

  // Extract settings to be used in the main program.
  int    nEvent    = pythia.mode("Main:numberOfEvents");
  int    nAbort    = pythia.mode("Main:timesAllowErrors");

  // Initialize.
  pythia.init();

  // Begin event loop.
  int iAbort = 0;
  for (int iEvent = 0; iEvent < nEvent; ++iEvent) {

    // Generate events. Quit if too many failures.
    if (!pythia.next()) {
      if (++iAbort < nAbort) continue;
      cout << " Event generation aborted prematurely, owing to error!\n";
      break;
    }
  }

  // convert mb to pb
  float xsec = pythia.info.sigmaGen() * 1.e09;

  cout<<"------------------------------------------------------------------------"<<endl;
  cout<<""<<endl;
  cout<<"Cross-section: "<<xsec<<" pb"<<endl;
  cout<<""<<endl;

  // chop off extension from pythia file name 
  string cmdFile(argv[1]);
  size_t lastindex = cmdFile.find_last_of("."); 
  string procName = cmdFile.substr(0, lastindex); 


  string paramFile(argv[2]);

  std::ofstream param(paramFile, std::ios_base::app | std::ios_base::out);
  param << "'"<<procName<<"':['','','','"<<xsec<<"','1.0','1.0'],\n";

  // Done.
  return 0;

}
