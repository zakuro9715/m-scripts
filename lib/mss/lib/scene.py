from maya import cmds

def current():
    return cmds.file(q=True, sceneName=True)
