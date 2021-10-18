import random
lines = open('VmsLines.txt').readlines()
print(lines)
random.shuffle(lines)
wt = open('VmsLines.txt', 'w').writelines(lines)
