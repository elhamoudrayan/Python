import email
from mechanize import Link
import pyautogui as pt
from time import sleep
import time
import keyboard
import random
import win32api, win32con
Mousespeed =0.2

email=['']         #list of email u have here

link="https://www.youtube.com/c/Freecodecamp"   #LINK FOR THE CHANNEL YOU WANNA SUB TO HERE
time.sleep(2)
for email in email:
    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/chrome.png', confidence=.6)
    pt.moveTo(x, y, Mousespeed)
    pt.click()

    time.sleep(2)

    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/search.png', confidence=.6)
    pt.moveTo(x, y, Mousespeed)
    pt.click()
    pt.typewrite(link)
    pt.press('Enter')


    time.sleep(5)

    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/sub.png', confidence=.6)
    pt.moveTo(x, y, Mousespeed)
    pt.click()

    time.sleep(5)

    pt.click(x=1370, y=690, interval=Mousespeed)


    time.sleep(5)

    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/email.png', confidence=.6)
    pt.moveTo(x, y, Mousespeed)
    pt.click()
    pt.typewrite(email)



    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/nextg.png', confidence=.6)
    pt.moveTo(x, y, Mousespeed)
    pt.click()

    time.sleep(2)

    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/pass.png', confidence=.6)
    pt.moveTo(x, y, Mousespeed)
    pt.click()
    pt.typewrite('M.H.2003')  #emails password here NOTE IF THE EMAILS DOSENT HAVE THE SAME PASSWORD IT IS NOT GOING TO WORK

    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/nextg.png', confidence=.6)
    pt.moveTo(x, y, Mousespeed)
    pt.click()

    time.sleep(6)


    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/puz.png', confidence=.9)
    pt.moveTo(x, y, Mousespeed)
    pt.moveRel(-300, 0)
    pt.click()
    pt.typewrite(link)
    pt.press('Enter')

    time.sleep(4)

    pt.moveTo(1800, 110, Mousespeed)
    pt.click()


    time.sleep(3)

    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/sub.png', confidence=.6)
    pt.moveTo(x, y, Mousespeed)
    pt.click()

    time.sleep(2)


    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/puz.png', confidence=.8)
    pt.moveTo(x, y, Mousespeed)
    pt.moveRel(90,0)
    pt.click()

    time.sleep(2)

    pt.moveRel(-50,500)
    pt.click()

    time.sleep(4)

    pt.moveTo(900, 600, Mousespeed)
    pt.click()


    pt.moveTo(800, 500, Mousespeed)
    pt.click()

    x, y = pt.locateCenterOnScreen('C:/Users/Admin/Desktop/code/youtube pyautogui/yesremove.png', confidence=.7)
    pt.moveTo(x, y, Mousespeed)
    pt.click()


    pt.moveTo(1980,0)
    pt.click()


    #IF YOUR LANGUAGE IS DIFFERENT THEN ARABIC-ENGLISH IT IS NOT GONNA WORK TOO BECAUSE IT IS USING PYAUTOGUI CHECK THE PHOTOS TO AMKE UR OWN CHANGES