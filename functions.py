from psychopy import gui

def sub_id():
    myDlg = gui.Dlg(title="SFB_289")
    myDlg.addField('Subject ID:')
    myDlg.addField('mzp:', )
    ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
    if myDlg.OK:  # or if ok_data is not None
        print(ok_data)
    else:
        print('user cancelled')
    return ok_data


def randomlist():
    bio = [1, 2, 3, 4, 5,  6]
    psych = [ 7, 8, 9, 10, 11, 12]
    return bio, psych

def quiz_bio():
    myDlgbio = gui.Dlg(title="Quiz")
    myDlgbio.addField('Frage 1:', choices =["A1", "A2", "A3", "A4"])
    myDlgbio.addField('Frage 2:', choices =["A1", "A2", "A3", "A4"])
    myDlgbio.addField('Frage 3:', choices=["A1", "A2", "A3", "A4"])
    myDlgbio.addField('Frage 4:', choices=["A1", "A2", "A3", "A4"])
    ok_databio = myDlgbio.show()  # show dialog and wait for OK or Cancel
    if myDlgbio.OK:  # or if ok_data is not None
        print(ok_databio)
    else:
        print('user cancelled')
    return ok_databio

def quiz_psych():
    myDlgpsych = gui.Dlg(title="Quiz")
    myDlgpsych.addField('Frage 1:', choices=["A1", "A2", "A3", "A4"])
    myDlgpsych.addField('Frage 2:', choices=["A1", "A2", "A3", "A4"])
    myDlgpsych.addField('Frage 3:', choices=["A1", "A2", "A3", "A4"])
    myDlgpsych.addField('Frage 4:', choices=["A1", "A2", "A3", "A4"])
    ok_datapsych = myDlgpsych.show()  # show dialog and wait for OK or Cancel
    if myDlgpsych.OK:  # or if ok_data is not None
        print(ok_datapsych)
    else:
        print('user cancelled')
    return ok_datapsych