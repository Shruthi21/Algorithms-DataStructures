#!/bin/python

import sys
from datetime import time
hour=0
minute=0
sec=0


time = raw_input().strip()
if time[8:] == 'PM':
    hour=12
    hour = hour + int(time[0:2])    
    minute = minute+ int(time[3:5])
    sec = sec + int(time[6:8])
else:

    hour = hour + int(time[0:2])
    minute = minute+ int(time[3:5])
    sec = sec + int(time[6:8])

print hour
print minute,sec
    
time(hour,minute,sec,0).isoformat()
    

