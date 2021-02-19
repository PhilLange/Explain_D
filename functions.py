from psychopy import gui


# 1) create subject lists
def randomlist():
    bio = [1, 2, 3, 4, 5,  6]
    psych = [7, 8, 9, 10, 11, 12]
    return bio, psych

# 2) Initialize the gui windows, they well be updated later
# define gui
myDlg = gui.Dlg(title="SFB_289")
myDlgbio = gui.Dlg(title="Quiz")
myDlgpsych = gui.Dlg(title="Quiz")


# 3) Adapt gui widows accordingly
def sub_id():
    myDlg.addField('Subject ID:')
    myDlg.addField('mzp:', )
    ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
    if myDlg.OK:  # or if ok_data is not None
        print(ok_data)
    else:
        print('user cancelled')
    return ok_data


def quiz_bio():
    myDlgbio.addField('Frage 1:', choices =["A1", "A2", "A3", "A4"])
    myDlgbio.addField('Frage 2:', choices =["A1", "A2", "A3", "A4"])
    myDlgbio.addField('Frage 3:', choices=["A1", "A2", "A3", "A4"])
    myDlgbio.addField('Frage 4:', choices=["A1", "A2", "A3", "A4"])

    # show dialog and wait for OK or Cancel
    ok_databio = myDlgbio.show()

    # or if ok_data is not None
    if myDlgbio.OK:
        print(ok_databio)
    else:
        print('user cancelled')
    return ok_databio


def quiz_psych():
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
    return ok_datapsych
