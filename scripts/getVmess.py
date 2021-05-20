import base64
import requests

with open('v2ray.txt', 'r') as f:
    urls = [line.strip() for line in f]
open("VmsLines.txt", 'w').close()
wt = open("VmsLines.txt", 'a', encoding='utf-8')
i = 0
for url in urls:
    c = requests.get(url)
    lines = str(base64.b64decode(c.text)).split('\\n')
    if len(lines[i]) > 10:
        wt.write(lines[i] + '\n')
        print(lines[i])
    else:
        wt.write(lines[i - 1] + '\n')
        print(lines[i - 1])
    if i >= 24:
        i = 20
    else:
        i += 1
wt.close()
