from tkinter import *
from PIL import Image, ImageTk
import time

bgcolor = '#272727'

root = Tk()
width_of_window = 427
height_of_window = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = (screen_width / 2) - (width_of_window / 2)
y_cordinate = (screen_height / 2) - (height_of_window / 2)
root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_cordinate, y_cordinate))
root.config(bg=bgcolor)
root.overrideredirect(True)



a = ImageTk.PhotoImage(Image.open('1.png').resize((10, 10)))
b = ImageTk.PhotoImage(Image.open('2.png').resize((10, 10)))
logo = ImageTk.PhotoImage(Image.open('icon.ico'))

Frame(root, width=427, height=250, bg=bgcolor).place(x=0, y=0)
Label(root, image=logo, bd=0, bg=bgcolor).place(x=180, y=15)
Label(root, text="MARK 68", font=('Game of squids', 29, 'bold'), fg='#ff0', bg=bgcolor).place(x=100, y=85)
Label(root, text="Powered by Dasun Nethsara", font=('Poppins', 13), fg='white', bg=bgcolor).place(x=85, y=140)
Label(root, text="Loading...", font=('Calibri', 11), fg='white', bg=bgcolor).place(x=10, y=215)

# animation

for i in range(3):
    Label(root, image=a, bd=0, relief=SUNKEN).place(x=180, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=200, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=220, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=240, y=195)
    root.update_idletasks()
    time.sleep(0.5)

    Label(root, image=b, bd=0, relief=SUNKEN).place(x=180, y=195)
    Label(root, image=a, bd=0, relief=SUNKEN).place(x=200, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=220, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=240, y=195)
    root.update_idletasks()
    time.sleep(0.5)

    Label(root, image=b, bd=0, relief=SUNKEN).place(x=180, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=200, y=195)
    Label(root, image=a, bd=0, relief=SUNKEN).place(x=220, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=240, y=195)
    root.update_idletasks()
    time.sleep(0.5)

    Label(root, image=b, bd=0, relief=SUNKEN).place(x=180, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=200, y=195)
    Label(root, image=b, bd=0, relief=SUNKEN).place(x=220, y=195)
    Label(root, image=a, bd=0, relief=SUNKEN).place(x=240, y=195)
    root.update_idletasks()
    time.sleep(0.5)


root.destroy()
root.mainloop()
