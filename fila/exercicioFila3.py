#
# Implemente um programa em Python que registre os nomes
# e as pontuações de times que estão disputando um campeonato,
# fazendo uma fila de prioridade, onde a pontuação mais baixa
# fica com prioridade baixa e a pontuação mais alta com a
# prioridade alta.
import heapq

class Time:
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao

    def __lt__(self, outro):
        return self.pontuacao < outro.pontuacao

    def __str__(self):
        return f"{self.nome} - {self.pontuacao} pontos"


class Campeonato:
    def __init__(self):
        self.times = []
        self.id = 0

    def adicionar_time(self):
        print("Adicionar Time")
        nome = input("Digite o nome do time: ")
        pontuacao = int(input("Digite a pontuação do time: "))
        time = Time(nome, pontuacao)
        heapq.heappush(self.times, (time, self.id))
        self.id += 1
        print(f"Time {nome} adicionado com sucesso!")

    def ver_tabela(self):
        if not self.times:
            print("Não há times registrados!")
        else:
            print("----- TABELA DE CLASSIFICAÇÃO -----")
            for time, _ in sorted(self.times, reverse=True):
                print(time)

    def menu(self):
        while True:
            print("\n=== MENU CAMPEONATO ===")
            print("1. Adicionar time")
            print("2. Ver tabela")
            print("0. Sair")

            opcao = input("Digite a opção desejada: ")
            print("\n")

            if opcao == "1":
                self.adicionar_time()
            elif opcao == "2":
                self.ver_tabela()
            elif opcao == "0":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida, tente novamente!")


campeonato = Campeonato()
campeonato.menu()
