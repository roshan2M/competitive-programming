def longestCommonSubsequence(a, b):
    """
    params: a, b are strings
    returns: length of longest common subsequence between a and b
    """
    T = [[0] * (len(a)+1)] * (len(b)+1)
    for i in range(len(b)):
        for j in range(len(a)):
            if (b[i] == a[j]):
                T[i+1][j+1] = T[i][j] + 1
            else:
                T[i+1][j+1] = max(T[i][j+1], T[i+1][j])
    return T[-1][-1]

# Simple Tests
assert(longestCommonSubsequence("abcdaf", "acbcf") == 4)
assert(longestCommonSubsequence("abcdefghi", "acdefghi") == 8)
