#!python
import subprocess
import time
from datetime import datetime
import psutil
import os
import signal

_=os.system("clear")
print("Battery log running")

file = open("Battery.txt","a")
file.write("Time Battery% CPU% Voltage" + '\n')
file.close()

i = 0

try:
    while True:
        #i < 1
        
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        cmd = 'pmset -g batt | grep -Eo "\d+%" | cut -d% -f1'
        ps = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0]

        cmd2 = 'system_profiler SPPowerDataType | grep Voltage'
        ps = subprocess.Popen(
            cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        batt = ps.communicate()[0]

        a = output.decode("utf-8")
        b = a.replace("b'", "")
        c = b.replace("\n"," ")
        
        batt2 = batt.decode("utf-8")
        batt3 = batt2.replace("      Voltage (mV): ", "")

        file = open("Battery.txt","a")  
        file.write(current_time + " " + c + str(psutil.cpu_percent()) + " " + str(batt3))
        file.close()
        _=os.system("clear")
        print(current_time + " " + c + str(psutil.cpu_percent()) + " " + str(batt3))

        time.sleep(60)
except KeyboardInterrupt:
    #stop
    file.close()
    print(" End")
