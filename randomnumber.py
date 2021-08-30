import random

def randomNumber() :
    list = []
    while len(list) < 10:
        r = random.randint(1,10)
        if r not in list :
            list.append(r)
    return list

print(randomNumber())
