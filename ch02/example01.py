'''
행렬 기초 문제01
아래에 제시한 1차연립방정식을 역행렬을 통해 구하여라

3x + 1y = 1
1x + 2y = 0
'''
import numpy as np
from inverse_matrix import inv_mat  #역함수 구하는 모듈 import

A = np.array([
    [3,1],
    [1,2]
])

b = np.array([1,0])

inv_A = inv_mat(A)
if inv_A is None:
    raise RuntimeError("역행렬 계산 실패: 행렬식이 0이거나 입력 오류")

ans = inv_A @ b     #A의 역행렬과 상수행렬 b를 곱하면 답이 리스트 형태로 출력됨
x = ans[0]
y = ans[1]
print(f"답: x = {x:.2f}, y = {y:.2f}")

'''
참고)
Ax = b 형태 연립방정식을 푸는 numpy 함수
numpy.linalg.solve(a, b)를 쓰면 좀 더 간단히 구할 수 있음
내부적으로 가우스 소거법 등을 이용해 효율적으로 풀 수 있음
x, y = solve_linear(A, b)
'''