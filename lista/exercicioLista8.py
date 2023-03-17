
# Utilizando somente operações de empilhar e desempilhar,
# escreva um programa que remove um item com chave c
# fornecida pelo usuário da pilha. Ao final da execução
# da função, a pilha deve ser igual à original, exceto pela
# ausência do item removido.

# L = ["a", "b", "c", "d"]
#
# while True:
#     letra = input("digite um item para ser removido")
#     for i in range(4):
#         if letra in L:
#             L.pop()
#         break

def remove(pilha, letra):
    pilha2 = []
    while pilha:
        topo = pilha.pop()
        if topo == letra:
            break
        pilha2.append(topo)

    while pilha2:
        pilha.append(pilha2.pop())
    print("Pilha com item removido:", pilha)

p = ["a", "b", "c", "d", "e"]
print(p)
letra = (input("Digite o item a ser removido da pilha: "))
remove(p, letra)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in lista[:]:
#     if i % 2 == 0:
#         lista.remove(i)
# print("Lista modificada:", lista)



# Faça um algoritmo em Python que solicite ao usuário números e os armazene em uma pilha de 30 posições. Crie uma função que receba a pilha preenchida e substitua todas as ocorrência de valores positivos por 1 e todos os valores negativos por 0. (1,0 ponto)
#
# Escreva um programa que solicite ao usuário uma sequência de caracteres sem limite máximo de tamanho e realize as seguintes operações usando uma pilha: (1,0 ponto)
# a)      Imprimir o texto na ordem inversa;
#
# b)      Verificar se o texto é um palíndromo, ou seja, se a string é escrita da mesma maneira de frente para trás e de trás para frente. Ignore espaços e pontos.
#
# Utilizando somente operações de empilhar e desempilhar, escreva um programa que remove um item com chave c fornecida pelo usuário da pilha. Ao final da execução da função, a pilha deve ser igual à original, exceto pela ausência do item removido. (1,0 ponto)
#
# Escreva um programa que remova todos os elementos com chaves pares de uma lista encadeada.