class No:
    def __init__(self, nome):
        self.nome = nome
        self.esquerda = None
        self.direita = None
        self.pai = None


class Diretorio:
    def __init__(self):
        self.raiz = No("C:")

    def buscar_pasta(self, nome_pasta, no=None):
        if no is None:
            no = self.raiz

        if no.nome == nome_pasta:
            return no

        if no.esquerda:
            pasta_esquerda = self.buscar_pasta(nome_pasta, no.esquerda)
            if pasta_esquerda:
                return pasta_esquerda

        if no.direita:
            pasta_direita = self.buscar_pasta(nome_pasta, no.direita)
            if pasta_direita:
                return pasta_direita

        return None

    def criar_pasta(self, nome_pasta, pasta_pai=None):
        if pasta_pai is None:
            pasta_pai = self.raiz

        nova_pasta = No(nome_pasta)
        nova_pasta.pai = pasta_pai

        if not pasta_pai.esquerda:
            pasta_pai.esquerda = nova_pasta
        elif not pasta_pai.direita:
            pasta_pai.direita = nova_pasta
        else:
            print("Erro: pasta pai já tem duas subpastas")
            return

        print(f"Pasta '{nome_pasta}' criada com sucesso")

    def deletar_pasta(self, nome_pasta):
        pasta_a_deletar = self.buscar_pasta(nome_pasta)

        if not pasta_a_deletar:
            print("Pasta não encontrada")
            return

        if pasta_a_deletar == self.raiz:
            print("Erro: não é possível deletar a pasta raiz")
            return

        pasta_pai = pasta_a_deletar.pai

        if pasta_a_deletar.esquerda:
            pasta_substituta = pasta_a_deletar.esquerda
        elif pasta_a_deletar.direita:
            pasta_substituta = pasta_a_deletar.direita
        else:
            pasta_substituta = None

        if pasta_substituta:
            pasta_substituta.pai = pasta_pai
            if pasta_pai.esquerda == pasta_a_deletar:
                pasta_pai.esquerda = pasta_substituta
            else:
                pasta_pai.direita = pasta_substituta
        else:
            if pasta_pai.esquerda == pasta_a_deletar:
                pasta_pai.esquerda = None
            else:
                pasta_pai.direita = None

        print(f"Pasta '{nome_pasta}' deletada com sucesso")

    def listar_pasta(self, nome_pasta, caminho="C:"):
        pasta = self.buscar_pasta(nome_pasta)

        if not pasta:
            print("Pasta não encontrada")
            return

        print(f"Pasta '{caminho}\\{nome_pasta}':")
        self._listar_pasta(pasta, caminho)

    def _listar_pasta(self, no, caminho):
        if no is None:
            return

        if no.esquerda is None and no.direita is None:
            print(f"{caminho}\\{no.nome}")

        if no.esquerda:
            print(f"{caminho}\\{no.nome}")
            self._listar_pasta(no.esquerda, f"{caminho}\\{no.nome}")
        if no.direita:
            print(f"{caminho}\\{no.nome}")
            self._listar_pasta(no.direita, f"{caminho}\\{no.nome}")



diretorio = Diretorio()

# Mostra as pastas filhas da raiz
raiz = diretorio.buscar_pasta("C:")
if raiz.esquerda is None and raiz.direita is None:
    print("A raiz não possui pastas filhas")
else:
    print("Pastas filhas da raiz:")
if raiz.esquerda:
    print(raiz.esquerda.nome)
if raiz.direita:
    print(raiz.direita.nome)

# Menu de opções
while True:
    print("\n---- Menu ----")
    print("1. Listar todas as pastas")
    print("2. Listar pastas de um diretório específico")
    print("3. Criar nova pasta")
    print("4. Deletar pasta")
    print("5. Buscar pasta")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        diretorio.listar_pasta("C:")
    elif opcao == "2":
        nome_pasta = input("Digite o nome da pasta: ")
        diretorio.listar_pasta(nome_pasta)
    elif opcao == "3":
        nome_pasta = input("Digite o nome da nova pasta: ")
        pasta_pai = input("Digite o nome da pasta pai (ou deixe em branco para criar na raiz): ")
        if pasta_pai:
            pasta_pai = diretorio.buscar_pasta(pasta_pai)
        diretorio.criar_pasta(nome_pasta, pasta_pai)
    elif opcao == "4":
        nome_pasta = input("Digite o nome da pasta a ser deletada: ")
        diretorio.deletar_pasta(nome_pasta)
    elif opcao == "5":
        nome_pasta = input("Digite o nome da pasta: ")
        pasta = diretorio.buscar_pasta(nome_pasta)
        if pasta:
            print(f"Pasta encontrada: {pasta.nome}")
        else:
            print("Pasta não encontrada")
    else:
        print("Opção inválida")
