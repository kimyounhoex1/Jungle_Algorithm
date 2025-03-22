import sys

N, B = map(int, sys.stdin.readline().split())

given_matrix = []
i_matrix = [[0] * N for _ in range(N)]

result_matrix = [[0] * N for _ in range(N)]
for i in range(N):
    given_matrix.append(list(map(int, sys.stdin.readline().split())))
    i_matrix[i][i] = 1



def multiflex_matrix(matrixA, matrixB): #제곱 행렬을 표현함
    size = len(matrixA)
    result_matrix = [[0] * N for _ in range(N)]
    for i in range(0, size, 1):
        for j in range(0, size, 1):
            for k in range(0, size, 1):
                result_matrix[i][j] += matrixA[i][k] * matrixB[k][j]

            result_matrix[i][j] %= 1000
        
    return result_matrix
            
def recursive_matrix(matrixA, B):    
    if B == 1:
        return multiflex_matrix(matrixA, i_matrix)
    else:
        temp_matrix = multiflex_matrix(matrixA, matrixA)
        if B % 2 == 0:
            return recursive_matrix(temp_matrix,B // 2)
        else:
            return multiflex_matrix(recursive_matrix(temp_matrix, B//2), matrixA)
    

# print(i_matrix)

final_matrix = recursive_matrix(given_matrix, B)
for i in range(len(given_matrix)):
    for j in range(len(given_matrix)):
        print(final_matrix[i][j], end =" ")
    print()
# print(multiflex_matrix(given_matrix, given_matrix))
    
    
    