from time import sleep

cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m'}

print(f'{cores["amarelo"]}' + '-'*20)
print('Conversor de Bases Numéricas')
print('-'*20 + f'{cores["limpa"]}')
num = input(f'{cores["verde"]}Digite um número inteiro qualquer:{cores["limpa"]}').strip()
if num.isdigit():
    num = int(num)
else:
    print(f'{cores["vermelho"]}Inválido. Tente digitar um número.{cores["limpa"]}')
    exit()
sleep(0.5)
print(f'''{cores["azul"]}Escolha uma das bases para conversão:{cores["limpa"]}
      {cores["roxo"]}[ 1 ] converter para BINÁRIO{cores["limpa"]}
      {cores["ciano"]}[ 2 ] converter para OCTAL{cores["limpa"]}
      {cores["vermelho"]}[ 3 ] converter para HEXADECIMAL{cores["limpa"]}''')
sleep(1.25)
opcao = input('Sua escolha:').strip()
if opcao.isdigit():
    opcao = int(opcao)
else:
    print(f'{cores["vermelho"]}Inválido. Tente digitar um número.{cores["limpa"]}')
    exit()
if opcao == 1:
    print(f'{cores["verde"]}{num}{cores["limpa"]} convertido para {cores["roxo"]}BINÁRIO{cores["limpa"]} é igual a {cores["roxo"]}{bin(num) [2:]}{cores["limpa"]}.')
elif opcao == 2:
    print(f'{cores["verde"]}{num}{cores["limpa"]} convertido para {cores["ciano"]}OCTAL{cores["limpa"]} é igual a {cores["ciano"]}{oct(num) [2:]}{cores["limpa"]}.')
elif opcao == 3:
    print(f'{cores["verde"]}{num}{cores["limpa"]} convertido para {cores["vermelho"]}HEXADECIMAL{cores["limpa"]} é igual a {cores["vermelho"]}{hex(num)[2:]}{cores["limpa"]}.')
else:
    print(f'{cores["vermelho"]}Inválido. Nenhuma opção selecionada.{cores["limpa"]}')
    exit()


