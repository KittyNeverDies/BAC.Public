from subprocess import check_output
import subprocess
import time
import os
import psutil
def kill(a):
    procces = a
    for d in psutil.process_iter():
        if d.name() == procces:
            d.kill()
def protect():
    while True:
        out = check_output("listdlls procc", shell=True)    # change to your procces file
        temp = ""
        mass = list(str(out))
        b = []
        for i in range(0, len(mass)):
            if i + 1 != len(mass) and i + 2 != len(mass) and i + 3 != len(mass):
                if str(mass[i]) != "\\" and str(mass[i + 1]) != "r" or str(mass[i]) == "\\" and str(mass[i + 1]) != "r":
                    temp = temp + str(mass[i])
                else:
                    b.append(temp)
                    temp = ""
        strings = len(b)
        print(strings)
        if strings != int(original):
            print("BAC | Inject Detect , Closing procces...")
            kill(target)
            exit()
            break


target = "procc.exe"             #   change to your procces
#if os.path.isfile("First.py"):      # change to your temp file
 #   os.remove("First.py")           # change to your temp file
if not os.path.isfile("log.txt"):   # change to your collect file
    kill(target)
    exit()
with open("log.txt") as f:  # change to your collect file
    original = f.read()
while True:
    time.sleep(5)
    for n in psutil.process_iter():
        if n.name() == target:
            protect()
            break
