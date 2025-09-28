# sort by each digit
# if a is integer with n digits, a = a1a2a3...an
# for an to a1: stable sort

# A = array of numbers, N1...Nn
# d = number of digit for each number N
def radix_sort(A, d):
    for i in range(d):
        stable_sort(A, i)

