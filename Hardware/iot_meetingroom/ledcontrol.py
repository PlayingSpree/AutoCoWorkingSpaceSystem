import os

def light_ON():
    os.system('irsend SEND_ONCE ledremote KEY_ON')
    
def light_OFF():
    os.system('irsend SEND_ONCE ledremote KEY_OFF')
    
def light_UP():
    os.system('irsend SEND_ONCE ledremote KEY_UP')
    
def light_DOWN():
    os.system('irsend SEND_ONCE ledremote KEY_DOWN')

while True:
    commandIn = input("Enter Command : ")
    if commandIn == "on":
        light_ON()
    elif commandIn == "off":
        light_OFF()
    elif commandIn == "up":
        light_UP()
    elif commandIn == "down":
        light_DOWN()

    
    