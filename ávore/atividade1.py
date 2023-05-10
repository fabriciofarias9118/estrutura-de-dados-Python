class NodoArvore:
    def __init__(self,chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                               self.chave,
                               self.direita and self.direita.chave)

    # raiz = NodoArvore(3)
    # raiz.esquerda = NodoArvore(5)
    # raiz.direita = NodoArvore(1)
    # print("Árvore: ", raiz)




# def em_ordem(raiz): #declarando a função com com o paranmetro 'raiz'
#     if not raiz:    #Verifica se a 'raiz' é vazil
#         return
#
#     em_ordem(raiz.esquerda) #Função recursiva para imprimir o filho esquerdo da raiz
#
#     print(raiz.chave)       #imprime o nó chave
#
#     em_ordem(raiz.direita)  #Função recursiva para imprimir o filho esquerdo da raiz




raiz = NodoArvore(40)   #criando a raiz da arvore com valor 40
raiz.esquerda = NodoArvore(20)  #criando o filho esquerdo da raiz com o valor 20
raiz.direita = NodoArvore(60)   #crinado o filho direito da raiz com o valor 60

raiz.direita.esquerda = NodoArvore(50) #criando a folha esquerda do filho direito com 50
raiz.direita.direita = NodoArvore(70)   #criando a folha direita do filho direito com 70
raiz.esquerda.esquerda = NodoArvore(10) #criando a folha esquerda do filho esquerdo com 10
raiz.esquerda.direita = NodoArvore(30)  #criando a folha diretia do filho esquerdo com 30
print(raiz) #imprimi o filho esquerdo a raiz e o filho direito