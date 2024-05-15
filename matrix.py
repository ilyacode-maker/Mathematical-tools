def multip(A,B):
    C = []
    for i in range(len(A)):
        C.append([])
    n = len(A[0])
    for i in range(len(A)):
        for j in range(len(A[i])):
            count = 0
            for h in range(1,n):
                count += A[i][h]*B[h][j]
            C[i].append(count)

    return C

A = [
    [1,2,3],
    [5,6,7],
    [9,3,5]
]
B = [
    [2,3,4],
    [1,1,1],
    [2,3,4]
]

print(multip(A,B))
