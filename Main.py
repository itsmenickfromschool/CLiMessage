import pyautogui
import time

x = pyautogui.position()[0]
y = pyautogui.position()[1]
print(f"({x} ,{y})")

print(pyautogui.position())
print(pyautogui.PAUSE)
print(pyautogui.FAILSAFE)

person = input("Enter the contact you want to text: ")
message = input(f"\nEnter your message to {person}: ")

def confirmSend():
    while True:
        res = input(f"Are you sure you want to send {person} the following message: \n {message}\n\n Type yes/no to continue...")
        if res in ['yes','y','true','ye','t']:
            return True
        elif res in ['no','n','false','quit','f']:
            return False
        else:
            print("Please enter a valid response (yes/no)")

confirmSend()
# def sendTextMessage(person, message):
    
