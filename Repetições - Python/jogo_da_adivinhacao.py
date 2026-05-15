from random import randint
from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'limpa': '\033[m'}

print(f'{cores["amarelo"]}{"=-"*20}')
print('Jogo da Adivinhação')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.5)

tentativas = 0
acertou = False

print(f'{cores["azul"]}Vou pensar em um número entre 0 e 10. Tente adivinhar...{cores["limpa"]}')
numero = randint(0,10)

sleep(1)

while not acertou:
    try:
        jogador = int(input(f'{cores["azul"]}Em que número eu pensei? {cores["limpa"]}'))
    
        if jogador < 0 or jogador > 10:
            print(f'{cores["vermelho"]}Digite um número entre 0 e 10.{cores["limpa"]}')
        else:
            print('Processando...')
            sleep(1)
            tentativas += 1    
            if jogador == numero:
                acertou = True
            elif jogador < numero:
                print(f'{cores["vermelho"]}Mais... tente novamente. {cores["limpa"]}')
            else:
                print(f'{cores["vermelho"]}Menos... tente novamente. {cores["limpa"]}')
        
    except ValueError:
        print(f'{cores["vermelho"]}ERRO. Tente digitar um número inteiro.{cores["limpa"]}')
        
print(f'{cores["verde"]}Acertou! Pensamos no número {numero}!')
print(f'Número de tentativas: {tentativas}{cores["limpa"]}')

    

