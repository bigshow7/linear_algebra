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
ans = np.array(inv_A @ b)
x = ans[0]
y = ans[1]
print(f"답: x = {x:.2f}, y = {y:.2f}")