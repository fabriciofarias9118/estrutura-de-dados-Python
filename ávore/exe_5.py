

#Escreva uma função para buscar um número impar em uma árvore binária não ordenada

class NodoArvore:
    def __init__(self,chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


def busca_impar(raiz):
    if not raiz:
        return None

    if raiz.valor % 2 != 0:
        return raiz.valor

    valor_esquerda = busca_impar(raiz.esquerda)
    if valor_esquerda:
        return valor_esquerda

    valor_direita = busca_impar(raiz.direita)
    if valor_direita:
        return valor_direita

    return None


def num_impar(raiz):
    if raiz is None:
        return None
    if raiz.chave % 2 == 1:
        return raiz.chave
    num_esquerdo = num_impar(raiz.esquerda)
    num_direito = num_impar(raiz.direita)
    if num_esquerdo is not None:
        return num_esquerdo

    return num_direito

raiz = NodoArvore(4)
raiz.esquerda = NodoArvore(2)
raiz.direita = NodoArvore(7)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(8)
raiz.direita.direita = NodoArvore(9)

print(num_impar(raiz)) # saída: 7
