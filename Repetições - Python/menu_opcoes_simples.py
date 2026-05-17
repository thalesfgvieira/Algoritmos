from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m',
         'limpa': '\033[m'}

print(f'{cores["amarelo"]}{"=-"*20}')
print('Menu de Opções')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.5)
print()

try:
    primeiro_numero = float(input((f'{cores["azul"]}Digite o 1° valor: {cores["limpa"]}')))
    segundo_numero = float(input(f'{cores["azul"]}Digite o 2° valor: {cores["limpa"]}'))
    print()
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Tente digitar um número.{cores["limpa"]}')
    exit()

soma = primeiro_numero + segundo_numero
multiplicar = primeiro_numero * segundo_numero
sair_programa = False

sleep(0.25)
print(f'{cores["amarelo"]}{"=-"*20}')
print(f'Opções de Escolha:{cores["limpa"]}')
print(f'''{cores["ciano"]}[1]{cores["limpa"]} para somar os valores;
{cores["roxo"]}[2]{cores["limpa"]} para multiplicar os valores;
{cores["verde"]}[3]{cores["limpa"]} para ver o maior valor;
{cores["amarelo"]}[4]{cores["limpa"]} para fazer uma nova escolha;
{cores["vermelho"]}[5]{cores["limpa"]} para sair do programa.''')

while not sair_programa:
    try:
        escolha = int(input('Escolha sua opção: '))
        if escolha < 1 or escolha > 5:
            print(f'{cores["vermelho"]}ERRO. Tente digitar entre 1 e 5.{cores["limpa"]}')
        else:
            if escolha == 1:
                print(f'{cores["ciano"]}A soma entre {primeiro_numero} e {segundo_numero} é {soma}.{cores["limpa"]}')
            elif escolha == 2:
                print(f'{cores["roxo"]}A multiplicação entre {primeiro_numero} e {segundo_numero} vale {multiplicar:.2f}.{cores["limpa"]}')
            elif escolha == 3:
                if primeiro_numero > segundo_numero:
                    print(f'{cores["verde"]}O maior valor é {primeiro_numero}{cores["limpa"]}')
                elif primeiro_numero < segundo_numero:
                    print(f'{cores["verde"]}O maior valor é {segundo_numero}{cores["limpa"]}')
                else:
                    print(f'{cores["verde"]}Os dois valores são iguais.{cores["limpa"]}')
            elif escolha == 4:
                try:
                    primeiro_numero = float(input((f'{cores["azul"]}Digite o 1° valor: {cores["limpa"]}')))
                    segundo_numero = float(input(f'{cores["azul"]}Digite o 2° valor: {cores["limpa"]}'))
                    soma = primeiro_numero + segundo_numero
                    multiplicar = primeiro_numero * segundo_numero
                except ValueError:
                    print(f'{cores["vermelho"]}ERRO. Digite um valor válido. {cores["limpa"]}')
            elif escolha == 5:
                print(f'{cores["vermelho"]}Adeus!{cores["limpa"]}')
                sair_programa = True
    except ValueError:
        print(f'{cores["vermelho"]}ERRO. Digite um valor válido. {cores["limpa"]}')




