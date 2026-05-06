from time import sleep

cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m'}

print('-'*20)
print('Analisador de Triângulos')
print('-'*20)

sleep (1)

try:
    a = float(input('Digite o comprimento de um segmento A: '))

    b = float(input('Digite o comprimento de um segmento B: '))

    c = float(input('Digite o comprimento de um segmento C: '))
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Digite valores numéricos válidos.{cores["limpa"]}')
    exit()

print('Analisando...')

sleep(1)

if a < b + c and b < a+c and c < a + b:
    print(f'{cores["verde"]}Os segmentos A, B e C formam um triângulo!{cores["limpa"]}')
    if a == b == c: 
        print(f'{cores["verde"]}Tipo de triângulo: Equilátero.{cores["limpa"]}')
    elif a == b or a == c or b == c:
        print(f'{cores["verde"]}Tipo de triângulo: Isósceles.{cores["limpa"]}')
    else:
        print(f'{cores["verde"]}Tipo de triângulo: Escaleno.{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}Os segmentos A, B e C NÃO formam um triângulo!{cores["limpa"]}')
