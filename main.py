import random
import os

palavras = ['macaco', 'elefante', 'jacare', 'girafa', 'tartaruga', 'calango', 'camelo', 'cachoro' 'uva', 'figo',
            'mamão', 'amora', 'caju', 'laranja', 'cupuaçu', 'morango', 'cereja', 'abacaxi', 'jaca', 'banana', 'pera', 'acerola', 'manga']
# palavras_frutas = ['uva', 'figo', 'mamão', 'amora', 'caju', 'laranja'] #, 'cupuaçu', 'morango', 'cereja', 'abacaxi', 'jaca', 'banana', 'pera', 'acerola', 'manga']
# palavras_nomes = ['victor', 'marcos', 'ana', 'joão']


# Escolhendo uma palavra aleatoria e deixando tudo em maiusculo
palavra_aleatoria = random.choice(palavras).upper()
os.system('cls')  # Limpando a tela antes de começar o jogo

print('\n---------------------------')
print('      JOGO DA FORCA')
print('---------------------------')

print('\nObjetivo: Tente adivinhar a palvra gerada')
print('Regras: Você só pode digitar uma letra por vez, com o limite de 6 erros')

# End é utilizado para não pular a linha quando chegar no for
print('\nA palavra sorteada é: ', end=' ')
for letra in palavra_aleatoria:
    print('_', end=' ')

erro = 0
# Criando um conjunto para a palavra aletoria, isso é para separar cada letra da palavra
conjunto_letras_palavras = set(palavra_aleatoria)
# Criando um conjunto lara o palpite do usuario, para verificar se a letra digitada está dentro do conjunto da palavra
conjunto_letras_digitada = set()

# Repetir enquanto não acertar
while not conjunto_letras_palavras.issubset(conjunto_letras_digitada) and erro <= 6:
    print("\n")
    palpite = input('Digite seu palpite: ').upper()
    conjunto_letras_digitada.add(palpite)
    if palpite in conjunto_letras_palavras:  # Verificando se o palpite foi correto
        print('\nA palavra sorteada é: ', end=' ')
        for letra in palavra_aleatoria:
            if letra in conjunto_letras_digitada:
                print(f'{letra}', end=' ')
            else:
                print('_', end=' ')
    else:
        erro += 1
        print(f'Você errou, {erro} de 6 tentativas. Tente novamente')
print('Letras já digitadas: ', conjunto_letras_digitada)

if erro <= 6:
    print('Parabens, você venceu essa partida!')
else:
    print('Não foi dessa vez, você perdeu essa partida!')
