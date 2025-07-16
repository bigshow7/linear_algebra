import numpy as np

#기초적인 벡터 표현법
def basic_vec(vector):
    print(f"벡터: {vector}")
    print(f"벡터의 차원: {vector.shape}")

#벡터의 크기 비교
def diff_vec(v1, v2):
    if v1.shape != v2.shape:
        raise ValueError("벡터 크기가 달라 계산이 불가합니다!")


#벡터의 연산

#벡터의 합 연산
def cal_vec(v1, v2):
    diff_vec(v1,v2)
    sum_vec = v1 + v2
    sub_vec = v1 - v2
    return sum_vec, sub_vec

#벡터의 스칼라 곱
def mul_scalar(scalar, vec):
    return scalar * vec

#벡터의 내적과 외적
def dot_product(v1,v2):
    diff_vec(v1, v2)        #벡터의 내적도 크기가 같아야 함
    return v1 @ v2

def cross_product(v1,v2):
    diff_vec(v1,v2)         #외적도 크기가 같아야 함
    if v1.shape[0] == 3 and v2.shape[0] == 3:
        return np.cross(v1,v2)
    else:
        raise ValueError("외적은 3차원 벡터만 가능합니다!")


#일반적인 벡터 표현
vector_a = np.array([1,2,3])
basic_vec(vector_a)

#명시적인 열 벡터 표현
vector_b = np.array([[1],[2],[3]])      #2차원 배열 형태로 명시적인 열 벡터로 나타냄
basic_vec(vector_b)

#명시적인 행 벡터 표현
vector_c = np.array([[1,2,3]])          #2차원 배열 형태로 명시적인 행 벡터로 나타냄
basic_vec(vector_c)

#벡터 합, 차
vector_d = np.array([3,5,8])
#cal_vec(vector_a, vector_c)             벡터의 합, 차는 크기가 같아야 함
result = cal_vec(vector_a, vector_d)             #정상적으로 계산됨
print(f"합: {result[0]}")
print(f"차: {result[1]}")

#스칼라 곱
print(f"스칼라 곱: {mul_scalar(5, vector_a)}")

#내적
print(f"내적: {dot_product(vector_a, vector_d)}")

#외적
print(f"외적: {cross_product(vector_a, vector_d)}")