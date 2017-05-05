import json
import sys
def testopenjson(dic):
    with open(dic,'r') as f:
        try:
            readf = json.load(f)
            print '\033[91m ----Local dictionnary succesfully loaded----  \033[0m'
        except ValueError:
            print '\033[91m ----Local dictionnary is corrupted, can not be opened----  \033[0m'
            print '\033[91m ----Please contact clement.helsens@cern.ch or michele.selvaggi@cern.ch---- \033[0m'
            return

#__________________________________________________________
if __name__=="__main__":

    if len(sys.argv)==2:
        testopenjson(sys.argv[1])
    else:
        print 'usage: python testopen.py <dic>'
