import datetime
from ahk import AHK

def re_rename():
    ahk.key_press('F2')

def revit_default_option():
    ahk.key_press('TAB')
    ahk.key_press('TAB')
    ahk.key_press('ENTER')
    ahk.key_press('TAB')
    ahk.key_press('TAB')
    ahk.key_press('ENTER')

def deltek_ts():
    ahk.send_input(f"{datetime.datetime.now():%m-%d-%Y}  - CWS")
    for _ in range(6):
        ahk.key_press('LEFT')

ahk = AHK()

ahk.add_hotkey('!ENTER', callback=re_rename)
ahk.add_hotkey('^g', callback=revit_default_option)
ahk.add_hotstring('!dts', deltek_ts, options='*') 
ahk.start_hotkeys()
ahk.block_forever()
