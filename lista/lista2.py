#OPERAÇÕES COM LISTAS
# len(L)         retorna o tamanho da lista.
# max(L)         retorna o maior valor da lista
# sum(L)         retorna soma dos elementos da lista.
# .append() =    adiciona um novo valor na no final da lista.
# in L           verifica se um valor pertence à lista. L
# del L[i]       Deleta o valor no indice da lista
# L.sort()                Ordena em ordem crescente
# L.extend([1,2,3])       Adiciona uma lista ao final da lista
# L.Sort(reverse==TRUE)   Inverte os elementos de uma lista
# L.insert(1,2)           Troca o elemento da inidicado no primeiro parametropelo segundo parametro
# L.pop()                 Remove o ultimo indice da lista ou do indice informado no parametro
# L.remove()              Remove o valor no parametro

#CONCATENAÇÃO +
print("concatena")
a = [0,1,2]
b = [3,4,5]
print("lista a: ",a)
print("lista b: ",b)
c = a + b
print("Lista a e b concatenada: ", c)

#REPETIÇÃO *
print("reptição 4 vezes 1,2")
L = [1,2]
print("Lista L: ",L)
R = L * 4
print("lista L repetida 4 vezes", R)

#FATIAMENTO DE LISTA
print("fatiamento 1:4")
L = [3 , 'abacate' , 9.7 , [5 , 6 , 3] , "Python" , (3 , 'j')]
print(L[1:4])
#del para deletar
print("del 0")
del L[0]
print(L)

#pop para remover o ultimo indice
L.pop()
print("pop")
print(L)

# remove para deletar um determinado valor
print("remove")
L.remove(9.7)
print(L)