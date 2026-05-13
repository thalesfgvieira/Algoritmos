from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'limpa': '\033[m'}

print(f'{cores["verde"]}{"=-"*20}')
print('Leitor de Palíndromo')
print(f'{"=-"*20}{cores["limpa"]}')

try:   
    frase = str(input('Digite uma frase qualquer: ')).strip().upper()
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Tente usar letras.{cores["limpa"]}')
    exit()

palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''

for letra in range(len(juntar)-1, -1 , -1):
    inverso += juntar[letra]

if inverso == juntar:
    print(f'{cores["verde"]}{juntar} -> {inverso}{cores["limpa"]}. Achamos um palíndromo!')
else:
    print(f'{cores["vermelho"]}{juntar} -> {inverso}{cores["limpa"]}. Não é palíndromo!')

