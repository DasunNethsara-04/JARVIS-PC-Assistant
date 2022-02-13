#-------------------------------------------------------------------------------
# Name:        Pomodoro Timer
# Purpose:     Just for fun
# Author:      Dasun Nethsara
# Created:     01/02/2022
# Copyright:   (c) Dasun Nethsara 2022
# Licence:     Open source - free software
#-------------------------------------------------------------------------------

#imports
import time
import threading
from tkinter import *
from tkinter import ttk


class Timer:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x300')
        self.root.title('Pomodoro Timer')
        #self.root.config(bg='#303841')
        self.img = PhotoImage(file='logo.png')
        self.root.iconphoto(False, self.img)
        self.root.resizable(False, False)

        self.s = ttk.Style()
        self.s.configure('TNotebook.Tab', font=('Calibri', 16))
        self.s.configure('TButton', font=('Calibri', 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill=BOTH, pady=5, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='Short Break')
        self.tabs.add(self.tab3, text='Long Break')

        self.timer_lbl = ttk.Label(self.tab1, text='25:00', font=('DS-Digital', 70))
        self.timer_lbl.pack(pady=20)

        self.shortBreak_lbl = ttk.Label(self.tab2, text='05:00', font=('DS-Digital', 70))
        self.shortBreak_lbl.pack(pady=20)

        self.longBreak_lbl = ttk.Label(self.tab3, text='15:00', font=('DS-Digital', 70))
        self.longBreak_lbl.pack(pady=20)

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.start_btn = ttk.Button(self.grid_layout, text='Start', command=self.start_timer_thread)
        self.start_btn.grid(row=0, column=0)

        self.skip_btn = ttk.Button(self.grid_layout, text='Skip', command=self.skip_clock)
        self.skip_btn.grid(row=0, column=1)

        self.reset_btn = ttk.Button(self.grid_layout, text='Reset', command=self.reset_clock)
        self.reset_btn.grid(row=0, column=2)

        self.counter_lbl = ttk.Label(self.grid_layout, text='Pomodoros: 0', font=('Calibri', 16))
        self.counter_lbl.grid(row=1, column=0, columnspan=3, pady=10)


        self.pomodoros = 0
        self.skipped = False
        self.stopped = False
        self.running = False



        self.root.mainloop()


    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_second = 60 * 25
            while full_second > 0 and not self.stopped:
                minutes, seconds = divmod(full_second, 60)
                self.timer_lbl.config(text=f'{minutes:02d}:{seconds:02d}')
                self.root.update()
                time.sleep(1)
                full_second -= 1

            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.counter_lbl.config(text=f'Pomodoros: {self.pomodoros}')
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                else:
                    self.tabs.select(1)
                self.start_timer()

        elif timer_id == 2:
            full_second = 60 * 5
            while full_second > 0 and not self.stopped:
                minutes, seconds = divmod(full_second, 60)
                self.shortBreak_lbl.config(text=f'{minutes:02d}:{seconds:02d}')
                self.root.update()
                time.sleep(1)
                full_second -= 1

            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()

        elif timer_id == 3:
            full_second = 60 * 15
            while full_second > 0 and not self.stopped:
                minutes, seconds = divmod(full_second, 60)
                self.longBreak_lbl.config(text=f'{minutes:02d}:{seconds:02d}')
                self.root.update()
                time.sleep(1)
                full_second -= 1

            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()

        else:
            print('Invalid timer id')

    def reset_clock(self):
        self.stopped = True
        self.skipped = False
        self.pomodoros = 0
        self.timer_lbl.config(text='25:00')
        self.shortBreak_lbl.config(text='05:00')
        self.longBreak_lbl.config(text='15:00')
        self.counter_lbl.config(text='Pomodoros: 0')
        self.running = False

    def skip_clock(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.timer_lbl.config(text='25:00')
        elif current_tab == 1:
            self.shortBreak_lbl.config(text='05:00')
        elif current_tab == 2:
            self.longBreak_lbl.config(text='15:00')

        self.stopped = True
        self.skipped = True



Timer()
