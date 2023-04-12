# Escreva um programa que simule o controle de uma pista de decolagem de aviões em um aeroporto. Neste programa, o usuário deve ser capaz de realizar as seguintes tarefas:
# a) Listar o número de aviões aguardando na fila de decolagem;
# b) Autorizar a decolagem do primeiro avião da fila;
# c) Adicionar um avião à fila de espera;
# d) Listar todos os aviões na fila de espera;
# e) Listar as características do primeiro avião da fila.
# Considere que os aviões possuem um nome e um número inteiro como identificador. Adicione outras características conforme achar necessário.

class Aviao:
    def __init__(self, nome, id, modelo):
        self.nome = nome
        self.id = id
        self.modelo = modelo

class PistaDecolagem:
    def __init__(self):
        self.fila_decolagem = []
        # self.max_avioes = 10

    def adicionar_aviao(self):
            nome = input("Digite o nome do avião: ")
            id = int(input("Digite o ID do avião: "))
            modelo = input("Digite o modelo do avião: ")
            aviao = Aviao(nome, id, modelo)
            self.fila_decolagem.append(aviao)
            print("Avião adicionado com sucesso.")

    def listar_fila_decolagem(self):
        print(f"Número de aviões aguardando na fila de decolagem: {len(self.fila_decolagem)}")

    def autorizar_decolagem(self):
        if len(self.fila_decolagem) > 0:
            aviao = self.fila_decolagem.pop(0)
            print(f"O avião {aviao.nome} com ID {aviao.id} e modelo {aviao.modelo} decolou.")
        else:
            print("Não há aviões aguardando na fila de decolagem.")

    def listar_todos_avioes(self):
        for aviao in self.fila_decolagem:
            print(f"Nome: {aviao.nome}, ID: {aviao.id}, Modelo: {aviao.modelo}")

    def listar_caracteristicas_primeiro_aviao(self):
        if len(self.fila_decolagem) > 0:
            aviao = self.fila_decolagem[0]
            print(f"Nome: {aviao.nome}, ID: {aviao.id}, Modelo: {aviao.modelo}")
        else:
            print("Não há aviões aguardando na fila de decolagem.")

pista = PistaDecolagem()

while True:
    print("\n---- Menu ----")
    print("1 - Listar número de aviões na fila de decolagem")
    print("2 - Autorizar decolagem do primeiro avião da fila")
    print("3 - Adicionar avião à fila de espera")
    print("4 - Listar todos os aviões na fila de espera")
    print("5 - Listar as características do primeiro avião da fila")
    print("0 - Encerrar programa")

    opcao = int(input("Digite a opção desejada: "))
    print("\n")

    if opcao == 0:
        break
    elif opcao == 1:
        pista.listar_fila_decolagem()
    elif opcao == 2:
        pista.autorizar_decolagem()
    elif opcao == 3:
        pista.adicionar_aviao()
    elif opcao == 4:
        pista.listar_todos_avioes()
    elif opcao == 5:
        pista.listar_caracteristicas_primeiro_aviao()
    else:
        print("Opção inválida. Tente novamente.")
