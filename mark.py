#-------------------------------------------------------------------------------
# Name:        MARK 50 (MRK L)
# Version:	   50.5.21.1
# Purpose:     Just for fun
# Author:      Dasun Nethsara
# Created:     24/05/2022
# Copyright:   (c) Dasun Nethsara 2022
# Licence:     free software
#-------------------------------------------------------------------------------


'''
--------------------+++++++++++++++++++++ MARK 50 +++++++++++++++++++++--------------------
-------------------=================== DOCUMENTATIONS ===================------------------

Welcome to the MARK 50 Source Code. MARK 50 is the next level free assisting software to make your computer easier to use.
JARVIS is the assisting program inside of the MARK application. We have upgraded the features, performance and the experience.

With,
✓ New Interface
✓ New Features
✓ More Powerful
✓ More Helpful
✓ More Options
✓ Easier to use
✓ With new bug fixes
✓ No more typing. Only selecting!

MARK 50 v50.5.21.1 is an open source community application. It works all the new Windows version Like Windows 8.1, 10 and Windows 11.

-------- System Requirements (Recommended) --------
OS - Windows 8.1 or upper
CPU - 1GHz Pentium IV Processor
RAM - 265MB or upper
VGA - 64MB with WDDM 1.0 Graphics Drivers

-------- New Features --------
✓ Built-In Music Player
✓ Automatic File Organizer
✓ ZIP File Extractor
✓ Familiar commands
✓ COVID 19 Tracker
✓ New GUI Effects
✓ PC Information


If you faced to any trouble, you can contact the programmer of the MARK 50.

Email - techsaralk.pro@gmail.com
GitHub - https://github.com/DasunNethsara-04/
Stackoverflow - https://stackoverflow.com/users/18193670/dasun-nethsara
Telegram - https://t.me/techsara_lk




Dasun Nethsara
2022.05.24
All Rights Reserved.
'''

# Imports
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog, ttk
from PIL import Image, ImageTk, ImageSequence
from bs4 import BeautifulSoup
from zipfile import ZipFile
import PySimpleGUI as sg
import requests
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
import boot_screen

try:
	os.mkdir(os.environ['USERPROFILE'] + "\\Documents\\Extracted Items")
except:
	pass

# text 2 speech
engine = pyttsx3.init()
voice = engine.getProperty('voices')
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
	talk('Initializing Built in Music Player')
	try:
		talk('Please select a Music to play')
		path = filedialog.askopenfilename(filetypes=[('MP3 Files', '*.mp3')], defaultextension=('.mp3'), title='Choose a Song to play')
		if path == '':
			talk('Process canceled by user.')
			pass
		else:
			talk('Playing the song you selected!')
			pygame.mixer.music.load(path)
			pygame.mixer.music.play(loops=0)
	except:
		talk('Initializing Faild.')
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
		talk('Song stopped. Deactivating the music player.')
		global stoped
		stoped = True
	except:
		pass

def zipFile():
	talk('Please select a ZIP file to extract. Do not select RAR files.')
	path = filedialog.askopenfilename(filetypes=[('ZIP Files', '*.zip')], defaultextension=('.zip'), title='Choose a ZIP file to extract.')
	if path != '':
		with ZipFile(path, 'r') as zip:
			npath = os.environ['USERPROFILE']+'\\Documents\\Extracted Items\\'
			zip.extractall(npath)
			sg.popup_notify("ZIP FIle Extracting Completed!", title='Done', icon='icon.png')
			talk('Task is completed.')
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
		sg.popup_notify("Automatic File Organizing completed!", title='Done', icon='icon.png')
		talk('Automatic File Organizing completed.')
	else:
		talk('Process canceled by user.')
		pass

def getTemp():
	talk('Just a moment.')
	try:
		location = take_command().replace('temperature in', '')
		search = f"temperature in {location}"
		url = f'https://www.google.com/search?q={search}'
		r = requests.get(url)
		data = BeautifulSoup(r.text, "html.parser")
		temp = data.find("div", class_="BNeawe").text
		talk(f'The Current {search} is {temp}.')
	except:
		talk('Make sure you are connected with the Internet.')
		pass

def get_html_data(url):
	try:
		data = requests.get(url)
		return data
	except:
		pass

def getCovidData():
	try:
		url = 'https://www.worldometers.info/coronavirus/'
		html_data = get_html_data(url)
		bs = BeautifulSoup(html_data.text, 'html.parser')
		info_div = bs.find('div', class_='content-inner').findAll('div', id='maincounter-wrap')
		all_data = ''
		for blank in info_div:
			text = blank.find('h1', class_= None).get_text()
			count = blank.find('span', class_= None).get_text()
			all_data = all_data + text + ' '+count + '\n'
		return all_data
	except:
		talk('Make sure your are connected with the internet!')
		pass

def search():
	command = take_command().replace('search', '')
	talk('Searching for ' + command)
	try:
		pyautogui.press('Win')
		for y in command:
			pyautogui.press(y)
		pyautogui.press('Enter')
	except:
		talk('Error searching '+ command)
		pass

def take_screenshot():
	root.iconify()
	talk('Taking a Screenshot')
	ss = pyautogui.screenshot()
	ss.save(os.environ['USERPROFILE']+'\\Pictures\\JARVIS - Screenshot.png')
	talk('This is the screenshot taken by me')
	os.startfile(os.environ['USERPROFILE']+'\\Pictures\\JARVIS - Screenshot.png')
	time.sleep(2)
	talk('Here is your screenshot. I renamed the screenshot as, JARVIS - Screenshot.png')
	os.startfile(os.environ['USERPROFILE']+'\\Pictures')

'''			Main Function			'''

def run(e):
	# username spilling
	name = psutil.users()[0][0]
	try:
		sname = name.split()[1]
	except:
		sname = name.split()[0]
	command = take_command()

	if 'time' in command:
		try:
			talk('The current time is ' + datetime.datetime.now().strftime('%I:%M %p') + '.')
		except:
			talk(f'Sorry Mr.{sname}, I have found an error in the datetime module, So I Couldn\'t get the current time.')

	elif 'date' in command:
		talk('Today is ' + str(datetime.date.today()) + ' sir.')

	elif 'about you' in command:
		talk('Hello sir! I am JARVIS. Your PC Assistant. JARVIS stands for, Just A Rather Very Intelligent System. I am here to assist you with the varieties tasks is best I can.')

	elif 'version' in command:
		talk('MARK 50 version 50.5.21.1')
		messagebox.showinfo("MARK", "MARK 50 (MRK L) PC Assisting Application\n\nApplication Version:\t\t50\nAssistant Version:\t\t50.5.21.1")

	elif '=' in command:
		ans = round(eval(command.replace('=', '')), 3)
		talk('The answer is ' + str(ans) + ' sir.')
		sg.popup_notify(f'Answer is {ans}', title='Answer', icon='icon.png')

	elif 'pc usage' in command:
		upTime()

	elif 'screenshot' in command:
		take_screenshot()

	elif 'pc info' in command:
		talk('Launching PC Info')
		import pc_info

	elif 'global covid' in command:
		data = getCovidData()
		talk(data)
		messagebox.showinfo('Details', data)

	elif 'help' in command:
		talk('Opening the help document. wait a second.')
		os.startfile('src\\help.pdf')
	
	elif 'search' in command:
		search()

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
		talk('CPU is at ' + str(psutil.cpu_percent()) + '%.')

	elif 'ram percentage' in command:
		talk('System Memory is at ' + str(psutil.virtual_memory().percent) + '%.')

	elif 'cores' in command:
		talk('There are ' + str(psutil.cpu_count()) + ' logical CPUs in your Computer')

	elif 'available ram' in command:
		ram = round((psutil.virtual_memory().available) / (1024 ** 3), 2)
		talk('Available System Memory is ' + str(ram) + 'GB')

	elif 'used ram' in command:
		ram = round((psutil.virtual_memory().used) / (1024 ** 3), 2)
		talk('Used System Memory is ' + str(ram) + 'GB')

	elif 'total ram' in command:
		ram = round((psutil.virtual_memory().total) / (1024 ** 3), 2)
		talk('Total System Memory is ' + str(ram) + 'GB')

	elif 'offline' in command:
		talk('Thank You for working with me. See you again sir!')
		sg.popup_notify('Have a nice day sir!', title='Good Bye', icon='icon.png')
		root.destroy()

	elif 'temperature in' in command:
		getTemp()
	
	elif 'create python file' in command:
		try:
			talk('Creating Python File')
			path = os.environ['USERPROFILE']+'\\Desktop'
			f = open(f'{path}\\Python File.py', 'w')
			f.write('# Made by MARK 50\n\n')
			f.close()
			sg.popup_notify(f'File Created\nin {path}\\Python File.py', title='Done', icon='icon.png')
		except:
			talk('Error creating Python File')
			pass		

	elif 'settings' in command:
		talk('Opening Settings')
		global ico, v
		win = Toplevel(root)
		win.geometry('600x200+450+420')
		win.title('Settings')
		win.resizable(0, 0)
		win.iconbitmap('icon.ico')
		s = ttk.Style()
		s.configure('TButton', font=('Calibri', 13))

		def select():
			global data, v
			cho = n.get()
			if cho == 'Voice 1 - Microsoft David':
				try:
					engine.setProperty('voice', voice[0].id)
					talk('You have selected Microsoft David as the Default JARVIS\' voice')
				except:
					Label(win, text='In some computers\' This sound might not be worked!', fg='red', font=('Calibri', 14, 'bold')).place(x=50, y=110)
					engine.setProperty('voice', voice[0].id)
					pass

			elif cho == 'Voice 2 - Microsoft Mark':
				try:
					engine.setProperty('voice', voice[1].id)
					talk('You have selected Microsoft Mark as the Default JARVIS\' voice')
				except:
					Label(win, text='In some computers\' This sound might not be worked!', fg='red', font=('Calibri', 14, 'bold')).place(x=50, y=110)
					engine.setProperty('voice', voice[0].id)
					pass
			else:
				try:
					engine.setProperty('voice', voice[2].id)
					talk('You have selected Microsoft Zira as the Default JARVIS\'s voice')
				except:
					Label(win, text='In some computers\' This sound might not be worked!', fg='red', font=('Calibri', 14, 'bold')).place(x=50, y=110)
					engine.setProperty('voice', voice[0].id)
					pass
		def close():
			cho2 = ne.get()
			sound = open('sound.txt', 'w')
			sound.write(str(cho2))
			sound.close()

		ttk.Label(win, text='Settings', font=('Calibri', 26, 'underline'), foreground='red').pack(side=TOP)
		ttk.Label(win, text='Change the JARVIS voice to: ', font=('Times', 13)).place(x=5, y=70)

		n = StringVar()
		choice = ttk.Combobox(win, width=25, textvariable=n, state='readonly')
		choice['values'] = ('Voice 1 - Microsoft David',
							'Voice 2 - Microsoft Mark',
							'Voice 3 - Microsoft Zira')
		choice.place(x=230, y=70)
		choice.current(0)
		ttk.Button(win, text='Preview', command=select).place(x=420, y=65)
		ne = BooleanVar()
		chk = ttk.Checkbutton(win, text='Enable the startup JARVIS sound', variable=ne, command=close)
		if v == "True":
			chk.state(['selected'])
		else:
			chk.state(['!selected'])
		chk.place(x=10, y=130)

		ttk.Button(win, text='Close', command=win.destroy).place(x=480, y=150)

		win.mainloop()

	elif 'wiki' in command:
		info = command.replace('wiki ', '')
		try:
			talk('Searching for ' + info)
			res = wikipedia.summary(info, 2)
			talk('Search found. Let me deliver it for you.')
			talk(res)
		except:
			talk('Make sure you\'re connected with the Internet or Try another word')
			pass

	elif 'pomodoro' in command:
		talk('Opening Pomodoro Timer. This Application helps you to study focused well.')
		os.startfile('src\\pomodoro.exe')

	elif 'play song' in command:
		talk('The songs has been playing started. If you want to pause it, you can cant do it just selecting, Pause Song ')
		playSong()

	elif 'pause song' in command:
		pauseSong()

	elif 'stop song' in command:
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
		talk('Locking your PC. Just a moment.')
		os.system('rundll32.exe user32.dll, LockWorkStation')

	elif 'hibernate' in command:
		try:
			talk('Hibernating Your PC.')
			talk('Initializing shutdown sequence. Logging System off.')
			os.system('rundll32.exe powrprof.dll, SetSuspendState')
		except:
			talk('Sorry Sir, your PC has no hibernation ability. To hibernate your PC, You need to activate it.')
			talk('This video will help you.')
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

	elif 'management' in command:
		talk('Opening Windows System Management Utility')
		path = 'C:\\WINDOWS\\System32\\compmgmt.msc'
		os.startfile(os.path.join(path))

	elif 'programs' in command:
		talk('Opening Add or Remove Programs utility in Control Panel')
		path = 'C:\\WINDOWS\\System32\\appwiz.cpl'
		os.startfile(os.path.join(path))

	elif 'system info' in command:
		talk('Getting System Information')
		path = 'C:\\WINDOWS\\System32\\msinfo32.exe'
		os.startfile(os.path.join(path))

	elif 'command prompt' in command:
		talk('Opening Windows Command Prompt')
		path = 'C:\\WINDOWS\\System32\\cmd.exe'
		os.startfile(os.path.join(path))

	elif 'task manager' in command:
		talk('Opening Windows Task Manager')
		path = 'C:\\WINDOWS\\System32\\taskmgr.exe'
		os.startfile(os.path.join(path))

	elif 'registry editor' in command:
		talk('Opening Windows Registry Editor')
		path = 'C:\\WINDOWS\\System32\\regedt32.exe'
		os.startfile(os.path.join(path))

	elif 'system volume' in command:
		talk('Launching System Volume Mixer')
		os.startfile('C:\\Windows\\System32\\SndVol.exe')

	elif 'services' in command:
		talk('Opening Windows Services. Just a moment.')
		os.startfile('C:\\Windows\\System32\\services.msc')

	elif 'restore' in command:
		try:
			os.startfile('C:\\Windows\\System32\\rstrui.exe')
			talk('Opening Windows System Restore Utility. Just a moment.')
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

	elif 'control panel' in command:
		talk('Opening Windows Control Panel')
		os.startfile('C:\\Windows\\System32\\control.exe')

	elif 'disk cleanup' in command:
		talk('Opening Windows Disk Cleanup Tool')
		os.startfile('C:\\Windows\\System32\\cleanmgr.exe')

	elif 'character map' in command:
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
			talk('Sorry sir, you have not installed VLC Media Player on your computer.')
			pass

	elif 'aimp' in command:
		try:
			talk('Opening AIMP Music Player')
			os.startfile('C:\\Program Files (x86)\\AIMP\\AIMP.exe')
		except:
			talk('Sorry sir, you have not installed AIMP Music Player on your computer.')
			pass

	elif 'zoom' in command:
		try:
			path = '\\AppData\\Roaming\\Zoom\\bin\\zoom.exe'
			talk('Opening Zoom Cloud Meeting Service')
			os.startfile(os.path.join(os.environ['USERPROFILE']+path))
		except:
			talk('Sorry sir, you have not installed Zoom Cloud Meeting Service on your computer')
			pass

	elif 'sublime text' in command:
		try:
			path = 'C:\\Program Files\\Sublime Text\\sublime_text.exe'
			talk('Opening Sublime Text')
			os.startfile(os.path.join(path))
		except:
			talk('Sorry sir, you have not installed Sublime Text on your computer')
			pass

	elif 'pyscripter' in command:
		try:
			path = 'C:\\Program Files\\PyScripter\\PyScripter.exe'
			talk('Opening PyScripter IDE')
			os.startfile(os.path.join(path))
		except:
			talk('Sorry sir, you have not installed PyScripter IDE on your computer')
			pass

	elif 'vs code' in command:
		try:
			path = '\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
			talk('Opening Visual Studio Code')
			os.startfile(os.path.join(os.environ['USERPROFILE'] + path))
		except:
			talk('Sorry sir, you have not installed Visual Studio Code on your computer')
			pass

	elif 'word' in command:
		search()

	elif 'powerpoint' in command:
		search()
			
	elif 'excel' in command:
		search()
	
	elif 'access' in command:
		search()
	
	#elif 'uninstall mark 50' in command:
	#	talk('Getting Ready to uninstall MARK 50')
	#	import uninstall

	else:
		try:
			search()
		except:
			talk('Sorry sir, This command is incorrect or not defined! To get a help, You need to select, "Help", from the Combo box.')

'''	-----------------------------------------------	'''

'''			Background Animating			'''

class AnimateGif(object):
    def __init__(self, image):
        self._frames = []
        img = Image.open(image)
        for frame in ImageSequence.Iterator(img):
            photo = ImageTk.PhotoImage(frame)
            photo.delay = frame.info['duration'] * 10
            self._frames.append(photo)

    def __len__(self):
        return len(self._frames)
    
    def __getitem__(self, frame_num):
        return self._frames[frame_num]
    
def update_label_image(label, ani_img, ms_delay, frame_num):
    global cancel_id
    label.configure(image=ani_img[frame_num])
    frame_num = (frame_num + 1) % len(ani_img)
    cancel_id = root.after(ms_delay, update_label_image, label, ani_img, ms_delay, frame_num)
    
def enable_animation():
    global cancel_id
    if cancel_id is None:
        ms_delay = 5000 // len(ani_img)
        cancel_id = root.after(ms_delay, update_label_image, animation, ani_img, ms_delay, 0)

def cancel_animation():
    global cancel_id
    if cancel_id is not None:
        root.after_cancel(cancel_id)
        cancel_id = None

'''------------------------------------------'''

pygame.mixer.music.load('src\\greeting.mp3')
pygame.mixer.music.play(loops=0)
'''
else:
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
		username = name.split()[1]
	except:
		username = os.environ['USERPROFILE'][9:]

	engine.setProperty('voice', voice[0].id)
	talk('MARK 50 is now online. Initializing JARVIS PC Assistant.')
	talk('Activating all the protocols.')
	talk('Keyboard Automation Activated.')
	time.sleep(1)

	try:
		engine.setProperty('voice', voice[0].id)
	except:
		engine.setProperty('voice', voice[0].id)

	try:
		search2 = f"temperature in"
		url = f'https://www.google.com/search?q={search2}'
		r = requests.get(url)
		data = BeautifulSoup(r.text, "html.parser")
		temp = data.find("div", class_="BNeawe").text
	except:
		pass

	try:
		talk(msg + 'its ' + datetime.datetime.now().strftime('%I:%M %p') + '. The weather in current location is ' + temp)
	except:
		talk(msg + 'its ' + datetime.datetime.now().strftime('%I:%M %p'))

	talk(f'Hello Mister {username}! I\'m JARVIS! Your PC Assistant.')
'''

#Main UI

root = Tk()
root.title('MARK 50')
root.geometry('260x230+600+400')
ico = root.iconbitmap('icon.ico')
root.resizable(0, 0)
root.config(bg='black')

ani_img = AnimateGif("anim.gif")
cancel_id = None
animation = Label(image=ani_img[0], bd=0)
#animation.place(x=-110, y=-80)
animation.pack()
enable_animation()

#UI Widgets
values_ = (
			'Time', 'Date', 'About You', 'Version', '= ', 'PC Usage','Create Python File', 
			'Screenshot','PC Info','Global COVID','Search ',
		   	'Facebook','Instagram','YouTube','Stackoverflow','Google','CPU','Cores',
		   	'RAM Percentage','Available RAM','Used RAM','Total RAM','Offline',
		   	'Temperature in','Pomodoro','Help','Play Song','Pause Song','Stop Song',
		   	'Video','ZIP File Extracter','Settings','Automatic File Organizer',
		   	'Shutdown','Restart','Log Off','Lock','Hibernate','Wiki ','This PC',
		   	'Notepad','About Windows','Wordpad','Management','Programs','System Info',
		   	'Command Prompt','Task Manager','Registry Editor','System Volume','Services',
		   	'Restore','MRT','Defrag','Control Panel','Disk Cleanup','Character Map',
		   	'diskpart','VLC Meida Player','AIMP Music Player','ZOOM','Sublime Text',
		   	'PyScripter','VS Code','Word','PowerPoint','Excel', 'Access',
		   )


combo = ttk.Combobox(root, width=21, values=values_, state='w', font=('Calibri', 14, 'bold'), justify='center')
combo.place(x=15, y=190)
combo.set('Select a Command')


root.bind('<Return>', run)

root.mainloop()
