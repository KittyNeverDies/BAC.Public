#   T E M P
#   F I L E
#   L O G G E R
#   Start This File then your game install
#   It needs ListDlls
from subprocess import check_output
import os
import psutil
strings = 0
target = "proc.exe"      # Change File Name here


def kill(a):
    for d in psutil.process_iter():
        if d.name() == a:
            d.kill()


def get():
    os.popen(target)
    out = check_output("listdlls proc", shell=True)    # change proc to your File Name
    temp = ""
    mass = list(str(out))
    b = []
    for i in range(0, len(mass)):
        if i + 1 != len(mass) and i + 2 != len(mass) and i + 3 != len(mass):
            if str(mass[i]) != "\\" and str(mass[i + 1]) != "r" or str(mass[i]) == "\\" and str(mass[i + 1]) != "r":
                temp = temp + str(mass[i])
            else:
                b.append(temp)
                temp = " "


f = open("log.txt", "w")         # change to your log with path file (Example  C://Windows//)
f.write(str(strings))
f.close()
p = os.popen('attrib +h ' + f)                  # Working Only Windows
t = p.read()                                    # (if you want hide file log search code for your system)
p.close()
kill(target)
