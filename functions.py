import subprocess
import time
import pygame
import os
import PySimpleGUI as sg
import random
import pyautogui

pygame.mixer.init()


def format_partition_windows(partition):
    """Format the selected partition"""
    playTrack("./src/voice/caged_trs11.wav")
    time.sleep(7)
    # Create a subprocess and pipe input/output
    p = subprocess.Popen(
        ["format", partition, "/FS:NTFS", "/Q"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )
    # Provide input to the subprocess (e.g., 'Y' to confirm formatting)
    p.communicate(input=b"Y\n")
    # Wait for the subprocess to finish
    p.wait()
    playTrack("./src/voice/caged_confirm_6.wav")
    sg.popup_notify(
        f"The drive was formatted successfully, ensuring a clean slate for future use.",
        title="Done",
    )


# functions
def playTrack(songClip):
    pygame.mixer.music.load(songClip)
    pygame.mixer.music.play()


def shutdown():
    playTrack("./src/voice/caged_sleep_0.wav")
    time.sleep(3)
    playTrack("./src/voice/caged_sleep_2.wav")
    # os.system("shutdown.exe -s -t 00")


def restart():
    playTrack("./src/voice/caged_sleep_0.wav")
    time.sleep(3)
    playTrack("./src/voice/caged_sleep_2.wav")
    # os.system("shutdown.exe -s -t 00")


def lock():
    # talk(random.choice(messages.ok))
    lst: list = [
        "./src/voice/caged_confirm_4.wav",
        "./src/voice/caged_confirm_5.wav",
        "./src/voice/caged_confirm_9.wav",
    ]
    playTrack(random.choice(lst))
    time.sleep(1)
    # os.system("rundll32.exe user32.dll, LockWorkStation")


def volDown():
    # talk(random.choice(messages.ok))
    pyautogui.press("volumedown")


def volUp():
    # talk(random.choice(messages.ok))
    pyautogui.press("volumeup")
