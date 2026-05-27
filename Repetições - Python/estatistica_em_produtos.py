from time import sleep

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'limpa': '\033[m'}

print(f'{cores["azul"]}{"=-"*20}')
print('Leitor de Preço e Nome')
print(f'{"=-"*20}{cores["limpa"]}')
sleep(0.5)

total_gasto = 0
produto_mais_barato = ' '
preco_mais_barato = 0
total_maior_1000 = 0

while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip()
    preco = float(input('Informe o preço do produto: R$ '))
    
    total_gasto += preco

    if preco_mais_barato == 0:
        preco_mais_barato = preco
        produto_mais_barato = nome_produto

    elif preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome_produto

    if preco > 1000:
        total_maior_1000 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip() [0]
        
    if continuar == 'N':
        print(f'{cores["amarelo"]}{"=-"*20}{cores["limpa"]}')
        print(f'{cores["vermelho"]}FIM{cores["limpa"]}')
        break
    else:
        print(f'{cores["amarelo"]}{"=-"*20}{cores["limpa"]}')

print(f'{cores["amarelo"]}{"=-"*20}{cores["limpa"]}')

print(f'{cores["azul"]}Total gasto na compra: R$ {total_gasto:.2f}\nTotal de produtos que custam mais de R$ 1000: {total_maior_1000}\nProduto mais barato: {produto_mais_barato}, custando R$ {preco_mais_barato:.2f} {cores["limpa"]}')