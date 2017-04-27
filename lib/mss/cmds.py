from os import path

import pymel.core as pm
from maya.cmds import scriptJob
from mss.lib import ui, scene, ws


__all__ = ['hello_mss', 'suggest_ws', 'activate_ws_suggestion']


def hello_mss():
    return 'Hello m-scripts'


def suggest_ws():
    f = scene.current()
    if f == '':
        return  # New scene

    new_ws = ws.find_for(f) 
    if new_ws == ws.current():
        return 

    ws_name = path.basename(new_ws[:-1])  # Dont pass last '/' to basename
    message = 'Do you want to switch workspace to "{}"?'.format(ws_name)
    if ui.yes_no('Workspace Suggestion', message):
        ws.set_current(new_ws)


def activate_ws_suggestion(event='SceneOpened'):
    scriptJob(event=[event, suggest_ws])
