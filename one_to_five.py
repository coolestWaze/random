try:
    from random import choice

    n1 = int(input("adivinhe um numero de 1 a 5 "))
    list = ('1', '2', '3', '4', '5')
    rand = choice(list)
    if n1 == int(rand):
        print('voce acertou!')
    elif n1 > 5:
        print('digite um valor apenas até 5.')
    else:
        print('voce errou.')
    print (rand)
except ValueError:
    print('digite um valor aceitável.')
