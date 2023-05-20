

import psutil
import datetime

booted_up = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime  \
            ("%H:%M"+" on "+"%A %d-%B-%Y")

print("you booted this session at:", booted_up)



print ("Developed by Abdulrahman Alharbi")