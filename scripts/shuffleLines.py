import random
lines = open('VmsLines.txt').readlines()
for i in range(5):
    random.shuffle(lines)
wt = open('VmsLines.txt', 'w').writelines(lines)
