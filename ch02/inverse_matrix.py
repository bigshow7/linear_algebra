#역행렬 기초 학습
import numpy as np

def inv_mat(matrix):
    det_A = np.linalg.det(matrix)
    print(f"입력된 행렬의 행렬식: {det_A}")

    if det_A == 0:
        print("행렬식이 0이므로 역행렬이 존재하지 않습니다!")

    else:
        print(f"입력된 행렬의 역행렬: {np.linalg.inv(matrix)}")
    

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