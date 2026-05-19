from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'limpa': '\033[m'}

print(f'{cores["amarelo"]}{"=-"*60}')
print('Vou ler vários números inteiros. Após isso, mostrarei a média entre todos os valores, assim como o maior e menor valor.')
print(f'{"=-"*60}{cores["limpa"]}')
sleep(0.5)

try:
    numero = int(input('Digite um número inteiro: '))
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Tente digitar um número INTEIRO.{cores["limpa"]}')
    exit()

soma = numero
total = 1
maior = numero
menor = numero
finalizar_programa = False

while not finalizar_programa:
    continuar = str(input(f'{cores["amarelo"]}Deseja continuar?{cores["limpa"]} ')).strip().upper() [0]
    if continuar in 'N':
        finalizar_programa = True
    elif continuar in 'S':
        try:
            numero = int(input('Digite outro número inteiro: '))
            soma += numero
            total += 1
            if numero > maior:
                maior = numero
            elif numero < menor:
                menor = numero
        except ValueError:
            print(f'{cores["vermelho"]}ERRO. Tente digitar um número INTEIRO.{cores["limpa"]}')
    else:
        print(f'{cores["vermelho"]}ERRO. Tente digitar "Sim" ou "Não" ("s" ou "n"){cores["limpa"]}')

media = soma/total
print(f'{cores["verde"]}Média entre os valores digitados: {media:.2f}\nMaior valor: {maior}\nMenor valor: {menor}{cores["limpa"]}')