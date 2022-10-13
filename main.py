from cgitb import text
from curses import window
import PySimpleGUI as sg
def calc_bmi(h,w):
    try:
        h, w = float(h), float(w)
        bmi = round(w / h **2, 1)
        if bmi < 18.5:
            standard = "Extra vājš"
        elif 18.5 <= bmi <= 23.9:
            standard = "Normāl"
        elif 24.0 <= bmi <= 27.9:
            standard = "lieks svars"
        else:
            standard = "trekns"
    except (ValueError, ZeroDivisionError):
        return None
    else:
        return (f'BMI: {bmi}, {standard}')

layot = [[sg.Text("Vārds"), sg.InputText (size=(25,1))],
        [sg.Text("Uzvārd"), sg.InputText (size=(25,1))],
        [sg.Text("dzinšanas datums"), sg.InputText ('dd,mm,gggg',size=(25,1))],
        [sg.Text("Augums"), sg.InputText (size=(25,1))],
        [sg.Text("Svars"), sg.InputText(size=(25,1))],
        [sg.Button("aprēķināt BMI", key='submit')],
        [sg.Text('', key='bmi', size=(20,2))],
        [sg.Text('', key='radit',size=(20,2))],
        [sg.Button("Saglabat datus", key='glab'),sg.Button("Beigt", key='q')]]

window = sg.Window ("Calculator BMI", layot)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'q':
        break
    if event == 'submit':
        bmi = calc_bmi(values[3], values[4])
        window['bmi'].update (bmi)
    if event == 'glab':
      window['radit'].update('dati saglabati')
window.close()