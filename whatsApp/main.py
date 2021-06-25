import pyautogui as pt
from time import sleep
import pyperclip
import random


sleep(3)

position1 = pt.locateOnScreen("paperclip.PNG", confidence= .6)
x = position1[0]
y = position1[1]

def group_identify():


    try:
        positionGroup = pt.locateOnScreen("plus.PNG", confidence=.6)
        groupX = positionGroup[0]
        groupY = positionGroup[1]
        pt.moveTo(groupX + 220, groupY +20, duration=.5)
       # pt.click()
    except(Exception):
        print(Exception, "down")

def txt_message_identify():
    try:
        print(pt.pixel(int(x + 58), int(y - 35)))
        if pt.pixelMatchesColor(int(x + 85), int(y - 35), (255, 255, 255), tolerance=10):
            print("white")
            processed_message = process_response(get_text_msg())
            post_response(processed_message)

        else:
            print("no new messages")

    except(Exception):
        print("no msg")

def new_messages():

    try:
        positionDown = pt.locateOnScreen("down.PNG", confidence= .6)
        downX = positionDown[0]
        downY = positionDown[1]
        pt.moveTo(downX + 20, downY +20, duration=.5)
        pt.click()
    except(Exception):
        print(Exception, "down")

#get msg

def get_text_msg():
    global x, y


    position = pt.locateOnScreen("paperclip.PNG", confidence=.6)
    x=position[0]
    y=position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 85, y - 35, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()

    waMsg=pyperclip.paste()

    pt.click()
    print("Message recieved: " + waMsg)

    return waMsg





#posts

def post_response(message):
    global x,y
    position = pt.locateOnScreen("paperclip.PNG", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x +200, y + 20, duration=0.5)
    pt.click()
    pt.typewrite(message,interval=.01)

    pt.typewrite("\n", interval= .01)



#process the response

def process_response(message):
    random_no = random.randrange(3)

    if "who are you" in str(message).lower() or "your name" in str(message).lower() or "hii" in str(message).lower() or "hey" in str(message).lower() or "ade" in str(message).lower() :
        return "Hii! I am WhatsApp Bot. I am my Master's personal assistant. He is busy right now. How can I help you?"
    elif "gm" in str(message).lower() or "good morning" in str(message).lower():
        return "Hii! I am WhatsApp Bot. I like to say good morning to you for my Master"
    elif "help" in str(message).lower():
        return "keywords:- \n \t gm, good morning \n \t who are you,your name,hii,hey \n \t how old is he \n \t . \n \t help"
    elif "@my Master" in str(message).lower():
        return "Hey I am WhatsApp Bot. He is busy right now. How can I help you"




#check for new msg
def check_for_new_message():
    txt_message_identify()
    pt.moveTo(x +200, y + 20, duration=0.5)
    while True:
        try:
            position = pt.locateOnScreen("greendot.PNG", confidence =.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                txt_message_identify()
                #sleep(2)

        except(Exception):
            print("No new messages")






        new_messages()
        txt_message_identify()






check_for_new_message()

