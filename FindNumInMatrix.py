
#create our matrix
from random import randint


matrix = list()

for i in range(10):
    matInd = list()
    for j in range(10):
        matInd.append((i*10)+j)
    matrix.append(matInd)

def FindNumInMatrix(mat, n, num):
    i = 0
    j = n-1
    while i < n and j > -1:
        if mat[i][j] == num:
            print("I:{} J:{}".format(i,j))
            return
        elif mat[i][j] > num:
            j -= 1
        else:
            i += 1
    print("Not present")

randNum = randint(0,99)
print("Finding {}:".format(randNum))
FindNumInMatrix(matrix,10,randNum)