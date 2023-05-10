
#Escreva uma função que conta o número de folhas de uma árvore binária

class NodoArvore:
    def __init__(self,chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

def contar(raiz):
    if raiz is None:
        return 0
    if raiz.esquerda is None and raiz.direita is None:
        return 1
    return contar(raiz.esquerda) + contar(raiz.direita)

raiz = NodoArvore(1)
raiz.esquerda = NodoArvore(2)
raiz.direita = NodoArvore(3)
raiz.esquerda.esquerda = NodoArvore(4)
raiz.esquerda.direita = NodoArvore(5)

print(contar(raiz)) # saída: 3
