import random
import os


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


def painel():
    print(23*'-')
    print((4*' '), 'JOGO DA FORCA')
    print(23*'-')
    print('\nObjetivo: Tente adivinhar a palvra gerada.')
    print('Regras: Você só pode digitar uma letra por vez, com o limite de 6 erros.\n')


chances = 0
ganhou = False
letras_digitadas = []
painel()
print(boneco_forca(chances))
palavra = palavras_sorteada()

while True:

    for letra in palavra:
        if letra.upper() in letras_digitadas:
            print(letra, end=" ")
        else:
            print('_', end=" ")

    print(f'\n\nVocê tem {6 - chances} chances restantes\n')

    palpite = input('Digite o seu palpite: ').upper()
    letras_digitadas.append(palpite)

    if palpite not in palavra:
        chances += 1
        os.system('cls')
        print(boneco_forca(chances))

    ganhou = True

    for letra in palavra:
        if letra.upper() not in letras_digitadas:
            ganhou = False

    if chances == 6:
        os.system('cls')
        print(boneco_forca(chances))
        print('GAME OVER - Você PERDEU')
        print(f'A palavra era: {palavra}\n')
        print('Você deseja jogar de novo? ')
        game = input('[S] - sim [N] - não\n').upper()

        match game:
            case 'S':
                os.system('cls')
                chances = 0
                ganhou = False
                letras_digitadas = []
                painel()
                print(boneco_forca(chances))
                palavra = palavras_sorteada()
                continue
            case 'N':
                print('FIM DE JOGO')
                break
            case Exception:
                print('Opção inválida. FIM DE JOGO')
                break

    if ganhou:
        os.system('cls')
        print(boneco_forca(chances))
        print('PARABÉNS VOCÊ GANHOU!')
        print(f'A palavra era: {palavra}\n')
        print('Você deseja jogar de novo? ')
        game = input('[S] - sim [N] - não\n').upper()

        match game:
            case 'S':
                os.system('cls')
                chances = 0
                ganhou = False
                letras_digitadas = []
                painel()
                print(boneco_forca(chances))
                palavra = palavras_sorteada()
                continue
            case 'N':
                print('FIM DE JOGO')
                break
            case Exception:
                print('Opção inválida. FIM DE JOGO')
                break
