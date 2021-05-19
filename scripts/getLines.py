with open('LinesToGet.txt', "r", encoding='utf-8') as text_file:
    lines = text_file.readlines()
    for i in range(0, 25):
        print(lines[7 + 111 * i], end='')
