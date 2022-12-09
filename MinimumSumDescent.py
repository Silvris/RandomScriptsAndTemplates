

triangle = [
    [2],
    [5,4],
    [1,4,7],
    [8,6,9,6]
]
t2 = [
    [2],
    [3,9],
    [1,6,7]
]

def descent(A, i, j):
    if i == len(A):
        return 0
    d1 = descent(A, i+1, j)
    d2 = descent(A, i+1, j+1)
    minVal = min(d1,d2)
    dp = A[i][j] + minVal
    return dp

def minSumDescent(triangle):
    n = len(triangle)

    dp = list()
    for i in range(n):
        dp.append(list())
        for j in range(n):
            dp[i].append(-1)
    retval =  descent(triangle,0,0)
    print(retval)
    return retval

print(minSumDescent(triangle))