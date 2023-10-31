import random


def escolher_palavra():
    palavras = ['python', 'javascript', 'java', 'html',
                'css', 'php']  # Lista de palavras para o jogo
    return random.choice(palavras).upper()


def exibir_forca(vidas_restantes):
    forca = [
        '''
           ------
           |    |
           |    
           |    
           |    
           |    
        ============
        ''',
        '''
           ------
           |    |
           |    O
           |    
           |    
           |    
        ============
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           |    
        ============
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           |    
        ============
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
        ============
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |    
        ============
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |    
        ============
        '''
    ]
    return forca[vidas_restantes]


def jogar():
    palavra = escolher_palavra()
    palavra_escondida = '_' * len(palavra)
    vidas = 6
    letras_erradas = []
    letras_corretas = []
    fim_jogo = False

    while not fim_jogo:
        print(exibir_forca(vidas))
        print(palavra_escondida)
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Letras corretas: {', '.join(letras_corretas)}")

        palpite = input("Digite uma letra ou adivinhe a palavra: ").upper()

        if len(palpite) == 1 and palpite.isalpha():

            if palpite in letras_corretas or palpite in letras_erradas:
                print("Você já tentou essa letra. Tente outra.")

            elif palpite in palavra:
                indices = [i for i, letra in enumerate(
                    palavra) if letra == palpite]
                for index in indices:
                    palavra_escondida = palavra_escondida[:index] + \
                        palpite + palavra_escondida[index + 1:]
                letras_corretas.append(palpite)
                if '_' not in palavra_escondida:
                    fim_jogo = True

            else:
                letras_erradas.append(palpite)
                vidas -= 1
                if vidas == 0:
                    fim_jogo = True
        elif len(palpite) == len(palavra) and palpite.isalpha():

            if palpite == palavra:
                palavra_escondida = palavra
                fim_jogo = True
            else:
                vidas = 0
                fim_jogo = True
        else:
            print(
                "Entrada inválida. Por favor, digite apenas uma letra ou tente adivinhar a palavra.")

    if vidas == 0:
        print(exibir_forca(vidas))
        print(f"Você perdeu! A palavra era {palavra}.")
    else:
        print(f"Parabéns! Você adivinhou a palavra: {palavra}.")


if __name__ == "__main__":
    jogar()
