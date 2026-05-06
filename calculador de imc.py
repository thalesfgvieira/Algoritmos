from time import sleep

print('-'*20)
print('Analisador de IMC')
print('-'*20)

sleep(0.5)

peso = float(input('Digite seu peso, em kg: '))
altura = float(input('Digite sua altura, em m: '))

imc = peso/(altura**2)

sleep(0.5)

print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc < 30:
    print('Você está em sobrepeso.')
elif imc < 40:
    print('Você está obeso.')
else:
    print('Você está em obesidade mórbida.')
