import emoji
from time import sleep
from random import randint
cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m'}

emojis = {1: emoji.emojize(":rock:"),
            2: emoji.emojize(":page_facing_up:"),
            3: emoji.emojize(":scissors:")}

print(f'{cores["verde"]}' + '-'*20)
print('Jokenpô')
print('-'*20 + f'{cores["limpa"]}')
sleep(0.25)
print(f'{cores["amarelo"]}Vou escolher minha jogada. Tente me derrotar...{cores["limpa"]}')
sleep(1)
sorteio = randint (1,3)
print('-=' *10)
print(f'{cores["amarelo"]}Escolhas do Jokenpô:{cores["limpa"]}')
print(f'{cores["vermelho"]}1{cores["limpa"]} para {emojis[1]}')
print(f'{cores["vermelho"]}2{cores["limpa"]} para {emojis[2]}')
print(f'{cores["vermelho"]}3{cores["limpa"]} para {emojis[3]}')
print('-='*10)
sleep(1.25)
escolha = input(f'{cores["verde"]}Qual foi a sua escolha?{cores["limpa"]}').strip()
sleep(0.25)
if  not escolha.isdigit():
    print(f'{cores["vermelho"]}ERRO. Nenhuma jogada selecionada.{cores["limpa"]}')
    exit()

escolha = int(escolha)

if escolha not in (1, 2, 3):
      print(f'{cores["vermelho"]}ERRO. Nenhuma jogada selecionada.{cores["limpa"]}')
      exit()
else:
    print(f'{cores["vermelho"]}JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('PÔ!' + f'{cores["limpa"]}')
    sleep(0.25)
    
if escolha == 1 and sorteio == 2 or (escolha == 2 and sorteio == 3) or (escolha == 3 and sorteio == 1):
        print(f'Minha jogada: {emojis[sorteio]}.\nSua jogada:{emojis[escolha]}\n{cores["vermelho"]}Você perdeu!{cores["limpa"]}')
elif escolha ==1 and sorteio ==3 or (escolha ==2 and sorteio==1) or (escolha==3 and sorteio==2):
        print(f'Minha jogada: {emojis[sorteio]}.\nSua jogada:{emojis[escolha]}\n{cores["verde"]}Você me venceu!{cores["limpa"]}')
elif escolha == sorteio:
        print(f'Minha jogada: {emojis[sorteio]}.\nSua jogada:{emojis[escolha]}\n{cores["amarelo"]}Empate!{cores["limpa"]}')
else:
      print(f'{cores["vermelho"]}ERRO. Nenhuma jogada selecionada.{cores["limpa"]}')


