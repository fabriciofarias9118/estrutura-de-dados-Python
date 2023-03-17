
# Faça um algoritmo em Python que solicite ao usuário
# números e os armazene em uma pilha de 30 posições.
# Crie uma função que receba a pilha preenchida e
# substitua todas as ocorrência de valores positivos
# por 1 e todos os valores negativos por 0.

tam = 30
p = [None] * tam
def sub(p):
    for i in range(tam):
        if p[i] > 0:
            p[i] = 1
        elif p[i] < 0:
            p[i] = 0
    return p


for i in range(0,tam):
    num = int(input(f"digite o numero {i+1}: "))
    p[i] = num

print("pilha 1: ",p)
print("pilha 2: ",sub(p))

# tam = 5
# p = [None] * tam
#
#
# def trocar(p):
#     for i in range(tam):
#         if p[i] > 0:
#             p[i] = 1
#         elif p[i] < 0:
#             p[i] = 0
#     return p
#
#
# for i in range(tam):
#     num = int(input(f"Digite o número {i+1}: "))
#     p[i] = num
# print("Pilha original:", p)
# print("Pilha atualizada:", trocar(p))

