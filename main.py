import random # Para sortear a palavra 
import os # Para limpar o terminar


def palavras_sorteada():  # Função para sortear uma palavra

    # Dicionario contendo todas as palavras
    palavra = {
        'ANIMAL': ['macaco', 'elefante', 'girafa', 'cabra', 'camelo', 'cachorro', 'chinchila', 'crocodilo', 
                   'camundongo', 'cavalo', 'coala', 'coelho', 'capivara', 'zebra', 'hiena', 'hipopotamo', 'vaca'],
        'NOME': ['victor', 'fabio', 'matheus', 'heitor', 'livia', 'luana', 'henrique', 'alice', 
                 'marcia', 'laura', 'antonella', 'beatriz', 'zilda', 'reginaldo'],
        'FRUTA': ['abacaxi', 'uva', 'banana', 'figo', 'damasco', 'framboesa', 'amora', 'goiaba',
                   'manga', 'laranja', 'mamao', 'limao', 'kiwi', 'pera', 'pessego']
    }

    # Sorteando a chave e uma palvra do dict
    chave_sorteada = random.choice(list(palavra.keys()))
    palavra_sorteada = random.choice(palavra[chave_sorteada])
    print(f'Dica: {chave_sorteada.upper()}') 

    return palavra_sorteada.upper() # Retorna a palavra sorteada em maiusculo


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

    # Retorna a possição que quero exibir o meu boneco
    return boneco[chances_retantes]


def painel(): # Somente para informar o usuario
    print(23*'-')
    print((4*' '), 'JOGO DA FORCA')
    print(23*'-')
    print('\nObjetivo: Tente adivinhar a palvra gerada.')
    print('Regras: Você só pode digitar uma letra por vez, com o limite de 6 erros.')
    print('Observação: O jogo não possui nenhum tipo de acentuação.\n')


chances = 0
ganhou = False
letras_digitadas = []
palpites_errados = []
painel()
print(boneco_forca(chances))
palavra = palavras_sorteada()

while True:

    # Percurendo a palavra
    for letra in palavra:
        if letra.upper() in letras_digitadas:
            print(letra, end=" ")
        else:
            print('_', end=" ")

    print(f'\n\nVocê tem {6 - chances} chances restantes.')
    print(f'Palpites errados digitados: {palpites_errados}\n')

    palpite = input('Digite o seu palpite: ').upper()
    letras_digitadas.append(palpite) # Armazendo os palpites em uma lista

    if palpite not in palavra: # Verificando se o jogador acerto uma letra
        chances += 1
        palpites_errados.append(palpite)
        os.system('cls')
        print(boneco_forca(chances))

    ganhou = True

    for letra in palavra:
        # Verificando se o jogador acertou todas as letras
        if letra.upper() not in letras_digitadas:
            ganhou = False

    if chances == 6: # Verificando se o atingiu o limite maximo de erros
        os.system('cls')
        print(boneco_forca(chances))
        print('GAME OVER - Você PERDEU.')
        print(f'A palavra era: {palavra}\n')
        print('Você deseja jogar de novo? ')
        game = input('[S] - sim [N] - não\n').upper()

        match game:
            case 'S':
                os.system('cls')
                chances = 0
                ganhou = False
                letras_digitadas = []
                palpites_errados = []
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
        print('VICTORY - PARABÉNS VOCÊ GANHOU!')
        print(f'A palavra era: {palavra}\n')
        print('Você deseja jogar de novo? ')
        game = input('[S] - sim [N] - não\n').upper()

        match game:
            case 'S':
                os.system('cls')
                chances = 0
                ganhou = False
                letras_digitadas = []
                palpites_errados = []
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
