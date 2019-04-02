#!/bin/python3

import math
import os
import random
import re
import sys

def findSet(x, sets):
    if sets[x] < 0:
        return x
    sets[x] = findSet(sets[x], sets)
    return sets[x]

def unionSet(u, v, sets):
    a = findSet(u, sets)
    b = findSet(v, sets)
    newSize = sets[a] + sets[b]
    if sets[a] > sets[b]:
        sets[a] = b
        sets[b] = newSize
    else:
        sets[b] = a
        sets[a] = newSize

if __name__ == '__main__':
    n, p = map(int, input().split())
    sets = [-1 for _ in range(n)]

    for _ in range(p):
        u, v = map(int, input().split())
        set_u = findSet(u, sets)
        set_v = findSet(v, sets)
        if set_u != set_v:
            unionSet(set_u, set_v, sets)

    l = [0] * n
    for i in range(n):
        if sets[i] < 0:
            l[i] += 1
        else:
            l[findSet(sets[i], sets)] += 1

    summ = 0
    ans = 0
    for i in l:
        ans += i * summ
        summ += i
    print(ans)
