from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'limpa': '\033[m'}

print(f'{cores["verde"]}{"=-"*20}')
print('Leitor de Número Primo')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.5)

try:
    num = int(input('Digite um número inteiro: '))
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Tente digitar um número inteiro.{cores["limpa"]}')
    exit()

print('Analisando...')
sleep(0.5)

primo = True

if num <=1:
    primo = False
else:

    for c in range(2, num):
        if num % c == 0:
            primo = False
            break
if primo:
    print(f'O número {num} é {cores["verde"]}PRIMO{cores["limpa"]}.')
else:
    print(f'O número {num} {cores["vermelho"]}NÃO{cores["limpa"]} é primo.')
       

