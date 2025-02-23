#!/usr/bin/env python3

import psutil

import time

import os


if not os.path.exists("logs"):

    os.makedirs("logs")        #check if a logs dir exist, if not makes one


log_file = "logs/monitor.log"

def log_system_stats() :

    with open(log_file,"a") as f:

        cpu_usage = psutil.cpu_percent(interval = 1)   #CPU utilisation
        
        f.write(f"CPU Usage : {cpu_usage}%\n")



        memory = psutil.virtual_memory()
        
        f.write(f"Memory Usage : {memory.percent}%\n")  #Memory Utilisation



        disk = psutil.disk_usage("/")
        
        f.write(f"Disk Usage : {disk.percent}%\n")      #Disk Usage         



        f.write("="*40 + "\n")

while True:

    log_system_stats()



    print("Logged system stats.....")

    time.sleep(15)


