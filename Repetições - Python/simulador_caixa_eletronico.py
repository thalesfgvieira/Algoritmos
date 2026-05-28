from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'limpa': '\033[m'}

print(f'{cores["verde"]}{"=-"*20}')
print('Caixa Eletrônico')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.5)

try:
    valor_a_sacar = int(input('Qual valor você quer sacar? R$ '))
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Tente digitar um número inteiro.{cores["limpa"]}')
    exit()
print()

total = valor_a_sacar
cedula = 50
total_cedula = 0


while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        print(f'Total de {cores["amarelo"]}{total_cedula}{cores["limpa"]} cédulas de {cores["azul"]}R$ {cedula}{cores["limpa"]}')
        total_cedula = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break

print(f'{cores["verde"]}{"=-"*20}{cores["limpa"]}')
