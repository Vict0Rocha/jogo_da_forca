import random
import sys


def palavras_sorteada():  # Função para sortear uma palavra

    # Dicionario contendo todas as palavras
    palavra = {
        'animal': ['macaco', 'elefante', 'girafa'],
        'nome': ['victor', 'fabio', 'matheus'],
        'cor': ['azul', 'amarelo', 'branco', 'rosa', 'roxo'],
        'fruta': ['abacaxi', 'uva', 'banana'],
    }

    # Sorteando a chave e uma palvra do dict
    chave_sorteada = random.choice(list(palavra.keys()))
    palavra_sorteada = random.choice(palavra[chave_sorteada])

    print(f'Dica: {chave_sorteada.upper()}')

    return palavra_sorteada.upper()


def boneco_forca(chances_retantes):
    boneco = [
        '''
    ------
    |    |
    |    
    |    
    |    
    |    
==============
''',
        '''
    ------
    |    |
    |    O
    |    
    |    
    |    
==============
''',
        '''
    ------
    |    |
    |    O
    |    |
    |    
    |    
==============
''',
        '''
    ------
    |    |
    |    O
    |   /|
    |    
    |    
==============
''',
        '''
    ------
    |    |
    |    O
    |   /|\\
    |    
    |    
==============
''',
        '''
    ------
    |    |
    |    O
    |   /|\\
    |   / 
    |    
==============
''',
        '''
    ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |    
==============
        ''']

    return boneco[chances_retantes]


# print(23*'-')
# print((4*' '), 'JOGO DA FORCA')
# print(23*'-')
# print('\nObjetivo: Tente adivinhar a palvra gerada.')
# print('Regras: Você só pode digitar uma letra por vez, com o limite de 6 erro.\n')

# loop = True
# palavra = palavras_sorteada()
# palavra_letras = []
# palpites_certo = []

# print('A palavra sorteada é... ')
# for letra in palavra:
#     print('_', end=' ')
#     palavra_letras.append(letra)

# print(palavra)
# print('\n')

# while loop:

#     palpite = input('Digite seu palpite <<< ').upper()

#     palpites_certo.append(palpite)

#     for letras in palavra_letras:
#         if palpite == letras:
#             print(palpite, end=' ')

#         else:
#             print('_', end=' ')
