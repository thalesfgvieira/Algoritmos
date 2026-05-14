from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'limpa': '\033[m'}

print(f'{cores["verde"]}{"=-"*20}')
print('Leitor de Nomes, Idades e Sexos')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.5)
print()

nome_mais_velho = ''
idade_mais_velho = 0
mulher_menor_20 = 0
maior_idade = 0
soma_idade = 0
num_homem = 0
num_mulher = 0

try:
    for c in range (1,5):
        nome = str(input('Digite o nome: ')).strip()
        idade = int(input('Digite a idade: '))
        soma_idade += idade
        print()
        sexo = str(input(f'''{cores["vermelho"]}Escolha o sexo:{cores["limpa"]}

{cores["azul"]}'M' para masculino{cores["limpa"]}
{cores["amarelo"]}'F' para feminino{cores["limpa"]}
                     
Digite a sua escolha: ''')).strip().upper()
        print()
        if sexo == 'M':
            num_homem += 1
            if c == 1:
                idade = maior_idade
                nome_mais_velho = nome
            elif idade > maior_idade:
                maior_idade = idade
                nome_mais_velho = nome

        elif sexo == 'F':
            num_mulher += 1
            if idade < 20:
                mulher_menor_20 += 1
        else:
            print(f'{cores["vermelho"]}ERRO. Digite um valor válido.{cores["limpa"]}')
            exit()
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Digite um valor válido.{cores["limpa"]}')

media = soma_idade/4

print(f'''{cores["verde"]}Média de idade: {media}{cores["limpa"]}
{cores["azul"]}Nome do homem mais velho: {nome_mais_velho}{cores["limpa"]}
{cores["amarelo"]}Número de mulheres com menos de 20 anos: {mulher_menor_20}{cores["limpa"]}''')