
#Escreva uma função que conta o número de nós de uma árvore binária.
class NodoArvore:
    def __init__(self,chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)


def contar(raiz):
    if raiz is None:
        return 0
    return 1 + contar(raiz.esquerda) + contar(raiz.direita)

raiz = NodoArvore(1)
raiz.esquerda = NodoArvore(2)
raiz.direita = NodoArvore(3)
raiz.esquerda.esquerda = NodoArvore(4)
raiz.esquerda.direita = NodoArvore(5)

print(contar(raiz)) # saída: 5
