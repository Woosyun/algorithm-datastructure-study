def direct_address_search(T, k):
    return T[k]
def direct_address_insert(T, key, val):
    T[key] = val
def direct_address_delete(T, key):
    T[key] = []

# Chained hash
# - if single linked, to delete element
#   we would find x in the list (T[h(x.key)])
#   but for doubly linked, O(1) time is enough? How?


