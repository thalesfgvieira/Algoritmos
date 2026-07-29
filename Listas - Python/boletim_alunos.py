from time import sleep
dados_gerais = []
continuar = ' '
print(f'{"=-"*20}')
print(f'{"BOLETIM DOS ALUNOS":^40}')
print(f'{"=-"* 20}')

while continuar not in 'N':
    nome = str(input('Digite o nome do aluno: '))
    nota_1 = float(input('Forneça a Nota 1: '))
    nota_2 = float(input('Forneça a Nota 2: '))
    dados_aluno = [nome, nota_1, nota_2]
    dados_gerais.append(dados_aluno)
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print(f'{"=-"*20}')

print(f'{"No.":<5}{"NOME":<19}MÉDIA')
print(f'{"--"*15}')

for i in range (0, len(dados_gerais)):
        media = (dados_gerais[i][1] + dados_gerais[i][2]) / 2
        print(f'{i:<5}{dados_gerais[i][0]:<20}{(media):.1f}')

print(f'{"--"*15}')
print(f'{"=-"*20}')

escolha = -1

while escolha != 999:
  escolha = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
  print(f'{"--"*15}')
  if escolha == 999:
    break
  else:
    if escolha in range (0, len(dados_gerais)):
      print(f'Notas de {dados_gerais[escolha][0]}: {dados_gerais[escolha][1]} e {dados_gerais[escolha][2]}.')
      print(f'{"--"*15}')
    else:
      print('Inválido, aluno inexistente.')
      exit()
      
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')