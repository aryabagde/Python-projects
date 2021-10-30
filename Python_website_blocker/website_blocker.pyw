import time
from datetime import datetime as dt

hosts_temp=r"E:\Python\mega_projects\Website blocker\hosts"#dummy file of host to check and run
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"#after adding original hosts,run it as cmd administrator
websites=['www.facebook.com','facebook.com','www.myntra.com','myntra.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write("127.0.0.1"+" "+ website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()

    time.sleep(5)
