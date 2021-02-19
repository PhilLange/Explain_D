from psychopy import gui


# 1) create subject lists
def randomlist():
    bio = [1, 2, 3, 4, 5,  6]
    psych = [7, 8, 9, 10, 11, 12]
    return bio, psych


# 3) Adapt gui widows accordingly
def sub_id():
    myDlg = gui.Dlg(title="SFB_289")
    myDlg.addField('Subject ID:')
    myDlg.addField('mzp:')

    # show dialog box and wait for subject input,
    # then OK or Cancel
    ok_data = myDlg.show()

    # if OK pressed show data, otherwise cancel
    if myDlg.OK:
        print(ok_data)
    else:
        print('user cancelled')

    # clean up
    del myDlg

    return ok_data


def quiz_bio():
    myDlgbio = gui.Dlg(title="Quiz")
    myDlgbio.addField('Frage 1:', choices=["A1", "A2", "A3", "A4"])
    myDlgbio.addField('Frage 2:', choices=["A1", "A2", "A3", "A4"])
    myDlgbio.addField('Frage 3:', choices=["A1", "A2", "A3", "A4"])
    myDlgbio.addField('Frage 4:', choices=["A1", "A2", "A3", "A4"])

    # show dialog box and wait for subject input,
    # then OK or Cancel
    ok_databio = myDlgbio.show()

    # if OK pressed show data, otherwise cancel
    if myDlgbio.OK:
        print(ok_databio)
    else:
        print('user cancelled')

    # clean up
    del myDlgbio

    return ok_databio


def quiz_psych():
    myDlgpsych = gui.Dlg(title="Quiz")
    myDlgpsych.addField('Frage 1:', choices=["A1", "A2", "A3", "A4"])
    myDlgpsych.addField('Frage 2:', choices=["A1", "A2", "A3", "A4"])
    myDlgpsych.addField('Frage 3:', choices=["A1", "A2", "A3", "A4"])
    myDlgpsych.addField('Frage 4:', choices=["A1", "A2", "A3", "A4"])

    # show dialog and wait for OK or Cancel
    ok_datapsych = myDlgpsych.show()

    # or if ok_data is not None
    if myDlgpsych.OK:
        print(ok_datapsych)
    else:
        print('user cancelled')

    # clean up
    del myDlgpsych

    return ok_datapsych
