import datetime
h=int(input("hour "))
m=int(input("min "))
arp=input("am or pm ")

if arp=="pm":
    h+=12

while True:
    if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute:
        print("alarm")
        break
    else:
        continue
