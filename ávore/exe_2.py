
#Escreva uma função que conta o número de nós não-folha de uma árvore binária

class NodoArvore:
    def __init__(self,chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

def naoFolhas(raiz):
    if raiz is None or (raiz.esquerda is None and raiz.direita is None):
        return 0
    return 1 + naoFolhas(raiz.esquerda) + naoFolhas(raiz.direita)

raiz = NodoArvore(1)
raiz.esquerda = NodoArvore(2)
raiz.direita = NodoArvore(3)
raiz.esquerda.esquerda = NodoArvore(4)
raiz.esquerda.direita = NodoArvore(5)

print(naoFolhas(raiz))
