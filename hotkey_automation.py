import tkinter as tk
from tkinter import simpledialog, Tk
import time
import pyautogui
import keyboard

#input GUI for credentials and client's names

def vinput(title, prompt, width, height):
    root = Tk()
    root.withdraw()
    user_input = simpledialog.askstring(title, prompt)
    return user_input

#Send keystroke functions to go into the required fields

def thanks():
    pyautogui.write("Thank you,\n")
    pyautogui.write("AIROS Support (Traevon B)")
    keyboard.add_hotkey("command+t", thanks)

#use the keyboard module to simulate hotkeys on windows 
# The Hot key bindings

def hotkeys():
    keyboard.add_hotkey("command+a", lambda: vinput("User's name:", 300, 100))

#usage code

if __name__ == "__main__":
    response = vinput("User's name:","Input the user's credentials", 300, 100)
print(response)

#keep the script running to listen fo key inputs

# keyboard.wait("esc")      (this is real code but is commented out.)