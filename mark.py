#-------------------------------------------------------------------------------
# Name:        MARK 8 (MRK8)
# Version:	   8.1.1
# Purpose:     Just for fun
# Author:      Dasun Nethsara
# Created:     14/03/2022
# Copyright:   (c) Dasun Nethsara 2022
# Licence:     free software
#-------------------------------------------------------------------------------

# Imports
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from zipfile import ZipFile
import datetime
import pyttsx3
import os
import psutil
import pyautogui
import webbrowser
import ctypes
import wikipedia
import pygame
import time
import shutil

try:
	os.mkdir(os.environ['USERPROFILE']+"\\Documents\\Extracted Items")
except:
	pass

# text 2 speech
engine = pyttsx3.init()
voice = engine.getProperty('voices')
try:
	engine.setProperty('voice', voice[1].id)
except:
	engine.setProperty('voice', voice[0].id)
engine.setProperty('rate', 174)
engine.setProperty('volume', 2.0)

pygame.mixer.init()

# Functions
def talk(audio):
	engine.say(audio)
	engine.runAndWait()

def take_command():
	try:
		if combo.get() != '':
			command = str(combo.get())
			command = command.lower()
			return command
		else:
			messagebox.showwarning('Warning', 'Please select a command on the Combobox')
	except:
		pass


def upTime():
	talk('Getting details. Just a moment sir.')

	lib = ctypes.windll.kernel32
	t = lib.GetTickCount64()
	t = int(str(t)[:-3])

	mins, sec = divmod(t, 60)
	hours, mins = divmod(mins, 60)
	days, hours = divmod(hours, 24)
	talk('Data collecting completed!')
	if days == 0:
		talk('Sir, You have used your computer for ' + str(hours) + ' hours, and ' + str(mins) + ' minuts.')
		messagebox.showinfo('JARVIS - PC Usage', f'PC Usage\n\nHours:\t\t{hours}\nMinutes:\t\t{mins}')
	else:
		talk('Sir, You have used your computer for ' + str(days) + ' days, ' + str(hours) + ' hours, and ' + str(mins) + ' minuts.')
		messagebox.showinfo('JARVIS - PC Usage', f'PC Usage\n\nDays:\t\t{days}\nHours:\t\t{hours}\nMinutes:\t\t{mins}')

def playSong():
	try:
		talk('Please select a Music to play')
		path = filedialog.askopenfilename(filetypes=[('MP3 Files', '*.mp3')], defaultextension=('.mp3'), title='Choose a Song to play')
		if path == '':
			talk('Process canceled by user.')
			pass
		else:
			talk('Playing the song you selected! Just a moment')
			pygame.mixer.music.load(path)
			pygame.mixer.music.play(loops=0)
	except:
		pass
global paused
paused = False
def pauseSong():
	global paused
	try:
		if paused:
			talk('Resuming...')
			pygame.mixer.music.unpause()
			paused = False
		else:
			talk('Pausing...')
			pygame.mixer.music.pause()
			paused = True
	except:
		pass

global stoped
stoped = False

def stopSong():
	try:
		pygame.mixer.music.stop()
		talk('Song stopped')
		global stoped
		stoped = True
	except:
		pass

def zipFile():
	talk('Please select a ZIP file to extract. Do not select RAR files.')
	path = filedialog.askopenfilename(filetypes=[('ZIP Files', '*.zip')], defaultextension=('.zip'), title='Choose a ZIP file to extract.')
	if path != '':
		with ZipFile(path, 'r') as zip:
			#zip.printdir()
			npath = os.environ['USERPROFILE']+'\\Documents\\Extracted Items\\'
			zip.extractall(npath)
			talk('Task is completed sir.')
			os.startfile(npath)
			talk('These are the files extracted by me.')
	else:
		talk('Process canceled by user.')
		pass

def organize():
	talk('Please select a folder to organize.')
	path = filedialog.askdirectory()
	if path != '':
		files = os.listdir(path)

		for file in files:
			filename, extension = os.path.splitext(file)
			extension = extension[1:]
			if os.path.exists(path + "/" + extension):
				shutil.move(path + "/" + file,path+"/"+extension+"/"+file)
			else:
				os.makedirs(path+"/"+extension)
				shutil.move(path+"/"+file,path+"/"+extension)
		talk('Automatic File Organizing completed sir.')
	else:
		talk('Process canceled by user.')
		pass


def run(e):
	command = take_command()

	if 'time' in command:
		try:
			talk('The current time is ' + datetime.datetime.now().strftime('%I:%M %p') + ' sir.')
		except:
			talk('Sorry sir, I have found an error in the datetime module, So I Cloudn\'t get the current time.')

	elif 'date' in command:
		talk('Today is ' + str(datetime.date.today()) + ' sir.')

	elif 'about_you' in command:
		talk('Hello sir! I am JARVIS. Your PC Assistant. I am here to assist you with the varieties tasks is best I can. ')

	elif 'version' in command:
		talk('MARK 8 version 8.1.2')
		messagebox.showinfo("MARK", "MARK 8 (MRK8) PC Assisting Application\n\nApplication Version:\t8\nAssistant Version:\t\t7.0.2")

	elif '=' in command:
		talk('The answer is ' + str(round(eval(command.replace('=', '')), 3)) + ' sir.')

	elif 'pc usage' in command:
		upTime()

	elif 'ss' in command:
		talk('Taking a Screenshot')
		ss = pyautogui.screenshot()
		ss.save(os.environ['USERPROFILE']+'\\Pictures\\JARVIS - Screenshot.png')
		talk('This is the screenshot taken by me')
		os.startfile(os.environ['USERPROFILE']+'\\Pictures\\JARVIS - Screenshot.png')
		talk('Here is your screenshot')
		os.startfile(os.environ['USERPROFILE']+'\\Pictures')

	elif 'help' in command:
		talk('Opening the help document. wait a second sir.')
		os.startfile('src\\help.pdf')

	elif 'facebook' in command:
		talk('Opening Facebook from your web browser. Just a moment')
		webbrowser.open('www.facebook.com')

	elif 'instagram' in command:
		talk('Opening Instagram from your web browser. Just a moment')
		webbrowser.open('www.instagram.com')

	elif 'youtube' in command:
		talk('Opening YouTube from your web browser. Just a moment')
		webbrowser.open('www.youtube.com')

	elif 'stackoverflow' in command:
		talk('Opening stackoverflow from your web browser. Just a moment')
		webbrowser.open('www.stackoverflow.com')

	elif 'google' in command:
		talk('Opening Google Search Engine. Just a moment')
		webbrowser.open('www.google.com')

	elif 'cpu' in command:
		talk('CPU is at ' + str(psutil.cpu_percent()) + '% sir.')

	elif 'per-ram' in command:
		talk('System Memory is at ' + str(psutil.virtual_memory().percent) + '% sir.')

	elif 'cores' in command:
		talk('Sir, There are ' + str(psutil.cpu_count()) + 'logical CPUs in your Computer')

	elif 'avil-ram' in command:
		ram = round((psutil.virtual_memory().available) / (1024 ** 3), 2)
		talk('Available System Memory is ' + str(ram) + 'GB')

	elif 'used-ram' in command:
		ram = round((psutil.virtual_memory().used) / (1024 ** 3), 2)
		talk('Used System Memory is ' + str(ram) + 'GB')

	elif 'total-ram' in command:
		ram = round((psutil.virtual_memory().total) / (1024 ** 3), 2)
		talk('Total System Memory is ' + str(ram) + 'GB')

	elif 'offline' in command:
		talk('Thank You for working with me. See you again sir!')
		root.destroy()

	elif 'wiki' in command:
		info = command.replace('wiki ', '')
		try:
			talk('Searching for ' + info)
			res = wikipedia.summary(info, 2)
			talk('Search found. Let me speak it sir')
			talk(res)
		except:
			talk('Make sure you\'re connected with the Internet or Try a different word')
			pass

	elif 'pomodoro' in command:
		talk('Opening Pomodoro Timer. This Application helps you to study focused well.')
		os.startfile('src\\pomodoro.exe')

	elif 'play_song' in command:
		playSong()

	elif 'pause_song' in command:
		pauseSong()

	elif 'stop_song' in command:
		stopSong()

	elif 'video' in command:
		try:
			talk('Please select a video file to play')
			path = filedialog.askopenfilename(filetypes=[('MP4 Files', '*.mp4')], defaultextension=('.mp4'), title='Choose a Video to play')
			if path == '':
				talk('Process canceled by user.')
				pass
			else:
				talk('Playing the video you selected! Just a moment')
				os.startfile(os.path.join(path))
		except:
			#talk('Process canceled by user.')
			pass
	
	elif 'zip file extracter' in command:
		zipFile()
	
	elif 'automatic file organizer' in command:
		organize()

	elif 'shutdown' in command:
		talk('Closing JARVIS PC Assistant')
		talk('Initializing shutdown sequence. Shutting System down.')
		os.system('shutdown.exe -s -t 00')

	elif 'restart' in command:
		talk('Closing JARVIS PC Assistant')
		talk('Initializing shutdown sequence. Restarting System.')
		os.system('shutdown.exe -r -t 00')

	elif 'log off' in command:
		talk('Closing JARVIS PC Assistant')
		talk('Initializing shutdown sequence. Logging System off.')
		os.system('shutdown.exe -l')

	elif 'lock' in command:
		talk('Locking your PC. Just a moment sir.')
		os.system('rundll32.exe user32.dll, LockWorkStation')

	elif 'hibernate' in command:
		try:
			talk('Hibernating Your PC.')
			talk('Initializing shutdown sequence. Logging System off.')
			os.system('rundll32.exe powrprof.dll, SetSuspendState')
		except:
			talk('Sorry Sir, your PC has no hibernation ability. To hibernate your PC, You need to activate it.')
			talk('This video will help you sir.')
			webbrowser.open('https://youtu.beYU681US3NS8')

	elif 'this pc' in command:
		talk('Opening Windows Explorer')
		path = 'C:\\Windows\\explorer.exe'
		os.startfile(os.path.join(path))

	elif 'notepad' in command:
		talk('Openin Windows Notepad')
		path = 'C:\\WINDOWS\\system32\\notepad.exe'
		os.startfile(os.path.join(path))

	elif 'about windows' in command:
		talk('Getting details about the Main Operating System')
		path = 'C:\\WINDOWS\\system32\\winver.exe'
		os.startfile(os.path.join(path))

	elif 'wordpad' in command:
		talk('Opening Windows Wordpad')
		path = 'C:\\Windows\\write.exe'
		os.startfile(os.path.join(path))

	elif 'manage' in command:
		talk('Opening Windows System Management Utility')
		path = 'C:\\WINDOWS\\System32\\compmgmt.msc'
		os.startfile(os.path.join(path))

	elif 'programs' in command:
		talk('Opening Add or Remove Programs utility in Control Panel')
		path = 'C:\\WINDOWS\\System32\\appwiz.cpl'
		os.startfile(os.path.join(path))

	elif 'sys-info' in command:
		talk('Getting System Information')
		path = 'C:\\WINDOWS\\System32\\msinfo32.exe'
		os.startfile(os.path.join(path))

	elif 'cmd' in command:
		talk('Opening Windows Command Prompt')
		path = 'C:\\WINDOWS\\System32\\cmd.exe'
		os.startfile(os.path.join(path))

	elif 'taskmgr' in command:
		talk('Opening Windows Task Manager')
		path = 'C:\\WINDOWS\\System32\\taskmgr.exe'
		os.startfile(os.path.join(path))

	elif 'regedit' in command:
		talk('Opening Windows Registry Editor')
		path = 'C:\\WINDOWS\\System32\\regedt32.exe'
		os.startfile(os.path.join(path))

	elif 'sys vol' in command:
		talk('Launching System Volume Mixer')
		os.startfile('C:\\Windows\\System32\\SndVol.exe')

	elif 'services' in command:
		talk('Opening Windows Services. Just a moment sir.')
		os.startfile('C:\\Windows\\System32\\services.msc')

	elif 'restore' in command:
		try:
			os.startfile('C:\\Windows\\System32\\rstrui.exe')
			talk('Opening Windows System Restore Utility. Just a moment sir.')
		except:
			talk('Unknown error found on opening Windows System Restore Utility.')
			pass

	elif 'mrt' in command:
		try:
			os.startfile('C:\\Windows\\System32\\MRT.exe')
			talk('Opening Microsoft Malicious software Removal Tool. Just a moment sir')
		except:
			talk('Sorry sir, The Microsoft Malicious software Removal Tool is not available on your Operating System!')

	elif 'defrag' in command:
		talk('Opening Windows Disk Optimizer')
		os.startfile('C:\\Windows\\System32\\dfrgui.exe')

	elif 'ctrl panel' in command:
		talk('Opening Windows Control Panel')
		os.startfile('C:\\Windows\\System32\\control.exe')

	elif 'cleanmgr' in command:
		talk('Opening Windows Disk Cleanup Tool')
		os.startfile('C:\\Windows\\System32\\cleanmgr.exe')

	elif 'charmap' in command:
		talk('Opening Windows Character Map')
		os.startfile('C:\\Windows\\System32\\charmap.exe')

	elif 'diskpart' in command:
		talk('Opening Windows Diskpart utility')
		os.startfile('C:\\Windows\\System32\\diskpart.exe')


	# application

	elif 'vlc' in command:
		try:
			path = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
			talk('Opening VLC Media Player')
			os.startfile(os.path.join(path))
		except:
			talk('Sorry sir, you have not installed VLC Media Player on your PC')
			pass

	elif 'aimp' in command:
		try:
			talk('Opening AIMP Music Player')
			os.startfile('C:\\Program Files (x86)\\AIMP\\AIMP.exe')
		except:
			talk('Sorry sir, you have not installed AIMP Music Player on your PC')
			pass

	elif 'zoom' in command:
		try:
			path = '\\AppData\\Roaming\\Zoom\\bin\\zoom.exe'
			talk('Opening Zoom Cloud Meeting Service')
			os.startfile(os.path.join(os.environ['USERPROFILE']+path))
		except:
			talk('Sorry sir, you have not installed Zoom Cloud Meeting Service on your PC')
			pass

	elif 'sublime text' in command:
		try:
			path = 'C:\\Program Files\\Sublime Text\\sublime_text.exe'
			talk('Opening Sublime Text')
			os.startfile(os.path.join(path))
		except:
			talk('Sorry sir, you have not installed Sublime Text on your PC')
			pass

	elif 'pyscripter' in command:
		try:
			path = 'C:\\Program Files\\PyScripter\\PyScripter.exe'
			talk('Opening PyScripter IDE')
			os.startfile(os.path.join(path))
		except:
			talk('Sorry sir, you have not installed PyScripter IDE on your PC')
			pass

	elif 'vs code' in command:
		try:
			path = '\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
			talk('Opening Visual Studio Code')
			os.startfile(os.path.join(os.environ['USERPROFILE'] + path))
		except:
			talk('Sorry sir, you have not installed Visual Studio Code on your PC')
			pass

	elif 'word' in command:
		try:
			path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk'
			talk('OPening Microsoft Office Word')
			os.startfile(os.path.join(path))
		except:
			talk('Sorry sir, you have not installed Microsoft Office 2013 on your PC')
			pass

	elif 'powerpoint' in command:
		try:
			path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013.lnk'
			talk('OPening Microsoft Office PowerPoint')
			os.startfile(os.path.join(path))
		except:
			talk('Sorry sir, you have not installed Microsoft Office 2013 on your PC')
			pass

	elif 'excel' in command:
		try:
			talk('OPening Microsoft Office Excel')
			path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013.lnk'
			os.startfile(os.path.join(path))
		except:
			talk('Sorry sir, you have not installed Microsoft Office 2013 on your PC')
			pass

	else:
		talk('Sorry sir, This command is incorrect or not defined! To get a help, You need to select, "Help" from the Combo box.')

hour = datetime.datetime.now().hour

if hour >= 0 and hour < 12:
	msg = 'Good Morning, '
elif hour >= 12 and hour < 17:
	msg = 'Good Afternoon, '
elif hour >= 17 and hour < 22:
	msg = 'Good Evening, '
else:
	pass


try:
	name = os.environ['USERPROFILE'][9:]
	username = name.split()[0]
except:
	username = os.environ['USERPROFILE'][9:]

engine.setProperty('voice', voice[0].id)
talk('MARK 8 application is now online. Initializing JARVIS PC Assistant.')
time.sleep(1)

try:
	engine.setProperty('voice', voice[1].id)
except:
	engine.setProperty('voice', voice[0].id)

try:
	talk(msg + 'its ' + datetime.datetime.now().strftime('%I:%M %p'))
except:
	talk('its ' + datetime.datetime.now().strftime('%I:%M %p'))

talk(f'Hello {username}. I am JARVIS! Your PC Assistant.')

#Main UI
root = Tk()
root.title('MARK 8')
root.geometry('260x230+600+400')
ico = root.iconbitmap('icon.ico')
root.resizable(0, 0)
bg = Image.open('bg.png')
bg = bg.resize((160, 160))
bg = ImageTk.PhotoImage(bg)
Label(root, image=bg, bd=0).pack(pady=15)
root.config(bg='black')

#UI Widgets
values_ = ('Time', 'Date', 'About_You', 'Version', '=', 'PC Usage',
		   'SS','Facebook','Instagram','YouTube','Stackoverflow',
		   'Google','CPU','Cores','Per-RAM','Avil-RAM','Used-RAM',
		   'Total-RAM','Offline','Pomodoro','Help','Play_Song',
		   'Pause_Song','Stop_Song','Video','ZIP File Extracter',
		   'Automatic File Organizer','Shutdown','Restart','Log Off',
		   'Lock','Hibernate','Wiki','This PC','Notepad','About Windows',
		   'Wordpad','Manage','Programs','Sys-Info','CMD','taskmgr','regedit',
		   'Sys Vol','Services','Restore','MRT','Defrag','Ctrl Panel',
		   'cleanmgr','CharMap','diskpart','VLC','AIMP','ZOOM','Sublime Text',
		   'PyScripter','VS Code','Smart Defrag','Word','PowerPoint','Excel')
		   

combo = ttk.Combobox(root, width=21, values=values_, state='w', font=('Calibri', 14, 'bold'), justify='center')
combo.pack()
combo.set('Select a Command')


root.bind('<Return>', run)

root.mainloop()