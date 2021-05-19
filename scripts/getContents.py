import requests
with open('clash.txt', 'r') as f:
    urls = [line.strip() for line in f]
open("LinesToGet.txt", 'w').close()
wt = open("LinesToGet.txt", 'a', encoding='utf-8')
for x in urls:
    c = requests.get(x)
    wt.write(c.text)
wt.close()
