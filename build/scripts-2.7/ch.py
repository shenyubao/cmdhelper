#!/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python

import sys
sys.path.append('/Projects/python/cmdhelper')
from src.cmdhelper.CmdHelper import *

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 1:
        parser.print_help()
        exit()

    #args[0] = 'get'
    #args[1] = 'db.pro'
    #args[2] = '127.0.0.2'

    cmdHelper = CmdHelper()
    if(args[1] == "list"):
        cmdHelper.list()

    if(args[1] == "get"):
        if(len(args) < 2):
            cmdHelper.list()
            exit()
        cmdHelper.get(args[2])

    if(args[1] == "del"):
        cmdHelper.delete(args[2])

    if(args[1] == "set"):
        cmdHelper.set(args[2]," ".join(args[3:]))

    exit()




















