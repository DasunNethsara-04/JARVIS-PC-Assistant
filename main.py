# imports
from typing import Any

from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import PySimpleGUI as sg
from PIL import Image
import datetime, pyttsx3, tkinter, random, os, requests, CTkToolTip, wikipedia, psutil, messages, threading, requests
from tkinter import filedialog
from functions import *
import subprocess
import platform

# theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# text 2 speech
engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("rate", 174)
engine.setProperty("volume", 2.0)


def logOff() -> None:
    talk(random.choice(messages.ok))
    os.system("shutdown.exe -l")


def updateCpuUtilization() -> None:
    util = psutil.cpu_percent()
    cpuLabel.configure(text=f"{util}%")
    cpuLabel.after(1000, updateCpuUtilization)


def updateRamUsage1() -> None:
    used = round((psutil.virtual_memory().used) / (1024**3), 2)
    ramLabel1.configure(text=f"{used}GB")
    ramLabel1.after(1000, updateRamUsage1)


def updateRamUsage2() -> None:
    total = round((psutil.virtual_memory().total) / (1024**3), 2)
    ramLabel2.configure(text=f"{total}GB")
    ramLabel2.after(1000, updateRamUsage2)


def botAns(text) -> None:
    msgBox.insert(tkinter.END, text=f"JARVIS: {text}\n")
    talk(text)


def change_appearance_mode_event(new_appearance_mode) -> None:
    ctk.set_appearance_mode(new_appearance_mode)


def change_color_theme_event(new_color_mode) -> None:
    ctk.set_default_color_theme(new_color_mode)


def settingsPanel() -> None:
    settings_window = ctk.CTkToplevel()
    settings_window.title("Settings - MARK PC Assistant")
    settings_window.resizable(width=False, height=False)

    # settings panel widgets
    ctk.CTkLabel(settings_window, text="Appearance Mode", font=("Arial", 14)).grid(row=1, column=0)
    appearance_mode_optionemenu = ctk.CTkOptionMenu(
        settings_window,
        values=["Dark", "Light", "System"],
        command=change_appearance_mode_event,
    )
    appearance_mode_optionemenu.grid(row=1, column=1)

    ctk.CTkLabel(settings_window, text="Colour Theme", font=("Arial", 14)).grid(row=2, column=0)
    theme_color_optionemenu = ctk.CTkOptionMenu(
        settings_window,
        values=["blue", "dark-blue", "green"],
        command=change_color_theme_event,
    )
    theme_color_optionemenu.grid(row=2, column=1)


def talk(audio) -> None:
    engine.say(audio)
    engine.runAndWait()


def get_current_time() -> None:
    url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Colombo"  # Replace with the actual API URL

    def make_api_request():
        while True:
            response: Any = requests.get(url)
            if response.status_code == 200:
                current_time: Any = response.json()["time"]
                date = response.json()["date"]
                timeZone = response.json()["timeZone"]
                # print("Current time:", current_time)
            else:
                print("Error:", response.status_code)
                import datetime

                current_time = datetime.datetime.now().strftime("%I:%M %p")
                date = datetime.date.today()
                timeZone = "N/A"

            timeabel.configure(text=current_time)
            dateLabel.configure(text=date)
            timeZonelbl.configure(text=timeZone)

            time.sleep(1)  # Wait for 1 second before making the next request

    # Create a new thread and start it
    api_thread = threading.Thread(target=make_api_request)
    api_thread.start()


def run(event):
    userAns = txtBox.get().lower()
    msgBox.insert(tkinter.END, f"User: {txtBox.get()}\n")
    if "time" in userAns:
        try:
            response = requests.get(
                "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Colombo"
            )
            if response.status_code == 200:
                data = response.json()
                current_time = data["time"]
                botAns("Current time is: " + current_time)

            else:
                botAns("Error: ", response.status_code)
        except Exception as e:
            playTrack("./src/voice/caged_network_lost_wifi.wav")

    elif "date" in userAns:
        botAns("Today is " + str(datetime.date.today()) + " sir.")

    elif "about you" in userAns:
        playTrack("./src/voice/caged_intro_2.wav")

    elif "version" in userAns:
        botAns("MARK 68 version 12.7.4")
        CTkMessagebox(
            title="MARK",
            message="MARK 68 (MRK LXVIII) PC Assisting Application\n\nApplication Version:\t52\nAssistant Version:\t\t52.0.0.1",
        )

    elif "=" in userAns:
        try:
            ans = round(eval(userAns.replace("=", "")), 3)
            botAns("The answer is " + str(ans) + " sir.")
            sg.popup_notify(f"Answer is {ans}", title="Answer")
        except ValueError as e:
            botAns("An error found: ", e)

    elif "wiki" in userAns:
        info: str = userAns.replace("wiki ", "")
        try:
            botAns("Searching for " + info)
            res = wikipedia.summary(info, 2)
            talk("Search found. Let me deliver it for you.")
            botAns(res)
        except:
            playTrack("./src/voice/caged_network_lost_wifi.wav")
            pass

    elif "format" in userAns:
        path = filedialog.askdirectory()
        path = path[:2]
        print(path)
        format_partition_windows(path)
    
    elif "wifi password" in userAns:
        if platform.system() == 'Windows':
            talk("Fetching the saved wifi passwords.  Just a second sir!")
            time.sleep(1)
            data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode('utf-8', errors="backslashreplace").split("\n")
            profiles = [i.split(":")[1][1:-1] for i in data if  "All User Profile" in i]

            for i in profiles:
                try:
                    results = subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode('utf-8', errors="backslashreplace").split("\n")
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    try:
                        msgBox.insert(tkinter.END, f"{"{:<30}| {:<}".format(i, results[0])}\n")
                    except IndexError:
                        msgBox.insert(tkinter.END, f"{"{:<30}| {:<}".format(i, "")}\n")
                except subprocess.CalledProcessError:
                    msgBox.insert(tkinter.END, f"{"{:<30}: {:<}".format(i, "ENCODING ERROR")}\n")
        else:
            talk("This feature is not available in this operating system.")

    elif "youtube" in userAns:
        try:
            import pywhatkit
            song = userAns.replace("youtube ", "")
            botAns(f"Searching for {song}")
            pywhatkit.playonyt(song)
        except:
            playTrack("./src/voice/caged_network_lost_wifi.wav")
            pass

    elif "ip address" in userAns:
        talk("Checking")
        try:
            ipAdd = requests.get("https://api.ipify.org").text
            botAns("your ip adress is " + ipAdd)
            # messagebox.showinfo('IP Address', 'Your IP Address is: ' + ipAdd)
        except Exception as e:
            playTrack("./src/voice/caged_network_lost_wifi.wav")

    else:
        voiceList: list = [
            "./src/voice/caged_repeat_1.wav",
            "./src/voice/caged_repeat_2.wav",
            "./src/voice/caged_repeat_3.wav",
        ]
        playTrack(random.choice(voiceList))
    txtBox.delete(0, tkinter.END)


# time api
try:
    response = requests.get(
        "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Colombo"
    )
    if response.status_code == 200:
        data = response.json()
        current_time = data["time"]
        # botAns("Current time is: " + current_time)
        hour = int(current_time.split(":")[0])
        if hour >= 0 and hour < 12:
            # msg = "Good Morning, "
            playTrack("./src/voice/caged_listening_on_morning.wav")
            time.sleep(2)
            playTrack("./src/voice/caged_listening_on_6.wav")
            time.sleep(3)
            playTrack("./src/voice/caged_listening_on_3.wav")
        elif hour >= 12 and hour < 17:
            # msg = "Good Afternoon, "
            playTrack("./src/voice/caged_listening_on_afternoon.wav")
            time.sleep(2)
            playTrack("./src/voice/caged_listening_on_6.wav")
            time.sleep(3)
            playTrack("./src/voice/caged_listening_on_3.wav")
        elif hour >= 17 and hour < 22:
            playTrack("./src/voice/caged_listening_on_evening.wav")
            time.sleep(2)
            playTrack("./src/voice/caged_listening_on_6.wav")
            time.sleep(3)
            playTrack("./src/voice/caged_listening_on_3.wav")
        else:
            pass
        # talk(msg)
    else:
        botAns("Error: ", response.status_code)
except Exception as e:
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        # msg = "Good Morning, "
        playTrack("./src/voice/caged_listening_on_morning.wav")
        time.sleep(2)
        playTrack("./src/voice/caged_listening_on_6.wav")
        time.sleep(3)
        playTrack("./src/voice/caged_listening_on_3.wav")
    elif hour >= 12 and hour < 17:
        # msg = "Good Afternoon, "
        playTrack("./src/voice/caged_listening_on_afternoon.wav")
        time.sleep(2)
        playTrack("./src/voice/caged_listening_on_6.wav")
        time.sleep(3)
        playTrack("./src/voice/caged_listening_on_3.wav")
    elif hour >= 17 and hour < 20:
        playTrack("./src/voice/caged_listening_on_evening.wav")
        time.sleep(2)
        playTrack("./src/voice/caged_listening_on_6.wav")
        time.sleep(3)
        playTrack("./src/voice/caged_listening_on_3.wav")
    else:
        pass

# main window
root = ctk.CTk()
root.title("JARVIS Assistant")
width_of_window: int = 940
height_of_window: int = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = (screen_width / 2) - (width_of_window / 2)
y_cordinate = (screen_height / 2) - (height_of_window / 2)
root.geometry(
    "%dx%d+%d+%d" % (width_of_window, height_of_window, x_cordinate, y_cordinate)
)
root.resizable(0, 0)
root.iconbitmap("./src/ICON.ico")

# widgets
ctk.CTkLabel(root, text="MARK PC Assistant", font=("Times", 35)).pack(pady=20)

# Frames
frm1 = ctk.CTkFrame(root, width=280)
frm1.place(x=750, y=230)

frm2 = ctk.CTkFrame(root, width=200, height=130)
frm2.place(x=730, y=70)

frm3 = ctk.CTkFrame(root, width=600, height=550)
frm3.place(x=30, y=170)

frm4 = ctk.CTkFrame(root, width=500, height=90)
frm4.place(x=30, y=70)

# ============ PC Usages ============
ctk.CTkLabel(frm2, text="CPU :", font=("Poppins", 25)).place(x=5, y=10)
cpuLabel = ctk.CTkLabel(frm2, font=("Poppins", 25), text_color="red")
cpuLabel.place(x=120, y=10)
ctk.CTkLabel(frm2, text="Used RAM :", font=("Poppins", 20)).place(x=5, y=55)
ramLabel1 = ctk.CTkLabel(frm2, font=("Poppins", 20), text_color="green")
ramLabel1.place(x=120, y=55)

ctk.CTkLabel(frm2, text="Full RAM :", font=("Poppins", 20)).place(x=5, y=90)
ramLabel2 = ctk.CTkLabel(frm2, font=("Poppins", 20), text_color="green")
ramLabel2.place(x=120, y=90)
# ============  ============

# ============ Time ============
ctk.CTkLabel(frm4, text="Time :", font=("Poppins", 25)).place(x=170, y=10)
timeabel = ctk.CTkLabel(frm4, font=("DS-Digital", 30), text_color="red")
timeabel.place(x=250, y=10)

ctk.CTkLabel(frm4, text="Date :", font=("Poppins", 20)).place(x=5, y=55)
dateLabel = ctk.CTkLabel(frm4, font=("Poppins", 20), text_color="#ffff00")
dateLabel.place(x=70, y=55)

ctk.CTkLabel(frm4, text="Time Zone :", font=("Poppins", 20)).place(x=210, y=55)
timeZonelbl = ctk.CTkLabel(frm4, font=("Poppins", 20), text_color="green")
timeZonelbl.place(x=330, y=55)
# ============  ============

# ============ Input Box and Log area ============
msgBox = ctk.CTkTextbox(frm3, font=("Calibri", 17), width=600, height=250)
msgBox.pack(padx=5, pady=5)

txtBox = ctk.CTkEntry(frm3, font=("Calibri", 15), width=600)
txtBox.pack(pady=15, padx=5)
# ============  ============

# ============ Images ============
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "src")
volUP_image = ctk.CTkImage(
    Image.open(os.path.join(image_path, "volume-up.png")), size=(24, 24)
)
volDown_image = ctk.CTkImage(
    Image.open(os.path.join(image_path, "volume-down.png")), size=(24, 24)
)
shutdown_image = ctk.CTkImage(
    Image.open(os.path.join(image_path, "shutdown.png")), size=(24, 24)
)
resrart_image = ctk.CTkImage(
    Image.open(os.path.join(image_path, "restart.png")), size=(24, 24)
)
logOff_image = ctk.CTkImage(
    Image.open(os.path.join(image_path, "sign-out.png")), size=(24, 24)
)
lock_image = ctk.CTkImage(
    Image.open(os.path.join(image_path, "lock.png")), size=(24, 24)
)
# ============  ============

# ============ Buttons ============
volUpBtn = ctk.CTkButton(frm1, image=volUP_image, text="", command=volUp)
volUpBtn.pack(pady=10, padx=20)
volUpTooltip = CTkToolTip.CTkToolTip(volUpBtn, delay=0.1, message="Increase Volume")

volDownBtn = ctk.CTkButton(frm1, image=volDown_image, text="", command=volDown)
volDownBtn.pack(pady=10, padx=20)
volDownTooltip = CTkToolTip.CTkToolTip(volDownBtn, delay=0.1, message="Decrease Volume")

shutdownBtn = ctk.CTkButton(
    frm1, text="", image=shutdown_image, font=("Poppins", 15), command=shutdown
)
shutdownBtn.pack(pady=10, padx=20)
shutdownTooltip = CTkToolTip.CTkToolTip(
    shutdownBtn, delay=0.1, message="Shutdown you computer."
)

restartBtn = ctk.CTkButton(
    frm1, text="", image=resrart_image, font=("Poppins", 15), command=restart
)
restartBtn.pack(pady=10, padx=20)
restartTooltip = CTkToolTip.CTkToolTip(
    restartBtn, delay=0.1, message="Restart you computer."
)
logOffBtn = ctk.CTkButton(
    frm1, text="", image=logOff_image, font=("Poppins", 15), command=logOff
)
logOffBtn.pack(pady=10, padx=20)
logOffTooltip = CTkToolTip.CTkToolTip(
    logOffBtn, delay=0.1, message="Sign out from  your computer."
)
lockBtn = ctk.CTkButton(
    frm1, text="", image=lock_image, font=("Poppins", 15), command=lock
)
lockBtn.pack(pady=10, padx=20)
lockTooltip = CTkToolTip.CTkToolTip(lockBtn, delay=0.1, message="Lock  your computer.")
# ============  ============

# ============ Settings Menu ============

ctk.CTkButton(root, text="Settings", font=("Arial", 14), command=settingsPanel).place(x=30, y=500)

# ============  ============

# ============ Key Binding ============
root.bind("<Return>", run)
# ============  ============

# ============ Calling boot-up functions ============
updateCpuUtilization()
updateRamUsage1()
updateRamUsage2()
get_current_time()
# ============  ============


root.mainloop()
