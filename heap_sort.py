class HeapBuilder:
    def __init__(self, unsorted_li):
        self.A = unsorted_li
        self.heap_size = len(unsorted_li)

    def left(self, i):
        return 2*i
    def right(self, i):
        return 2*i+1

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l <= self.heap_size and self.A[l-1] > self.A[i-1]:
            largest = l
        else:
            largest = i

        if r <= self.heap_size and self.A[r-1] > self.A[largest-1]:
            largest = r

        # assume left and right subtrees satisfy the max_heap property
        if largest != i:
            self.A[i-1], self.A[largest-1] = self.A[largest-1], self.A[i-1]
            self.max_heapify(largest)
    
    def pop(self):
        self.A[0], self.A[self.heap_size-1] = self.A[self.heap_size-1], self.A[0]
        self.heap_size -= 1
        self.max_heapify(1)
        return self.A[self.heap_size]

    def max_heap_sort(self):
        for i in range(self.heap_size//2, 0, -1):
            self.max_heapify(i)

        for _ in range(self.heap_size):
            self.pop()
        self.A.reverse()
        return self.A

unsorted_arr = [0, 3, 1, 20, 18, 21, -1]
hb = HeapBuilder(unsorted_arr)
sorted_arr = hb.max_heap_sort()
print("sorted_arr is ", sorted_arr)
