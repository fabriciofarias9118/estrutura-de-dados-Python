#leia e adicione em uma lista, nomes de forma
# dinamica e exibi-los junto aos indices correspondentes

nomes = []
while True:
    print("insira um nome ou digite 0 para encerra")
    nome = input(":")
    if nome == "0":
        break
    nomes.append(nome)

for i in range(len(nomes)):
    print(f"Nome: {nomes[i]} -- indice : {i}")


