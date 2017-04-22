import os
from os import path
from maya import cmds, mel


def find_workspace(f):
    d = path.dirname(f)
    if d == f:
        return None  # f is root dir

    if 'workspace.mel' not in os.listdir(d):
        return find_workspace(d)

    # Because maya's workspace command returns value with suffix '/', append '/' to return value. 
    return d + '/' 

def set_workspace(ws):
    mel.eval('setProject "{}";'.format(ws))


def suggest_workspace():
    f = cmds.file(q=True, sceneName=True)
    if f == '':
        return  # New scene

    ws = find_workspace(f) 
    if ws == cmds.workspace(q=True, rootDirectory=True):
        return 

    ws_name = path.basename(ws[:-1])  # Dont pass last '/' to basename
    message = 'Do you want to switch workspace to "{}"?'.format(ws_name)
    if cmds.confirmDialog(title='Workspace Suggestion', message=message, button=['Yes','No'],
                          defaultButton='Yes', cancelButton='No') == 'Yes':
        set_workspace(ws)

def activate_suggestion(event='SceneOpened'):
    cmds.scriptJob(event=[event, suggest_workspace])
