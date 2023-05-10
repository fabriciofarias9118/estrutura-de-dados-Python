
#Escreva uma função que exclui todos os nós de uma árvore binária NÃO ordenada com ID par

class NodoArvore:
    def __init__(self,chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

def excluir_id_par(raiz):
    if raiz is None:
        return None
    raiz.esquerda = excluir_id_par(raiz.esquerda)
    raiz.direita = excluir_id_par(raiz.direita)
    if raiz.chave % 2 == 0:
        return None
    return raiz

raiz = NodoArvore(4)
raiz.esquerda = NodoArvore(2)
raiz.direita = NodoArvore(7)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(8)
raiz.direita.direita = NodoArvore(9)

nova_raiz = excluir_id_par(raiz)

# percorre a árvore resultante para verificar se os nós foram excluídos
def trav(NodoArvore):
    if NodoArvore is None:
        return
    print(NodoArvore.chave)
    trav(NodoArvore.esquerda)
    trav(NodoArvore.direita)

trav(nova_raiz) # saída: 7 9

