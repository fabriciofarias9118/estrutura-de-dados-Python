
# Escreva um programa que solicite ao usuário uma
# sequência de caracteres sem limite máximo de tamanho
# e realize as seguintes operações usando uma pilha
# a)      Imprimir o texto na ordem inversa;
#
# b)      Verificar se o texto é um palíndromo,
# ou seja, se a string é escrita da mesma maneira de
# frente para trás e de trás para frente. Ignore espaços
# e pontos.

def inverso(texto):
    p = []
    for letra in texto:
        p.append(letra)
    textoInverso = ""
    while p:
        textoInverso += p.pop()
    print("Texto na ordem inversa:", textoInverso)
    return textoInverso

def palindromo(pal):
    pali = pal.replace(" ", "").replace(".", "")
    pali = True
    for i in range(len(texto) // 2):
        if texto[i] != texto[-(i + 1)]:
            pali = False
            break

    if pali:
        print("O texto é um palíndromo!")
    else:
        print("O texto não é um palíndromo.")

texto = input("Digite um texto: ")

inverso(texto)
palindromo(texto)