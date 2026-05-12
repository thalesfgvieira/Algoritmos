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

decimo_termo = primeiro_termo + (10-1) * razao

for c in range (primeiro_termo, decimo_termo + razao, razao):
    print(c, end= ' -> ')
print(f'{cores["vermelho"]}FIM{cores["limpa"]}')