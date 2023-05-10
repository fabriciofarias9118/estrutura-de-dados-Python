
#Escreva uma função para achar o MAIOR número em uma árvore binária não ordenada

class NodoArvore:
    def __init__(self,chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita


def maior_num(raiz):
    if raiz is None:
        return float('-inf')
    max_esquerdo = maior_num(raiz.esquerda)
    max_direito = maior_num(raiz.direita)
    return max(raiz.chave, max_esquerdo, max_direito)

raiz = NodoArvore(4)
raiz.esquerda = NodoArvore(2)
raiz.direita = NodoArvore(7)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(8)
raiz.direita.direita = NodoArvore(9)

print(maior_num(raiz)) # saída: 10
