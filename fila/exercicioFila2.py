#  Deque (ou fila de duas pontas) é uma estrutura de dados que consiste de uma lista na qual as seguintes operações são permitidas:
# (a) Empilha(A) Insere o elemento A no início do deque.
# (b) Desempilha () Remove o elemento que está no início do deque.
# (c) Inject(A) Insere o elemento A no final do deque.
# (d) Eject () Remove o elemento que está no final do deque.
# Crie uma estrutura de dados adequada e implemente as operações acima.
class Deque:
    def __init__(self):
        self.items = []

    def empilha(self, item):
        self.items.insert(0, item)

    def desempilha(self):
        if self.esta_vazio():
            return None
        return self.items.pop(0)

    def inject(self, item):
        self.items.append(item)

    def eject(self):
        if self.esta_vazio():
            return None
        return self.items.pop()

    def esta_vazio(self):
        return len(self.items) == 0

    def ver_deque(self):
        if self.esta_vazio():
            print("O deque está vazio.")
        else:
            print("Deque:", self.items)


deque = Deque()

while True:
    print("\nEscolha uma opção:")
    print("1 - Empilhar == iserir no inicio do Deque")
    print("2 - Desempilhar == remover do inicio do Deque")
    print("3 - Inject == inserir no final do Deque")
    print("4 - Eject == remover no final do Deque")
    print("5 - Ver deque")
    print("6 - Sair")

    opcao = int(input("Opção escolhida: "))
    print("\n")

    if opcao == 1:
        item = input("Digite o item a ser empilhado: ")
        deque.empilha(item)
    elif opcao == 2:
        item = deque.desempilha()
        if item is None:
            print("O deque está vazio.")
        else:
            print("Item desempilhado:", item)
    elif opcao == 3:
        item = input("Digite o item a ser injetado: ")
        deque.inject(item)
    elif opcao == 4:
        item = deque.eject()
        if item is None:
            print("O deque está vazio.")
        else:
            print("Item ejetado:", item)
    elif opcao == 5:
        deque.ver_deque()
    elif opcao == 6:
        break
    else:
        print("Opção inválida.")
