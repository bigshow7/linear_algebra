#numpy를 이용한 행렬 표현 및 행렬 기초 학습

import numpy as np

#행렬 표현
matrix_A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("행렬 A를 numpy로 표현하면:")
print(matrix_A)
print(f"행렬 A의 타입: {type(matrix_A)}")

#행렬의 원소에 출력해보기
print(matrix_A[0][1])
print(matrix_A[1][2])

#행렬의 크기 및 차원
print(f"행렬 A의 형태: {matrix_A.shape}")   #행렬 A의 행의 개수, 열의 개수
print(f"행렬 A의 차원: {matrix_A.ndim}")    #행렬 A의 차원(2D)
print(f"행렬 A의 원소 개수: {matrix_A.size}")

#기초 행렬 계산
matrix_B = np.array([
    [1,3,5],
    [2,4,6]
])

print(f"행렬의 합: A+B = {matrix_A + matrix_B}")
print(f"스칼라 곱: 2 * A = {2 * matrix_A}")

matrix_C = np.array([
    [1, 3],
    [2, 6],
    [3, 9]
])

print(f"행렬 곱: A * C = {matrix_A @ matrix_C}")

matrix_C = np.array([
    [1, 2],
    [3, 4]
])
print(f"행렬의 제곱(정방행렬만 가능): C^3 = {np.linalg.matrix_power(matrix_C, 3)}")

#전치 행렬
print(f"A의 전치 행렬: {matrix_A.T}")