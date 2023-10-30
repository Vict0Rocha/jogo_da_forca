import random
import sys


def palavras():  # Função para sortear uma palavra

    # Dicionario contendo todas as palavras
    palavra = {
        'animal': ['macaco', 'elefante', 'girafa'],
        'nome': ['victor', 'fabio', 'matheus'],
        'cor': ['azul', 'amarelo', 'branco', 'rosa', 'roxo'],
    }

    # Sorteando a chave e uma palvra do dict
    chave_sorteada = random.choice(list(palavra.keys()))
    palavra_sorteada = random.choice(palavra[chave_sorteada])

    print(f'Dica: {chave_sorteada.upper()}')

    return palavra_sorteada.upper()


print(23*'-')
print((4*' '), 'JOGO DA FORCA')
print(23*'-')
print('\nObjetivo: Tente adivinhar a palvra gerada.')
print('Regras: Você só pode digitar uma letra por vez, com o limite de 6 erro.\n')

loop = True

# while loop:
palavra = palavras()
palavra_letras = []

print('A palavra sorteada é... ')
for letra in palavra:
    print('_', end=' ')
    palavra_letras.append(letra)

print(palavra)
print('\n')
palpite = input('Digite seu palpite <<< ').upper()

if palpite in palavra:
    print('Ok')
else:
    print('erro')
