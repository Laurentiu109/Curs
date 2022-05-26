# 1. Matrice de 5 x 5. Sa se afiseze diagonala principala si diagonala secundara

matrix=[[1,2,3,11,12],
        [4,5,6,13,14],
        [7,8,9,15,16],
        [1,2,3,4,5],
        [6,7,8,9,10]
    ]


for i in range(len(matrix)):
    print(matrix[i])
print("Diagonala principala\n")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j:
            print(matrix[i][j])
print("Diagonala secundara\n")
for i in range(len(matrix)):
    print(matrix[i][len(matrix)-1-i])
