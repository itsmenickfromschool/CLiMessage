import pyautogui as pg
import time

x = pg.position()[0]
y = pg.position()[1]
# pg.PAUSE = 2
# print(pg.PAUSE)
# print(f"({x} ,{y})")

# print(pg.position())
# print(pg.PAUSE)
# print(pg.FAILSAFE)


def confirmSend():
    person = input("Enter the contact you want to text: ")
    message = input(f"\nEnter your message to {person}: ")
    while True:
        res = input(f"Are you sure you want to send {person} the following message: \n\n {message}\n\n (Y/N?): ")
        if res in ['yes','y','true','ye','t']:
            return True
        elif res in ['no','n','false','quit','f']:
            return False
        else:
            print("Please enter a valid response (yes/no)")


# On Mac OS the command key needs to be pressed before the other key in the hotkeys, adding in this interval solved a bug where it would simply just type a space before command and not exectue the script
def sendTextMessage():
    pg.hotkey('command', 'space', interval=0.125)
    pg.typewrite('messages\n')

sendTextMessage()

# if confirmSend():
#     sendTextMessage(person, message)

    
  