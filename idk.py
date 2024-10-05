import random
listdmg = [1, 1, 2]
rlist = random.choice(listdmg)
dmg = random.randint(12, 15)
x = 100
y = random.randint(10, 15)
def global_sum():
    global x
    if rlist == 1:
        x -= dmg
    else:
        x-=y
global_sum()
print(x)
