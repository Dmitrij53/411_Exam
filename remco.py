import time
from datetime import datetime as dt
host_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.youtube.com", "youtube.com", "www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,12):
        print("Vel vajag pastrādāt")
        file = open(host_path,"r+")
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
    else:
        print("Atpūšamies")
        file = open(host_path,'r+')
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
            file.truncate()
    time.sleep(5)