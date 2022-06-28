#imports
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import subprocess


path = ''
#Functions

def run():
	if path == '':
		messagebox.showerror('Error', 'Please save the file before running!')
	else:
		command = f'python {path}'
		runFile = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		output, error = runFile.communicate()
		outputarea.delete(1.0, END)
		outputarea.insert(1.0, output)
		outputarea.insert(1.0, error)


def saveAs():
	global path
	path = filedialog.asksaveasfilename(filetypes=[('Python Files', '*.py')], defaultextension=('.py'))
	if path != '':
		file = open(path, 'w')
		file.write(textarea.get(1.0, END))
		file.close()

def openFile(event=None):
	global path
	path = filedialog.askopenfilename(filetypes=[('Python Files', '*.py')], defaultextension=('.py'))
	if path != '':
		file = open(path, 'r')
		data = file.read()
		textarea.delete(1.0, END)
		textarea.insert(1.0, data)
		file.close()

def save(event=None):
	if path == '':
		saveAs()
	else:
		file = open(path, 'w')
		file.write(textarea.get(1.0, END))
		file.close()

def newFile(event=None):
	global path
	path = ''
	textarea.delete(1.0, END)
	outputarea.delete(1.0, END)

def iexit(event=None):
	res = messagebox.askyesno('Confirm', 'Do you want to exit?')
	if res:
		win.destroy()
	else:
		pass

def theme():
	if check.get() == 'light':
		win.config(bg='white')
		textarea.config(bg='white', fg='black')
		outputarea.config(bg='white', fg='black')
		outputFrame.config(bg='white', fg='black')

	if check.get() == 'dark':
		win.config(bg='gray20')
		textarea.config(bg='gray20', fg='white')
		outputFrame.config(bg='gray20', fg='white')
		outputarea.config(bg='gray20', fg='white')

def clear():
	textarea.delete(1.0, END)
	outputarea.delete(1.0, END)

def font_inc(event=None):
	global font_size
	font_size += 1
	textarea.config(font=('Consolas', font_size, 'bold'))

def font_dec(event=None):
	global font_size
	font_size -= 1
	textarea.config(font=('Consolas', font_size, 'bold'))


font_size = 17

win = Tk()
win.title('Python IDE')
win.geometry('1270x670+150+250')
win.iconbitmap('icon.ico')

myMenu = Menu()
filemenu = Menu(myMenu, tearoff=0)
filemenu.add_command(label='New file', accelerator='Ctrl + N', command=newFile)
filemenu.add_command(label='Open file', accelerator='Ctrl + O', command=openFile)
filemenu.add_command(label='Save As...', accelerator='Ctrl + Alt + S', command=saveAs)
filemenu.add_command(label='Save file', accelerator='Ctrl + S')
filemenu.add_command(label='Exit', accelerator='Ctrl + Q', command=iexit)
myMenu.add_cascade(label='File', menu=filemenu)

check = StringVar()
check.set('light')
thememenu = Menu(myMenu, tearoff=0)
thememenu.add_radiobutton(label='Light Theme', variable=check, value='light', command=theme)
thememenu.add_radiobutton(label='Dark Theme', variable=check, value='dark', command=theme)

myMenu.add_cascade(label='Theme', menu=thememenu)


myMenu.add_command(label='Clear', command=clear)

myMenu.add_command(label='Run', command=run)

win.config(menu=myMenu)


editFrame = Frame(win, bg='white')
editFrame.place(x=0, y=0, height=500, relwidth=1)

scrollBar = Scrollbar(editFrame, orient=VERTICAL)
scrollBar.pack(side=RIGHT, fill=Y)
textarea = Text(editFrame, font=('Consolas', font_size, 'bold'), yscrollcommand=scrollBar.set)
textarea.pack(fill=BOTH)
scrollBar.config(command=textarea.yview)


outputFrame = LabelFrame(win, bg='white', text='Output', font=('Arial', 12, 'bold'))
outputFrame.place(x=0, y=500, height=170, relwidth=1)
scrollBar2 = Scrollbar(outputFrame, orient=VERTICAL)
scrollBar2.pack(side=RIGHT, fill=Y)
outputarea = Text(outputFrame, font=('Consolas', font_size, 'bold'), yscrollcommand=scrollBar2.set)
outputarea.pack(fill=BOTH)
scrollBar2.config(command=textarea.yview)



win.bind('<Control-n>', newFile)
win.bind('<Control-o>', openFile)
win.bind('<Control-s>', save)
win.bind('<Control-q>', iexit)

win.bind('<Control-p>', font_inc)
win.bind('<Control-m>', font_dec)

win.mainloop()