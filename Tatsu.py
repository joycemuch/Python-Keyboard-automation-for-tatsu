#Run after every 3hours
import pyautogui
import time

def train(num):
  count = 0
  while count< num:
     time.sleep(4)
     text = '!tg train'
     pyautogui.PAUSE = 0.10

     chartlist = {i for i in text}
     for i in text:
        pyautogui.typewrite(i)
     pyautogui.press('enter')
     count = count + 1

def slots(num):
  count = 0
  while count< num:
     time.sleep(4)
     text = "!slots"
     pyautogui.PAUSE = 0.10

     chartlist = {i for i in text}
     for i in text:
        pyautogui.typewrite(i)
     pyautogui.press('enter')
     count = count + 1


train(172)
slots(172) #you can change the number to your liking


  #print("3hrs passed")
  #time.sleep(10800)