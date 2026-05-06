from time import sleep

cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m'}

print('-'*20)
print('Analisar Preço do Produto')
print('-'*20)

sleep(0.5)

try:
    preco = float(input('Digite o preço base do produto: R$'))
except ValueError:
    print(f'{cores["vermelho"]}ERRO. Digite um valor numérico válido.{cores["limpa"]}')
    exit()


print(f'{cores["amarelo"]}Condições de pagamento:{cores["limpa"]}')
print(f'0 para {cores["verde"]}à vista dinheiro/cheque{cores["limpa"]}')
print(f'1 para {cores["verde"]}à vista no cartão{cores["limpa"]}')
print(f'2 para {cores["verde"]}em até 2x no cartão (sem juros){cores["limpa"]}')
print(f'3 para {cores["verde"]}3x ou mais no cartão (20% de juros){cores["limpa"]}')

sleep(1)

condicao = (input('Escolha a condição de pagamento: '))

if condicao.isdigit():
    condicao = int(condicao)
else:
    print(f'{cores["vermelho"]}ERRO. Digite apenas números válidos.{cores["limpa"]}')
    exit()

if condicao == 0:
    print(f'O produto custará {cores["amarelo"]}R${preco*0.90:.2f}{cores["limpa"]} ao receber um desconto de 10% pelo pagamento {cores["verde"]}à vista dinheiro/cheque.{cores["limpa"]}')
elif condicao == 1:
    print(f'O produto custará {cores["amarelo"]}R${preco*0.95:.2f}{cores["limpa"]} após o desconto de 5% pelo pagamento {cores["verde"]}à vista no cartão.{cores["limpa"]}')
elif condicao == 2:
    print(f'O produto custará {cores["amarelo"]}R${preco:.2f}{cores["limpa"]}, não recebendo promoções ao realizar o pagamento de {cores["verde"]}em até 2x no cartão.{cores["limpa"]}')
elif condicao == 3:
    print(f'O produto custará {cores["amarelo"]}R${preco*1.20:.2f}{cores["limpa"]} após receber um aumento de 20% de juros ao realizar o {cores["verde"]}pagamento parcelado de 3x ou mais no cartão.{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}ERRO. Escolha uma opção entre 0 e 3.{cores["limpa"]}')
