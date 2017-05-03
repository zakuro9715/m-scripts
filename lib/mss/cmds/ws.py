from os import path

import pymel.core as pm
from maya.cmds import scriptJob
from mss.lib import ui, scene, ws


__all__ = ['suggest_ws', 'activate_ws_suggestion']


def suggest_ws():
    f = scene.current()
    if f == '':
        return  # New scene

    new_ws = ws.find_for(f) 
    if new_ws == ws.current():
        return 
   # return (new_ws, ws.current())

    ws_name = path.basename(new_ws)
    message = 'Do you want to switch workspace to "{}"?'.format(ws_name)
    if ui.yes_no('Workspace Suggestion', message):
        ws.set_current(new_ws)


def activate_ws_suggestion(event='SceneOpened'):
    scriptJob(event=[event, suggest_ws])
