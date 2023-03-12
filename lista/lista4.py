idade = [[0,2,0],
         [0,2,0]]
y = []

for i in range(2):
    for j in range(3):
        print(f"{idade[i][j]}", end=" ")
        y.append(idade[i][j]*2)
    print("")

print(y)
for x in range(2):
    for z in range(3):
        print(f"{y[x][z]}", end="")
    print("")