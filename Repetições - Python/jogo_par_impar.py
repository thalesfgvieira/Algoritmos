from time import sleep
from random import randint

cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m'}

print(f'{cores["vermelho"]}{"=-"*15}')
print('Vamos jogar Par ou Ímpar!')
print(f'{"=-"*15}{cores["limpa"]}')
sleep(0.5)

vitorias = 0

while True:
    numero_jogador = int(input('Digite um número entre 1 a 10: '))
    numero_computador = randint (1,10)
    soma = numero_jogador + numero_computador
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper() [0]
        print(f'{cores["vermelho"]}{"=-"*20}')
    sleep(0.5)

    print(f'{cores["amarelo"]}Você jogou {numero_jogador} e o computador {numero_computador}. Total de {soma} deu {cores["limpa"]}', end='')

    if soma % 2 == 0:
        print(f'{cores["verde"]}PAR{cores["limpa"]}')
    else:
        print(f'{cores["verde"]}ÍMPAR{cores["limpa"]}')
    
    print(f'{cores["vermelho"]}{"=-"*20}')
    sleep(1)

    if par_impar == 'P':
        if soma % 2 == 0:
            vitorias += 1
            print(f'{cores["verde"]}Você VENCEU!{cores["limpa"]}\n{cores["amarelo"]}Vamos jogar novamente...{cores["limpa"]}')
            print(f'{cores["vermelho"]}{"=-"*15}{cores["limpa"]}')
            sleep(1)
        else:
            print(f'{cores["vermelho"]}Você PERDEU!{cores["limpa"]}')
            break

    elif par_impar == 'I':
        if soma % 2 == 1:
            vitorias += 1
            print(f'{cores["verde"]}Você VENCEU!{cores["limpa"]}\n{cores["amarelo"]}Vamos jogar novamente...{cores["limpa"]}')
            print(f'{cores["vermelho"]}{"=-"*15}{cores["limpa"]}')
            sleep(1)
        else:
            print(f'{cores["vermelho"]}Você PERDEU!{cores["limpa"]}')
            break
print(f'{cores["verde"]}Total de vitórias: {vitorias}.{cores["limpa"]}')

