from ast import If
from playsound import playsound
from datetime import datetime

now_time = datetime.now()
now_hour = now_time.strftime("%I")
now_minute = now_time.strftime("%M")
now_second = now_time.strftime("%S")
now_period = now_time.strftime("%p")
print(now_hour,":",now_minute, ":",now_second, " ", now_period)

alarm_time = input("Enter alarm in format set:HH:MM:SS AM/PM\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Input time is = ",alarm_hour,":",alarm_minute, ":",alarm_second, " ", alarm_period)

while True:
    now_time = datetime.now()
    now_hour = now_time.strftime("%I")
    now_minute = now_time.strftime("%M")
    now_second = now_time.strftime("%S")
    now_period = now_time.strftime("%p")
    print(now_hour,":",now_minute, ":",now_second, " ", now_period)
    if(alarm_period == now_period):
        if(alarm_hour == now_hour):
            if(alarm_minute == now_minute):
                if(alarm_second == now_second):
                    print("wake up")
                    break



    
    