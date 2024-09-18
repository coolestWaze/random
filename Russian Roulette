try:
    import random

    print("Bem-Vindo a roleta russa!")
    print("Existem 5 numeros que te fazem ganhar, e um 1 que te faz perder.")
    n1 = int(input("digite um numero de 1 a 6 para jogar, e 0 para sair do jogo. "))
    listy = [1, 2, 3, 4, 5, 6]
    randy = random.choice(listy)
    if n1 < 0 or n1 > 6:
        print('digite apenas um valor de 1 a 6')
    elif n1 == 0:
        print('Voce saiu do jogo.')
    elif n1 == randy:
        print('Bang! Voce perdeu!')
    else:
        print(f'Wow! voce sobreviveu! A bala estava no número {randy}')
except ValueError:
    print('digite um número aceitável')
