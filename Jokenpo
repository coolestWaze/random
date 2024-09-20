from random import randint
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']

esc = int(input('Escolha sua jogada (1 - Pedra, 2 - Papel, 3 - Tesoura): '))

print('Jo!')
sleep(0.5)
print('Ken!')
sleep(0.5)
print('PO!!!')

comp = randint(1, 3)

print(f'Você jogou: {itens[esc - 1]}')
print(f'O computador jogou: {itens[comp - 1]}')

if esc == comp:
    print('Empate!')
elif (esc == 1 and comp == 3) or (esc == 2 and comp == 1) or (esc == 3 and comp == 2):
    print('Você ganhou!')
else:
    print('Você perdeu!')
