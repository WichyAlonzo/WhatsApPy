import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
sheet = pd.read_csv("da.csv")
dir = sheet.to_dict('list')
celulares = dir['celular']
mensajes = dir['mensaje']
combo = zip(celulares,mensajes)
first = True
for celular,mensaje in combo:
    time.sleep(2)
    web.open("https://api.whatsapp.com/send/?phone="+celular+"&text="+mensaje)
    if first:
        time.sleep(2)
        first=False
        
    width,height = pg.size()
    time.sleep(2)
    pg.press('enter')
