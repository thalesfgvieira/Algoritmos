from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'limpa': '\033[m'}

print(f'{cores["verde"]}{"=-"*20}')
print('Tabuada de um Número')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.25)

try:
    num = int(input('Digite o número que você escolheu para montar a tabuada: '))
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Digite um número inteiro{cores["limpa"]}.')
    exit()

print()
print('Criando a tabuada...')
sleep(0.5)

print('=-'*20)

for c in range (1,11):

    print(f'{num} x {c:<2}= {(num * c):2}')

print('=-' *20)

