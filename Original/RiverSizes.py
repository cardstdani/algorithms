#Solution to AlgoExpert problem https://www.algoexpert.io/questions/river-sizes
def helper(matrix, i, j):
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]==0:
        return 0
    matrix[i][j]=0
    return helper(matrix, i+1, j)+helper(matrix, i-1, j)+helper(matrix, i, j+1)+helper(matrix, i, j-1)+1
    

def riverSizes(matrix):
    out = []
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            if matrix[a][b] == 1:
                out.append(helper(matrix, a, b))
    return out
