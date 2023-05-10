def gauss_jordan():
    n = int(input("Digite o número de equações: "))

    # pede para o usuário inserir a matriz
    A = []
    B = []
    for i in range(n):
        row = input(f"Digite os elementos da linha {i+1} da matriz A, separando por espaço: ").split()
        A.append([float(elem) for elem in row])
        b = float(input(f"Digite o valor da equação {i+1}: "))
        B.append([b])

    # cria a matriz aumentada
    AB = []
    for i in range(n):
        AB.append(A[i] + B[i])

    # pivoteamento parcial
    for i in range(n):
        pivo = AB[i][i]
        if pivo == 0:
            print("Erro: pivô igual a zero")
            return None
        for j in range(i, n+1):
            AB[i][j] = AB[i][j] / pivo
        for k in range(n):
            if k == i:
                continue
            m = AB[k][i]
            for j in range(i, n+1):
                AB[k][j] = AB[k][j] - m * AB[i][j]

    # imprime a solução
    print("Solução:")
    for i in range(n):
        print(f"x{i+1} = {AB[i][-1]}")
