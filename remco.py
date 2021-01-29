import time #bibliotēka importēšana
from datetime import datetime as dt #bibliotēkas specifikācija
host_path = "/etc/hosts" #faiļa atrašanas vietas norādīšana
redirect = "127.0.0.1" #norādam uz kurieniem novirzam klientu
website_list = ["www.youtube.com", "youtube.com", "www.facebook.com", "facebook.com"] #lietotņu sarakstu definēšana

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,12): # if funkcija salīdzina ar lokāla datora laiku
        print("Vel vajag pastrādāt") #rezultāta izvade
        file = open(host_path,"r+") #definējam tiesības mapei ar read
        content = file.read()
        for website in website_list: #funkcija ierakstu meklēšanai
            if website in content: 
                pass #ja ir ignorējam
            else:
                file.write(redirect + " " + website + "\n") #ja iestājās pretējais kritērijs, ierakstam vērtibas
    else:
        print("Atpūšamies") #ja laiks nesakrīt izvada šo
        file = open(host_path,'r+') #definējam tiesības mapei ar read
        content = file.readlines() 
        file.seek(0) #funkcija pārbauda vai ir kaut kādi ieraksti no weblist
        for line in content: #norāda ko jādara ja ir
            if not any(website in line for website in website_list): #nosakam kritēriju ko meklēt
                file.write(line) #iedodam vajadzīgas tiesības
            file.truncate() #izdzēšam
    time.sleep(5) #snoozy funkciaj
