## imports
from tkinter import *
import psutil
import platform
import os

bgcolor = '#26242f'
fgcolor = 'white'
fgcolor1 = '#15d7e9'

'''
windows - #00ff15
cpu - #ff0000
ram - #fffb00
'''


## functions
def btn():
    path = 'C:\\WINDOWS\\System32\\taskmgr.exe'
    os.startfile(os.path.join(path))

def win():
    sys = platform.system()
    rls = platform.release()
    edition = platform.win32_edition()

    windows.config(text=f'{sys} {rls} {edition}', font=('Consolas', 15, 'bold'))

def cpu_check():
    cpu_data = psutil.cpu_percent()
    cpu.config(text=str(cpu_data)+"%")
    cpu.after(1000, cpu_check)

def ramcheck():
    per_ram = psutil.virtual_memory().percent
    ram.config(text=str(per_ram)+'%')
    ram.after(1000, ramcheck)

def totRam():
    total_ram = round((psutil.virtual_memory().total) / (1024 ** 3), 2)
    tot_ram.config(text=str(total_ram)+'GB (usable)')
    tot_ram.after(1000, totRam)

def useRam():
    used_ram = round((psutil.virtual_memory().used) / (1024 ** 3), 2)
    usd_ram.config(text=str(used_ram)+'GB')
    usd_ram.after(1000, useRam)

def freeRam():
    freeram = round((psutil.virtual_memory().free) / (1024 ** 3), 2)
    free_ram.config(text=str(freeram)+'GB')
    free_ram.after(1000, freeRam)

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

def battery():
    if not hasattr(psutil, "sensors_battery"):
        #return sys.exit("platform not supported")
        btry.config(text='Platform not supported')
    batt = psutil.sensors_battery()
    if batt is None:
        btry.config(text='N/A')
        btry.after(1000, battery)
        #return sys.exit("no battery is installed")
    else:
        btry.config(text=("charge:     %s%%" % round(batt.percent, 2)))
        btry.after(1000, battery)
        #print("charge:     %s%%" % round(batt.percent, 2))


## main ui
root = Tk()
root.title("PC Info")
root.geometry('450x450')
root.iconbitmap('icon.ico')
root.resizable(0, 0)
root.config(bg=bgcolor)

## content
# labels (Indicator Labels)
Label(root, text='PC Info', font=('Consolas', 30, 'bold', 'underline'), bg=bgcolor, fg=fgcolor).pack()
Label(root, text=('System: '), font=('Calibri', 20, 'bold'), bg=bgcolor, fg=fgcolor).place(x=10, y=90)
Label(root, text=('CPU: '), font=('Calibri', 20, 'bold'), bg=bgcolor, fg=fgcolor).place(x=10, y=130)
Label(root, text=('RAM: '), font=('Calibri', 20, 'bold'), bg=bgcolor, fg=fgcolor).place(x=10, y=170)
Label(root, text=('Battery: '), font=('Calibri', 20, 'bold'), bg=bgcolor, fg=fgcolor).place(x=10, y=250)
Label(root, text=('Total RAM: '), font=('Calibri', 20, 'bold'), bg=bgcolor, fg=fgcolor).place(x=10, y=290)
Label(root, text=('Used RAM: '), font=('Calibri', 20, 'bold'), bg=bgcolor, fg=fgcolor).place(x=10, y=330)
Label(root, text=('Free RAM: '), font=('Calibri', 20, 'bold'), bg=bgcolor, fg=fgcolor).place(x=10, y=370)

# labels ( Data Showing Labels)
windows = Label(root, font=('Consolas', 20, 'bold'), bg=bgcolor, fg='#00ff15')
windows.place(x=170, y=90)
cpu = Label(root, font=('Consolas', 20, 'bold'), bg=bgcolor, fg='#ff0000')
cpu.place(x=170, y=130)
ram = Label(root, font=('Consolas', 20, 'bold'), bg=bgcolor, fg='#fffb00')
ram.place(x=170, y=170)
btry = Label(root, font=('Consolas', 20, 'bold'), bg=bgcolor, fg=fgcolor1)
btry.place(x=170, y=250)
tot_ram = Label(root, font=('Consolas', 20, 'bold'), bg=bgcolor, fg=fgcolor1)
tot_ram.place(x=170, y=290)
usd_ram = Label(root, font=('Consolas', 20, 'bold'), bg=bgcolor, fg=fgcolor1)
usd_ram.place(x=170, y=330)
free_ram = Label(root, font=('Consolas', 20, 'bold'), bg=bgcolor, fg=fgcolor1)
free_ram.place(x=170, y=370)


## functions callback
cpu_check()
ramcheck()
totRam()
useRam()
freeRam()
battery()
win()

root.mainloop()
