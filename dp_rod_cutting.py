#<input>
#  prices[i]: price for each length i
#  1 <= i <= N
# N: length of rod

def rod_cutting(prices, N):
    # store max values for each length
    memo = [0]*N
    
    for i in range(1, N+1): # i represent length of rod
        for j in range(1, len(prices)+1): # j represents length of the rod given in prices
            if i-j == 0:
                memo[i-1] = prices[j-1]
            elif i-j > 0:
                memo[i-1] = max(memo[i-1], memo[i-j-1] + prices[j-1])

    return memo

result = rod_cutting([1, 2, 5], 6)
print(result)
