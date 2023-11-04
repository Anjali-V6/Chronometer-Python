import datetime
from playsound import playsound

h=int(input("hour "))
m=int(input("min "))
arp=input("am or pm ")

if arp=="pm":
    h+=12

while True:
    if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
        print("playsound")
        playsound("music.mp3")
        break
    else:
        continue

    
