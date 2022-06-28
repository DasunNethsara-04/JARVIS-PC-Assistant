from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *

w = Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_cordinate = (screen_width / 2) - (width_of_window / 2)
y_cordinate = (screen_height / 2) - (height_of_window / 2)

w.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_cordinate, y_cordinate))
w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress = Progressbar(w, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate')    

def bar():
    l4 = Label(w, text="Loading", fg='white', bg="#249794", font=('Calibri', 10))
    l4.place(x=0, y=210)

    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.03)
        r += 1
    w.destroy()

progress.place(x=-10, y=235)

# adding frame
Frame(w, width=427, height=241, bg='#249794').place(x=0, y=0)
b1 = Button(w, width=10, height=1, text='Get Started', command=bar, border=0, fg='#249794')
b1.place(x=170, y=200)

# label
l1 = Label(w, text="MARK 50", fg='white', bg='#249794', font=('Calibri', 20, "bold"))
l1.place(x=50, y=80)

l2 = Label(w, text="(MRK L)", fg='white', bg='#249794', font=('Calibri',20, "bold"))
l2.place(x=160, y=78)

l3 = Label(w, text="Dasun Nethsara", fg='white', bg='#249794', font=('Calibri', 15, "bold"))
l3.place(x=50, y=110)


w.mainloop()