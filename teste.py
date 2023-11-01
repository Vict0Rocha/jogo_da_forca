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


def boneco_forca(chances_retantes):  # Função com uma lista com o desenho do boneco
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


print(23*'-')
print((4*' '), 'JOGO DA FORCA')
print(23*'-')
print('\nObjetivo: Tente adivinhar a palvra gerada.')
print('Regras: Você só pode digitar uma letra por vez, com o limite de 6 erros.\n')

loop = True
palavra = palavras_sorteada()
# palavra_letras = []
palpites_certo = []
conjunto_palavra = [palavra]

print('A palavra sorteada é... ')
espacos = '_ ' * len(palavra)
print(espacos)

print(palavra)
print('\n')

while conjunto_palavra == palpites_certo:

    palpite = input('Digite seu palpite <<< ').upper()

    if palpite in conjunto_palavra:
        palpites_certo.append(palpite)
        for letras in palavra:
            if palpite == letras:
                print(palpite, end=' ')
            else:
                print('_', end=' ')
