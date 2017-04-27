import pymel.core as pm 
def yes_no(title, message):
    return confirm(title, message, 'Yes', 'No')


def ok_cancel(title, message='Do you OK?'):
    return confirm(title, message, 'OK', 'Cancel')


def confirm(title, message, button_ok, button_ng):
    return pm.windows.confirmDialog(
        title=title, message=message, button=[button_ok, button_ng],
        defaultButton=button_ok, cancelButton=button_ng, dismissString=button_ng,
    ) == button_ok
