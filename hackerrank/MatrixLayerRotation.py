def matrixRotation(matrix, m, n, r):
    resultMatrix = [row[:] for row in matrix]

    m -= 1
    n -= 1
    for i in range(m+1):
        for j in range(n+1):
            x = min(i, m-i)
            y = min(j, n-j)
            layer = min(x, y)
            maxRows = m - layer
            maxCols = n - layer
            cycleSize = 2*(maxRows + maxCols) - 4*layer

            row = i
            col = j
            for k in range(r % cycleSize):
                if col == layer and row < maxRows:
                    row += 1
                elif row == maxRows and col < maxCols:
                    col += 1
                elif row > layer and col == maxCols:
                    row -= 1
                elif row == layer and col > layer:
                    col -= 1
            resultMatrix[row][col] = matrix[i][j]
    return resultMatrix

if __name__ == '__main__':
    mnr = raw_input().rstrip().split()
    m = int(mnr[0])
    n = int(mnr[1])
    r = int(mnr[2])

    matrix = []

    for _ in xrange(m):
        matrix.append(map(int, raw_input().rstrip().split()))

    result = matrixRotation(matrix, m, n, r)
    for row in result:
        print(' '.join(map(str, row)))
