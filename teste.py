import random
import sys


def palavras():  # Função para sortea uma palavra

    # Dicionario contendo todas as palavras
    palavra = {
        'animal': ['Macaco', 'elefante', 'girafa'],
        'nome': ['Victor', 'fabio', 'matheus'],
        'cor': ['Azul', 'amarelo', 'branco', 'rosa', 'roxo'],
    }

    # Sorteando a chave e uma palvra do dict
    chave_sorteada = random.choice(list(palavra.keys()))
    palavra_sorteada = random.choice(palavra[chave_sorteada])

    return print(f'A dica é {chave_sorteada} e a palavra é {palavra_sorteada}')


print(23*'-')
print((4*' '), 'JOGO DA FORCA')
print(23*'-')

print('\nObjetivo: Tente adivinhar a palvra gerada.')
print('Regras: Você só pode digitar uma letra por vez, com o limite de 6 erros. ')

print()
palavras()
