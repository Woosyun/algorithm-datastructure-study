from math import floor
def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        # insert A[i] to B[n*A[i](floor)]
        B[floor(n*A[i])].append(A[i])

    # sort
    for i in range(n):
        B[i].sort()

    return [x for bucket in B for x in bucket]

li = [0.1, 0.5, 0.3, 0.9, 0.7]
result = bucket_sort(li)
print(result)
