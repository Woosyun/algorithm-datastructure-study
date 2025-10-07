def bottom_up(matrices, i, j, memo):
    if memo[i][j] != None:
        return memo[i][j]

    if i == j:
        return 0

    for k in range(i, j):
        result1 = bottom_up(matrices, i, k, memo)
        result2 = bottom_up(matrices, k+1, j, memo)
        mul = matrices[i][0]*matrices[k][1]*matrices[j][1]
        temp = result1 + result2 + mul

        if memo[i][j] == None:
            memo[i][j] = temp
        else:
            memo[i][j] = min(memo[i][j], temp)
    
    return memo[i][j]

def find_minimum_matrix_multiplications(matrices):
    n = len(matrices)
    memo = [[None for _ in range(n)] for _ in range(n)]
    bottom_up(matrices, 0, n-1, memo)

    return memo[0][n-1]

#matrices = [[5, 3], [3, 2], [2, 6]]
#result = find_minimum_matrix_multiplications(matrices)
#print(result)

n = int(input())
matrices = []
for _ in range(n):
    a, b = map(int, input().split())
    matrices.append((a,b))

result = find_minimum_matrix_multiplications(matrices)
print(result)
