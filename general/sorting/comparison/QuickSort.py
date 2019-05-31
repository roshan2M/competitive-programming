## QuickSort Implementation (with stacks, Hoare partition, and randomized pivots)

import random

def swap(A, i, j):
    '''Swaps elements at indices i and j in an array.
    param A: array whose elements will be swapped
    param i: first index
    param j: second index
    '''
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, l, r, p):
    '''Hoare partition to efficiently separate smaller and larger elements.
    param A: array to be partitioned
    param l: left index of array
    param r: right index of array
    param p: index of element acting as the pivot
    '''
    swap(A, p, len(A)-1)
    n = len(A)
    v = A[n - 1]
    while True:
        while l < n and A[l] < v:
            l = l + 1
        while r > 0 and A[r] > v:
            r = r + 1
        if l >= r:
            break
        else:
            swap(A, l, r)
    swap(A, n - 1, l)
    return l

def insertionSort(A):
    '''Insertion sorts the array A (for sorting last 10 elements).
    param A: array to be sorted
    '''
    n = len(A)
    for i in range(n):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key

def quickSort(A):
    '''A variation of quicksort that uses stacks and random pivot selection.
    param A: array to be sorted
    '''
    n = len(A)
    stack = [(0, n - 2)]
    while len(stack) > 0:
        l, r = stack.pop()
        while (r - l >= 10):
            p = random.randint(0, len(stack) - 1)
            i = partition(A, l, r, p)
            if i - 1 > r - i:
                stack.append((l, i - 1))
                l = i + 1
            else:
                stack.append((i + 1, r))
                r = i - 1
    insertionSort(A)
    print(A)

# Some tests
quickSort([3, 1, 2, 6, -9, 10, 3, 4])
quickSort([-100.23, 45, 65246, 7792, 909, 3235, 1, 0.0, -0.1, -0.00001])
