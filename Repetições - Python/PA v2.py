from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'limpa': '\033[m'}

print(f'{cores["verde"]}{"=-"*20}')
print('Progressão Aritmética')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.5)

try:
    primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
    razao = int(input('Digite a razão da PA: '))
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Tente digitar um número inteiro.{cores["limpa"]}')
    exit()

print('Mostrando os 10 primeiros termos da PA...')
sleep(1)

termo = primeiro_termo
contador = 1
total_termo = 0
mais_termos = 10

while mais_termos != 0:
    total_termo += mais_termos
    while contador <= total_termo:
        print(f'{termo}', end=' -> ')
        termo += razao
        contador += 1
    print(f'{cores["vermelho"]}PAUSA{cores["limpa"]}')
    mais_termos = int(input('Quantos termos a mais você quer mostrar na PA? Digite 0 para finalizar a progressão: '))
print(f'{cores["verde"]}Progressão finalizada com {total_termo} termos mostrados.{cores["limpa"]}')

    

