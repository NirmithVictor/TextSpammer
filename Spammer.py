import pyautogui
import time
a=input("Enter Your Message:")
b=int(input("Enter Number Of Times You Wanna Spam:"))
time.sleep(5)
for i in range(b):
    pyautogui.typewrite(a+'\n')
