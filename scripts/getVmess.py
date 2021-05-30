import base64
import requests

with open('v2ray.txt', 'r') as f:
    urls = [line.strip() for line in f]
open("VmsLines.txt", 'w').close()
wt = open("VmsLines.txt", 'a', encoding='utf-8')
i = 0
for url in urls:
    c = requests.get(url)
    lines = str(base64.b64decode(c.text).decode()).split('\n')
    if len(lines[i]) > 10:
        wt.write(lines[i] + '\n')
        print(lines[i])
    if i > 22:
        i -= 5
    else:
        i += 1
wt.close()
