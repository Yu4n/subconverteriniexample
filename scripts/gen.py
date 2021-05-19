import re
import base64

a = 'https://api.suda.cat/sub?target=v2ray&url=https%3A%2F%2Fsuda.sub.koicloud.pw%2Flink%2F'
c = '%3Fsub%3D3%26extend%3D1&config=https%3A//raw.githubusercontent.com/Yu4n/subconverteriniexample/master/Minimalist.ini&include=1.0%7C0.8%7C0.2&emoji=false'

with open('gen.txt', "r", encoding='utf-8') as text_file:  # Put html source code into gen.txt
    f = text_file.read()
    m = re.findall('link/(.+?)\?sub=3', f)  # Two markers to locate the substring
    if m:
        for x in m:
            print(a + x + c)
            wt = open('v2ray.txt', 'a')  # clash.txt is the output
            wt.write(a + x + c + '\n')
            wt.close()

            # message = a + x + c
            # message_bytes = message.encode('ascii')
            # base64_bytes = base64.b64encode(message_bytes)
            # base64_message = base64_bytes.decode('ascii')
            # print("sub://" + base64_message)
            # wt = open('base64.txt', 'a')
            # wt.write("sub://" + base64_message + '\n')
            # wt.close()
