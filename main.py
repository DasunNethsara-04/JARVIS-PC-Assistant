# imports
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import PySimpleGUI as sg
from PIL import Image
import pyautogui, datetime, messages, pyttsx3, tkinter, pygame, random, psutil, time, os, requests

# theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# text 2 speech
engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("rate", 174)
engine.setProperty("volume", 2.0)

pygame.mixer.init()


# functions
def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def playTrack(songClip):
    pygame.mixer.music.load(songClip)
    pygame.mixer.music.play()


def shutdown():
    playTrack("./src/voice/caged_sleep_0.wav")
    time.sleep(3)
    playTrack("./src/voice/caged_sleep_2.wav")
    os.system("shutdown.exe -s -t 00")


def restart():
    playTrack("./src/voice/caged_sleep_0.wav")
    time.sleep(3)
    playTrack("./src/voice/caged_sleep_2.wav")
    os.system("shutdown.exe -s -t 00")


def logOff():
    talk(random.choice(messages.ok))
    os.system("shutdown.exe -l")


def lock():
    # talk(random.choice(messages.ok))
    lst: list = [
        "./src/voice/caged_confirm_4.wav",
        "./src/voice/caged_confirm_5.wav",
        "./src/voice/caged_confirm_9.wav",
    ]
    playTrack(random.choice(lst))
    time.sleep(1)
    os.system("rundll32.exe user32.dll, LockWorkStation")


def volDown():
    # talk(random.choice(messages.ok))
    pyautogui.press("volumedown")


def volUp():
    # talk(random.choice(messages.ok))
    pyautogui.press("volumeup")


def updateCpuUtilization() -> float:
    util = psutil.cpu_percent()
    cpuLabel.configure(text=f"{util}%")
    cpuLabel.after(1000, updateCpuUtilization)


def updateRamUsage() -> float:
    used = round((psutil.virtual_memory().used) / (1024**3), 2)
    total = round((psutil.virtual_memory().total) / (1024**3), 2)
    ramLabel.configure(text=f"{used}GB / {total}GB")
    ramLabel.after(1000, updateRamUsage)


def botAns(text):
    msgBox.insert(tkinter.END, text=f"JARVIS: {text}\n")
    talk(text)


def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


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
                if (
                    int(current_time.split(":")[0]) >= 0
                    and int(current_time.split(":")[0]) < 12
                ):
                    amPM = "AM"
                else:
                    amPM = "PM"
                botAns("Current time is: " + current_time + amPM)

            else:
                botAns("Error: ", response.status_code)
        except Exception as e:
            playTrack("./src/voice/caged_network_lost_wifi.wav")

    elif "date" in userAns:
        botAns("Today is " + str(datetime.date.today()) + " sir.")

    elif "about you" in userAns:
        botAns(
            "Hello sir! I am JARVIS. Your PC Assistant. JARVIS stands for, Just A Rather Very Intelligent System. I am here to assist you with the varieties tasks is best I can."
        )
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
root.title("JARVIS Asistant")
width_of_window: int = 940
height_of_window: int = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = (screen_width / 2) - (width_of_window / 2)
y_cordinate = (screen_height / 2) - (height_of_window / 2)
root.geometry(
    "%dx%d+%d+%d" % (width_of_window, height_of_window, x_cordinate, y_cordinate)
)
# root.resizable(0, 0)
root.iconbitmap("./src/ICON.ico")

# widgets
ctk.CTkLabel(root, text="JARVIS PC Asistant", font=("Times", 35)).pack(pady=20)

# Frames
frm1 = ctk.CTkFrame(root, width=280)
frm1.place(x=750, y=230)

frm2 = ctk.CTkFrame(root, width=280, height=130)
frm2.place(x=650, y=70)

frm3 = ctk.CTkFrame(root, width=600, height=550)
frm3.place(x=30, y=150)

ctk.CTkLabel(frm2, text="CPU :", font=("Poppins", 25)).place(x=5, y=30)
cpuLabel = ctk.CTkLabel(frm2, font=("Poppins", 25), text_color="red")
cpuLabel.place(x=75, y=30)
ctk.CTkLabel(frm2, text="RAM :", font=("Poppins", 25)).place(x=5, y=75)
ramLabel = ctk.CTkLabel(frm2, font=("Poppins", 25), text_color="green")
ramLabel.place(x=75, y=75)

msgBox = ctk.CTkTextbox(frm3, font=("Calibri", 17), width=600, height=250)
msgBox.pack(padx=5, pady=5)

txtBox = ctk.CTkEntry(frm3, font=("Calibri", 15), width=600)
txtBox.pack(pady=25, padx=5)
# images
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "src")
volUP_image = ctk.CTkImage(
    Image.open(os.path.join(image_path, "volume-up.png")), size=(24, 24)
)
volDown_image = ctk.CTkImage(
    Image.open(os.path.join(image_path, "volume-down.png")), size=(24, 24)
)
send_image = ctk.CTkImage(
    Image.open(os.path.join(image_path, "send.png")), size=(48, 48)
)

# frm2 = ctk.CTkFrame(root)
# frm2.pack(pady=20, padx=50)
ctk.CTkButton(frm1, image=volUP_image, text="", command=volUp).pack(pady=10, padx=20)
ctk.CTkButton(frm1, image=volDown_image, text="", command=volDown).pack(
    pady=10, padx=20
)
ctk.CTkButton(frm1, text="Shutdown", font=("Poppins", 15), command=shutdown).pack(
    pady=10, padx=20
)
ctk.CTkButton(frm1, text="Restart", font=("Poppins", 15), command=restart).pack(
    pady=10, padx=20
)
ctk.CTkButton(frm1, text="Log Off", font=("Poppins", 15), command=logOff).pack(
    pady=10, padx=20
)
ctk.CTkButton(frm1, text="Lock", font=("Poppins", 15), command=lock).pack(
    pady=10, padx=20
)

appearance_mode_optionemenu = ctk.CTkOptionMenu(
    root,
    values=["Dark", "Light", "System"],
    command=change_appearance_mode_event,
)
appearance_mode_optionemenu.place(x=30, y=500)

root.bind("<Return>", run)
updateCpuUtilization()
updateRamUsage()
root.mainloop()
