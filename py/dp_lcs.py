# X, Y, lcs Z

def lcs(X, x, Y, y, memo):
    if x==-1 or y==-1:
        return 0

    if memo[x][y] == None:
        if X[x] == Y[y]:
            memo[x][y] = 1 + lcs(X, x-1, Y, y-1, memo)
        else:
            memo[x][y] = lcs(X, x-1, Y, y, memo)
            memo[x][y] = max(memo[x][y], lcs(X, x, Y, y-1, memo))

    return memo[x][y]

def bottom_up(X, Y):
    memo = [[0 for _ in range(len(Y)+1)] for _ in range(len(X)+1)]

    for x in range(1, len(X)+1):
        for y in range(1, len(Y)+1):
            if X[x-1] == Y[y-1]:
                memo[x][y] = memo[x-1][y-1] + 1
            else:
                memo[x][y] = max(memo[x][y-1], memo[x-1][y])

    return memo[len(X)][len(Y)]


X = list(input())
Y = list(input())

result = bottom_up(X, Y)
print(result)

