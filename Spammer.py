import pyautogui
import time
a=input("Enter Your Message:")
b=int(input("Enter Number Of Times You Wanna Spam:"))


Timecounter=5
while(Timecounter!=0):
    time.sleep(1)
    print(Timecounter)
    Timecounter=Timecounter-1
time.sleep(1.5)
print("Sayanora Motherfucker")

for i in range(b):
    pyautogui.typewrite(a+'\n')
