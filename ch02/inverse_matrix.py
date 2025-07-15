#역행렬 기초 학습
import numpy as np

def inv_mat(matrix):
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        print("정방행렬만 지원합니다")
        return

    det = np.linalg.det(matrix)
    print(f"입력된 행렬의 행렬식: {det:.4f}")       #소수점 4째까지만

    if np.isclose(det, 0):
        print("행렬식이 0이므로 역행렬이 존재하지 않습니다!")
        return None

    else:
        inverse_mat = np.linalg.inv(matrix)
        print(f"입력된 행렬의 역행렬: {inverse_mat}")
        return inverse_mat  #재사용 시 편리하도록 역행렬 반환
        
    

matrix_A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(f"행렬 A: {matrix_A}")
inv_mat(matrix_A)

matrix_B = np.array([
    [3,6,5],
    [2,5,10],
    [5,2,0]
])

print(f"행렬 B: {matrix_B}")
inv_mat(matrix_B)

matrix_C = np.array([
    [1,2,3],
    [4,5,6]
])
print(f"행렬 C: {matrix_C}")
inv_mat(matrix_C)