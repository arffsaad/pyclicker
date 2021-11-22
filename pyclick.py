from os import system
from time import sleep

import mouse
import keyboard


def clicker(x):
    print("[+] Clicking in 3 seconds")
    sleep(3)
    print("[!] Press Insert to stop")
    while True:
           sleep(x)
           mouse.click(button='left')
           if (keyboard.is_pressed('insert')):
               break
    print("[+] Stopping...")
    
    
def setspeed(speed):
    x = speed
    print("[!] Enter time interval per click (current interval: ", x, "s)")
    x = input(">>")
    return float(x)
    
speed = 0.0005

while True:
    system("cls")
    print("Pyclicker v1.0 by ssl2k")
    print("MAIN MENU")
    print("[1] Start clicker\n[2] Set clicker speed (current speed: ", speed, "s/click)")
    menu = input(">>")
    if (menu == "1"):
        while True:
            system("cls")
            sleep(1)
            print("[!] Press Insert to start clicking!\n[!] Press 'Q' to quit to menu")
            k = keyboard.read_key(suppress=False)
            if (k == 'q'):
                break
            elif (k == 'insert'):
                clicker(speed)
                sleep(1)
            else:
                print("[-] Wrong key!")
                sleep(1)
                keyboard.send('backspace')
    if (menu == "2"):
        system("cls")
        speed = setspeed(speed)
    else:
        print("[-] Wrong input!")
                
        
