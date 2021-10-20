import random
lines = open('VmsLines.txt').readlines()
random.shuffle(lines)
wt = open('VmsLines.txt', 'w').writelines(lines)
