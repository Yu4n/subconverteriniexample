import base64
import json

with open('VmsLines.txt', 'r') as f:
    urls = [base64.b64decode(line.strip()[8:]).decode("utf-8") for line in f]
i = 1
for url in urls:
    url = json.loads(url)
    url["ps"] = url["ps"][:3] + str(i)
    url = json.dumps(url, ensure_ascii=False)
    i += 1
    url = base64.b64encode(bytes(url, "utf-8"))
    print("vmess://" + url.decode())
