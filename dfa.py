from time import sleep

import pyautogui as pag

DIRECTORY = "assets/DFA/"
def clickImage(fileName, offsetX=0, offsetY=0):
    location = pag.locateCenterOnScreen(DIRECTORY + fileName, confidence=0.8)
    while(location == None):
        location = pag.locateCenterOnScreen(DIRECTORY + fileName, confidence=0.8)
    pag.click(x=location.x + offsetX, y=location.y + offsetY)

def sub1():
    sleep(1)
    pag.typewrite("https://www.passport.gov.ph/appointment/group/schedule?index=1")
    pag.hotkey("enter")
    clickImage("1_checkbox.png")
    clickImage("2_button.png")
    clickImage("3_choice.png")
    pag.hotkey("down")
    pag.hotkey("enter")
    sleep(1)
    pag.hotkey("tab")
    pag.hotkey("tab")
    pag.hotkey("enter")
    sleep(2)
    clickImage("6_choose.png")
    sleep(2)

TOPS_SITE_COUNT = 13
def main():
    pag.hotkey("winleft")
    pag.typewrite("Chrome")
    sleep(2)

    pag.hotkey("enter")
    sub1()

    pag.hotkey("down")
    pag.hotkey("enter")
    clickImage("7_checkbox.png")
    pag.hotkey("tab")
    pag.hotkey("enter")

    for i in range(TOPS_SITE_COUNT):
        clickImage("9_siteChooser.png", 100, 30)
        pag.hotkey("down")
        pag.hotkey("enter")
        sleep(1)
    pag.hotkey("ctrl", "t")
    sleep(0.5)
    pag.hotkey("ctrl", "l")

    #next batch, none TOPS site
    sub1()
    for i in range(TOPS_SITE_COUNT + 1):
        pag.hotkey("down")
    pag.hotkey("enter")
    sleep(1)
    pag.hotkey("tab")
    sleep(1)
    pag.hotkey("tab")
    sleep(1)
    pag.hotkey("space")
    sleep(1)
    pag.hotkey("tab")
    sleep(1)
    pag.hotkey("enter")

    for i in range(40):
        clickImage("9_siteChooser.png", 100, 30)
        pag.hotkey("down")
        pag.hotkey("enter")
        sleep(1)


main()