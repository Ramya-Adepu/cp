# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    if(len(m1[0])==len(m2)):
        result = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*m2)]
                                for A_row in m1]
        return result
    return None

# ([[1,3],[2,4],[2,5]], [[1,3,2,2], [2,4,5,1]], [[7, 15, 17, 5], [10, 22, 24, 8], [12, 26, 29, 9]]),
# ([[1],[2,4],[2,5]], [[1,3,2,2], [2,4,5,1]], None),
# ([[1,3,5],[2,4,6],[2,5,7]], [[1,3,2,2], [2,4,5,1]], None),
# ([[1,3],[2,4]], [[1,3,2,2], [2,4,5,1]], [[7, 15, 17, 5], [10, 22, 24, 8]])

print(fun_matrixmultiply([[1],[2,4],[2,5]], [[1,3,2,2], [2,4,5,1]]))

