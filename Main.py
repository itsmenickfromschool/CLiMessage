import pyautogui as pg
import time
import os


# ************* TO USE THIS PROGRAM 
# must be on macOS
# run in terminal, also must install dependencies in the pipenv or locally
#
def terminalPrompt():
    person = input("Enter the contact you want to text: ")
    message = input(f"\nEnter your message to {person}: ")
    while True:
        res = input(f"\n\n\nAre you sure you want to send {person} the following message: \n\n {message}\n\n (Y/N?): ")
        if res in ['yes','y','true','ye','t']:
            confirmation = True
            return confirmation, person, message
        elif res in ['no','n','false','quit','f']:
            confirmation = False
            return confirmation, person, message
        else:
            print("Please enter a valid response (yes/no)")


# On Mac OS the command key needs to be pressed before the other key in the hotkeys, adding in this interval solved a bug where it would simply just type a space before command and not exectue the script

def sendMessage(person, message):
    pg.hotkey('command', 'space', interval=0.125)
    pg.typewrite('messages\n')
    time.sleep(1)
    button = pg.locateCenterOnScreen('./newMessage.png', confidence=0.8) #newMessage is btn screenshot we are aiming
    print(button)
    pg.leftClick(x=button[0],y=button[1])
    pg.typewrite(person)
    time.sleep(.5)
    pg.press('\n')
    time.sleep(.5)
    pg.press('\t')
    pg.typewrite(message)
    time.sleep(.5)
    pg.press('\n')
  
confirmation, person, message = terminalPrompt()
if confirmation:
    time.sleep(1)
    sendMessage(person=person, message=message )

    
  