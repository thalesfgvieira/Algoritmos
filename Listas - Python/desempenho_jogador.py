lista_jogadores = []
continuar = ' '
while continuar not in "N":
    dados_jogador = {}
    dados_jogador["Nome"] = str(input('Digite o nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {dados_jogador["Nome"]} jogou? '))

    gols_lista = []
    for c in range (1,partidas+1):
        num_gols = int(input(f'Quantos gols na partida {c}? '))
        gols_lista.append(num_gols)
    dados_jogador["Gols"] = gols_lista
    dados_jogador["Total de Gols"] = sum(gols_lista)
    lista_jogadores.append(dados_jogador.copy())
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar in "S":
        print(f'{"--"*20}')
print(f'{"=-"*35}')

print(f'{"No.":<5}{"NOME":<19}{"GOLS":<24}TOTAL')
print(f'{"--"*30}')
for c in range (1,len(lista_jogadores)+1):
    print(f'{c:<5}{lista_jogadores[c-1]["Nome"]:<15}{str(lista_jogadores[c-1]["Gols"]):<30}{lista_jogadores[c-1]["Total de Gols"]}')
print(f'{"--"*30}')

mostrar = -1
while mostrar != 999:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para finalizar): '))
    if mostrar == 999:
        break
    else:
        if mostrar not in range (1,len(lista_jogadores)+1):
            print('Inválido. Digite o código correto (1,2,3...)')
        else:
            print()
            print(f'    Levantamento do Jogador: {lista_jogadores[mostrar-1]["Nome"]}')
            for partida, gols in enumerate(lista_jogadores[mostrar - 1]["Gols"]):
                print(f'    Na partida {partida+1}, fez {gols} gols.')
        print(f'{"--"*30}')
print('<< VOLTE SEMPRE >>')
