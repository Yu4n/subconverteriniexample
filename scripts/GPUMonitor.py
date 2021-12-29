import datetime
import os
import time

import GPUtil

gpu = GPUtil.getGPUs()[0]
load = gpu.load * 100
i = 0
while True:
    if i >= 6:
        os.system(f'''curl -F chat_id=341795952 -F text="{load}, {datetime.datetime.now()}" https://api.telegram.org/bot1473272910:AAHHYndU7yQRfFWqtcpW6QDyRQ3ujWHQt_o/sendMessage --proxy 127.0.0.1:7890''')
        i = 0
    if load < 50:
        os.system(f'''curl -F chat_id=341795952 -F text="{load}" https://api.telegram.org/bot1473272910:AAHHYndU7yQRfFWqtcpW6QDyRQ3ujWHQt_o/sendMessage --proxy 127.0.0.1:7890''')
        os.system("shutdown /r /t 1")
    time.sleep(600)
    i += 1
