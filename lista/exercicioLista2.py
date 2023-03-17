# Gere uma lista de contendo os múltiplos
# de 3 entre 1 e 50

multiplo3 = []

for i in range(1,51):
    if i % 3 == 0:
        multiplo3.append(i)

print(multiplo3)