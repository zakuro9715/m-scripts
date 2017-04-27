import os
from os import path
from maya import cmds, mel


def current():
    return cmds.workspace(q=True, fullName=True)


def set_current(ws):
    mel.eval('setProject "{}";'.format(ws))


def find_for(f):
    d = path.dirname(f)
    if d == f:
        return None  # f is root dir

    if 'workspace.mel' not in os.listdir(d):
        return find_for(d)

    # Because maya's workspace command returns value with suffix '/', append '/' to return value. 
    return d + '/' 
