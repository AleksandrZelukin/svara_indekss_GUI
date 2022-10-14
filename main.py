from cgitb import text
from curses import window
from datetime import date
import PySimpleGUI as sg
import sqlite3

conn = sqlite3.connect(r'veseliba.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   vards TEXT,
   uzvards TEXT,
   dzimsanas datums TEXT,
   augums TEXT,
   svars TEXT,
   bmi TEXT);
""")
conn.commit()
# https://pythonru.com/osnovy/sqlite-v-python
#https://pythobyte.com/python-sqlite3-tutorial-database-programming-riqdhwx9z-fafd14f8/

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




menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],    
           ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'],],            ['Help', 'About...'], ]      
layot = [[sg.Menu(menu_def, tearoff=True)],
        [sg.Text("Vārds"), sg.InputText (size=(25,1))],
        [sg.Text("Uzvārd"), sg.InputText (size=(25,1))],
        [sg.Text("dzinšanas datums"), sg.InputText('dd,mm,gggg',size=(25,1))],
        [sg.Text("Augums"), sg.InputText (size=(25,1))],
        [sg.Text("Svars"), sg.InputText(size=(25,1))],
        [sg.Button("aprēķināt BMI", key='submit')],
        [sg.Text('', key='bmi', size=(20,2))],
        [sg.Text('', key='radit',size=(20,2))],
        [sg.Button("Saglabāt datus", key='glab'),sg.Button("Beigt", key='q')]]

window = sg.Window ("Calculator BMI", layot)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'q':
      print(values[1],values[2],bmi)
      break
    if event == 'submit':
      bmi = calc_bmi(values[4], values[5])
      window['bmi'].update (bmi)
    if event == 'glab':
      window['radit'].update('dati saglabāti')
      cur.execute("""INSERT INTO users(userid, vards, uzvards, dzimsanas datums, augums, svars, bmi) 
   VALUES(values[0], values[1], values[2], values[3], values[4], values[5],bmi);""")
conn.commit()
window.close()