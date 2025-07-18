#선형 독립과 종속 관계를 파이썬 코드를 통해 구현해보는 프로젝트

import numpy as np

'''
벡터의 선형 독립을 확인하는 방법
1) 벡터를 열벡터로 하는 행렬을 만들고 행렬의 열의 개수 = 랭크이면 선형독립
2) 만약 정사각행렬이 된다면 행렬식 = 0이면 선형독립

참고할 함수
np.column_stack((a, b, c...))	    1차원 → 열벡터로 해석 후 열 단위로 붙임(선형독립성 확인에서 쓰일 함수)
np.row_stack((a, b, c...))	    1차원 → 행벡터로 해석 후 행 단위로 붙임
'''

#선형 독립성 확인
def lin_dep(*vec):
    mat = np.column_stack((vec))
    if mat.shape[0] == mat.shape[1]:         #정사각행렬 여부 확인
        det = np.linalg.det(mat)
        print("입력된 벡터들로 만들어진 행렬은 정방행렬입니다\n따라서 행렬식의 값으로 선형독립성 판단이 가능합니다")
        if np.isclose(det, 0):
            print(f"{', '.join(str(v) for v in vec)}는 선형종속입니다.")
        else:
            print(f"{', '.join(str(v) for v in vec)}는 선형독립입니다.")
    else:
        print("입력된 벡터들로 만들어진 행렬은 정방행렬이 아닙니다\n따라서 행렬식의 값이 아닌 랭크값과 열의 개수의 비교를 통해 선형독립성 판단이 가능합니다")
        if mat.shape[1] == np.linalg.matrix_rank(mat):
            print(f"{', '.join(str(v) for v in vec)}는 선형독립입니다.")
        else:
            print(f"{', '.join(str(v) for v in vec)}는 선형종속입니다.")

#2D 선형독립성 확인
v1 = np.array([1,0])
v2 = np.array([0,1])        #표준 기저 벡터

v3 = np.array([1,1])
v4 = np.array([2,2])        # v3 * 2 = v4, 즉 선형 종속 관계

lin_dep(v1,v2)
lin_dep(v3,v4)

'''
연습문제
(1,2,3), (4,1,-2), (-1,2,-1)은 선형독립인가?
'''
#풀이
v3 = np.array([1,2,3])
v4 = np.array([4,1,-2])
v5 = np.array([-1,2,-1])
lin_dep(v3,v4,v5)