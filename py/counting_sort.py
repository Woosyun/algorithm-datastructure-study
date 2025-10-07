# A: unsorted array
# B: sorted array
# k: 0 <= A[i], B[i] <= k
def counting_sort(A, B, k):
    C = [0 for _ in range(k+1)]

    # count each number
    for a in A:
        C[a] += 1
    
    # accumulate C
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]

    # sort to B
    for a in A:
        B[C[a]-1] = a
        C[a] -= 1

li = [0, 10, 3, 2, 1]
result = [0 for _ in range(len(li))]
counting_sort(li, result, 10)

print(result)
