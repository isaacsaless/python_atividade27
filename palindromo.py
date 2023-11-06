# Exercício Python 27: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. DICA: VEJA SOBRE FUNÇÃO REPLACE(), LOWER() E UMA FORMA DE INVERTER OS CARACTERES. 

print('Descubra se uma frase ou palavra é um palíndromo.')
texto =  str(input('Digite uma frase ou palavra: '))
texto = texto.lower().replace(" ", "")

texto2 = texto.lower() [::-1]
texto2 = texto2.replace(" ", "")

if texto == texto2:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')