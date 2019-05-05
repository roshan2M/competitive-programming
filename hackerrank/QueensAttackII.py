#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    moves = 0
    for k in (-1, 0, 1):
        for l in (-1, 0, 1):
            if k == 0 and l == 0:
                continue
            i, j = r_q, c_q
            while True:
                # Update position
                i += k
                j += l
                
                # Check if queen can move to position
                if ([i, j] in obstacles) or (i < 1 or i > n or j < 1 or j > n):
                    break
                moves += 1
    return moves
    
if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
