from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'limpa': '\033[m'}

print(f'{cores["verde"]}{"=-"*20}')
print('Tabuada de um Número')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.25)

while True:
    try:
        contador = 1
        num = int(input('Digite um número inteiro para ver sua tabuada (número negativo para finalizar o programa): '))
        if num < 0:
            break
        else:
            print('Criando a tabuada...')
            sleep(0.5)
            print('=-'*20)

            while contador <= 10:
                print(f'{num} x {contador:2} = {num*contador}')
                contador += 1
            print('=-'*20)
    except ValueError:
        print(f'{cores["vermelho"]}ERRO. Tente digitar um número inteiro.{cores["limpa"]}')

print(f'{cores["vermelho"]}FIM{cores["limpa"]}')
