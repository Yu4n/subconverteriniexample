import base64
import requests

with open('v2ray.txt', 'r') as f:
    urls = [line.strip() for line in f]
# open("VmsLines.txt", 'w').close()  # Clear content
wt = open("VmsLines.txt", 'a', encoding='utf-8')
i = 0
for url in urls:
    try:
        c = requests.get(url)
        lines = str(base64.b64decode(c.text).decode()).split('\n')[:-1]
    except UnicodeDecodeError or requests.exceptions.SSLError:
        continue
    else:
        if lines[i] and len(lines[i]) > 10:
            wt.write(lines[i] + '\n')
            print(lines[i])
        if i == len(lines) - 1:
            i -= 4
        else:
            i += 1
wt.close()
