# – Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

L = [5, 7, 2, 9, 4, 1, 3]
print("Lista L: ",L)
print("tamanho lista L: ",len(L))
print("maior valorda lista L: ",max(L))
print("menor valor da lista L: ",min(L))
print("soma de todos os elementos de L: ",sum(L))
L.sort()
print("L em ordem crescente: ",L)
L.sort(reverse=True)
print("L inverttido:         ", L)


