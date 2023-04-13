# ⦁    No seu sistema operacional ao abrir o “gerenciador  de
# tarefas” você pode exibir os processos que estão em execução, veja como isso é apresentado
# no Windows: Você já parou pra pensar como é possível executar todos esses aplicativos em
# apenas um processador? Isso existe graças a uma funcionalidade chamada de tempo
# compartilhado(“time - shared”).Essa funcionalidade mantém uma sequência de processos em uma
# fila, esperando para serem executados.Implemente uma fila para armazenar as informações desses
# processos. Seu programa deverá permitir: 
# ncluir novos processos na fila de processo;
# Matar o processo com o maior tempo de espera;
# Executar um processo(remover da fila)
# Imprimir o conteúdo da lista de processos.

class Processo:
    def __init__(self, nome, tempo_espera):
        self.nome = nome
        self.tempo_espera = tempo_espera

class FilaProcessos:
    def __init__(self):
        self.fila = []

    def adicionar_processo(self, processo):
        self.fila.append(processo)

    def matar_Processo(self):
        if len(self.fila) > 0:
            maior_tempo = self.fila[0].tempo_espera
            indice_maior_tempo = 0
            for i in range(len(self.fila)):
                if self.fila[i].tempo_espera > maior_tempo:
                    maior_tempo = self.fila[i].tempo_espera
                    indice_maior_tempo = i
            del self.fila[indice_maior_tempo]

    def executar_processo(self):
        if len(self.fila) > 0:
            processo_executado = self.fila[0]
            del self.fila[0]
            return processo_executado
        else:
            return None

    def imprimir_fila(self):
        print("Lista de processos:")
        for processo in self.fila:
            print(f"Nome: {processo.nome}, Tempo de espera: {processo.tempo_espera}")

# Exemplo de uso
fila = FilaProcessos()

while True:
    print("\n--- Menu ---")
    print("1 - Adicionar processo")
    print("2 - Matar processo com maior tempo de espera")
    print("3 - Executar processo")
    print("4 - Imprimir lista de processos")
    print("5 - Sair")

    opcao = int(input("Digite a opção desejada: "))
    print("\n")

    if opcao == 1:
        print(" - Adicionar Processo - ")
        nome = input("Digite o nome do processo: ")
        tempo_espera = int(input("Digite o tempo de espera do processo: "))
        processo = Processo(nome, tempo_espera)
        fila.adicionar_processo(processo)
        print(f"Processo {processo.nome} adicionado à fila.")
    elif opcao == 2:
        fila.matar_Processo()
        print("Processo com maior tempo de espera morto.")
    elif opcao == 3:
        processo_executado = fila.executar_processo()
        if processo_executado is not None:
            print(f"Processo {processo_executado.nome} executado.")
        else:
            print("Não há processos na fila.")
    elif opcao == 4:
        fila.imprimir_fila()
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Digite novamente.")
