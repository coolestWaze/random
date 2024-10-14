import random
print("Welcome to python coin flip")
cont = 0
h = 0
t = 0
x = int(input('Digit some number to roll the coin (-1 to leave)'))
coin = random.randint(0, 1)
if coin == 1:
    print('Tails')
    cont+=1
    t+=1
else:
    print("Heads")
    cont+=1
    t+=1
while x != -1:
    x = int(input('Digit some number to roll the coin (-1 to leave)'))
    if x == -1:
        print('Finished.')
        break
    else:
        coin = random.randint(0, 1)
        if coin == 1:
            print('Tails')
            cont+=1
            t+=1
        else:
            print("Heads")
            cont+=1
            h+=1

print(f'You have played it {cont} times.')
print(f'You got {h} heads and {t} tails.')
