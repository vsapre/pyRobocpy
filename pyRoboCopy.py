# ========================================================================
# Name:         pyRobocpy
# Purpose:      Automated Backup of important folders
# Author:       Vishal.Sapre
# Created:      03-11-2012
# Copyright:    (c) Vishal.Sapre 2012
# Licence:      MIT License
# ========================================================================
import subprocess as sp
import os
from time import strftime, localtime
from yaml import load

rcCmd = 'robocopy'
src   = 'F:\\'
dst   = 'H:\\'
fOpts = ''
##:: /COPYALL   :: COPY ALL file info
##:: /B         :: copy files in Backup mode (use local user security)
##:: /SEC       :: copy files with SECurity
##:: /MIR       :: MIRror a directory tree
##:: /COPY:DT   :: Copy Data and Timestamp only. No file/security attributes.
wOpts = '/B'
##:: /R:n :: number of Retries
##:: /W:n :: Wait time between retries
##:: /LOG :: Output log file
##:: /NFL :: No file logging
##:: /NDL :: No dir logging
hOpts  = '/R:0 /W:0 /NFL /NDL'
# multi threaded copying, using 16 threads.
mtOpts = '/MT:16'


def runRobocopy(args):
    """
    runs robocopy with the given arguments
    """
    rtask = sp.Popen(args, shell=True)
    rtask.wait()

if __name__ == '__main__':
    sDict = {}
    cfgFile = 'F:\\Projects\\PyProjects\\pyrobocopy_cfg.yaml'
##    cfgFile = 'pyrobocopy_cfg.yaml'
    with open(cfgFile) as fin:
        tasks = load(fin.read())

    for task in tasks:
        t = task['backup']
        if t.has_key('ropts'):
            valueTuple = (t['destin'], t['fTypes'], t['ropts'])
        else:
            valueTuple = (t['destin'], t['fTypes'])

        sDict[t['source']] = valueTuple

    lFileName = 'robocopy_' + strftime('%Y%m%d%I%M%p', localtime()) + '.log'
    folder, fl = os.path.split(__file__)
    #/LOG+:file : Output status to LOG file (append to existing log).
    #/TEE : Output to console window, as well as the log file.
    logOpts = '/LOG+:' + os.path.join(folder, lFileName) + ' /TEE /V'

    for s, v in sDict.items():
        if not os.path.exists(v[0]):
            os.makedirs(v[0])

        fTypeArgs = ' '.join(['*.%s' % t for t in v[1]])
        argList = [rcCmd, s, v[0], fTypeArgs, mtOpts, wOpts, logOpts, hOpts]

        if(len(v) > 2):
            argList.insert(4, v[2])

##        if(len(v) > 2):
##            for t in v[1]:
##                  args = ' '.join([rcCmd, s, v[0], '*.%s' % t, v[2], mtOpts, wOpts, logOpts, hOpts])
##        else:
##            for t in v[1]:
##                args = ' '.join([rcCmd, s, v[0], '*.%s' % t, mtOpts, wOpts, logOpts, hOpts])
        args = ' '.join(argList)
        runRobocopy(args)
