## HeapSort Implementation

# Utility Functions

def swap(A, i, j):
    '''Swaps elements at indices i and j in an array.
    param A: array whose elements will be swapped
    param i: first index
    param j: second index
    '''
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def isLeaf(n, k):
    '''Returns True if index k is a leaf element in an array of length n.
    param n: length of array
    param k: index of element
    '''
    return 2*k + 1 >= n

def parent(i):
    '''Finds the parent of given index in array representation.
    param i: index to find the parent of
    '''
    return (i-1)//2


# Functions related to HeapSort

def fixDown(A, n, k):
    '''Filters element at index i to the correct position in heap.
    param i: index of position to be filtered down
    '''
    while not isLeaf(n, k):
        j = 2*k + 1
        if j < n-1 and A[j+1] > A[j]:
            j = j + 1
        if A[k] >= A[j]:
            break
        swap(A, j, k)
        k = j

def heapSort(A):
    '''An implementation of heap sort using an array representation of a heap.
    param A: array to be sorted
    '''
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        fixDown(A, n, i)
    while n > 1:
        swap(A, 0, n-1)
        n = n - 1
        fixDown(A, n, 0)
    print(A)

# Some tests
heapSort([3, 1, 2, 6, -9, 10, 3, 4])
heapSort([-100.23, 45, 65246, 7792, 909, 3235, 1, 0.0, -0.1, -0.00001])
