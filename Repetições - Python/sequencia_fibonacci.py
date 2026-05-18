from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m',
         'limpa': '\033[m'}

print(f'{cores["amarelo"]}{"=-"*20}')
print('Sequência de Fibonacci')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.5)

try:
    numero_elementos = int(input('Digite um n número inteiro. Mostrarei os n primeiros elementos da sequência de Fibonacci: '))
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Digite um número inteiro.{cores["limpa"]}')
    exit()

if numero_elementos == 0 or numero_elementos == 1:
    print(f'{cores["vermelho"]}0{cores["limpa"]}')
    exit()

if numero_elementos < 0:
    print(f'{cores["vermelho"]}ERRO. Digite um número positivo.{cores["limpa"]}')
    exit()

primeiro_elemento = 0
segundo_elemento = 1
print(f'{primeiro_elemento} -> {segundo_elemento}', end=' -> ')
contador = 3

while contador <= numero_elementos:
   proximo_elemento = primeiro_elemento + segundo_elemento
   print(f'{proximo_elemento}', end=' -> ')
   primeiro_elemento = segundo_elemento
   segundo_elemento = proximo_elemento
   contador += 1
print(f'{cores["vermelho"]}FIM{cores["limpa"]}')
    