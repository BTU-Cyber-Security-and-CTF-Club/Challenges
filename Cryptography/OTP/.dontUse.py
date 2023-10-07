import random
import string
from random import randrange

randomFlag = ''
for num in range(25):
    c = randrange(9)
    if c <= 4:
        randomFlag += random.choice(string.ascii_letters)
    elif c <= 6 and c >= 4:
        randomFlag += random.choice(string.digits)
    elif c <= 8 and c >= 6:
        randomFlag += random.choice(random.choice('_-+=!~/'))

flag = f'BTU{ {randomFlag} }'.replace("'", '')

