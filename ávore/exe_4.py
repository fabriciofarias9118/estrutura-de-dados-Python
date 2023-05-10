
#Escreva uma função que calcula a altura de uma árvore binária.

class NodoArvore:
    def __init__(self,chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

def Altura(raiz):
    if raiz is None:
        return -1
    altura_esquerda = Altura(raiz.esquerda)
    altura_direita = Altura(raiz.direita)
    return 1 + max(altura_esquerda, altura_direita)

raiz = NodoArvore(1)
raiz.esquerda = NodoArvore(2)
raiz.direita = NodoArvore(3)
raiz.esquerda.esquerda = NodoArvore(4)
raiz.esquerda.direita = NodoArvore(5)

print(Altura(raiz)) # saída: 2
