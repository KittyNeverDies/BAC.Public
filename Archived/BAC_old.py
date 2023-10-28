from subprocess import check_output
import time
import os
# target = "RobloxPlayerBeta"
out = check_output("listdlls RobloxPlayerBeta")
mass = list(str(out))
print(mass)
all = []
temp = ""
for i in range(0, len(mass)):
    if i+1 != len(mass) and i+2 != len(mass) and i+3 != len(mass):
        if str(mass[i]) != "\\" and str(mass[i+1]) != "r" or str(mass[i]) == "\\" and str(mass[i+1]) != "r":
            temp = temp + str(mass[i])
        else:
            print("dsgasd")
            all.append(temp)
            temp = ""
print(all)
print(out)
print(len(out))
while True:
    out = check_output("listdlls RobloxPlayerBeta", shell=True)
    if len(out) == 121:
        print("Error | Matching Procces Not Found")
        time.sleep(5)
    elif len(out) != 9269:
        print("BAC | Inject Detect , Closing procces...")
       # os.sys("taskkill RobloxPlayerBeta")
        break
