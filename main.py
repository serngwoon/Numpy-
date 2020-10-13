import numpy as np
# sum() 합
# mean() 평균
# std() 표준편차
# var() 분산
# max() min() 최대, 최소
# cumsum() 누적합
# cumprod() 누적곱
# A.dot(B), or np.dot(A,B) 행렬곱
# A.transpose() or np.transpose(A) 전치행렬
# np.linalg.inv(A) 역행렬
# np.linalg.det(A) 행렬식
# 배열명[[행위치1, 행위치2, 행위치3...],[열위치1,열위치2,열위치3...]] 2차원행열에서 여러 원소
# [행끼리 벡터값, 열끼리 벡터값]
# 배열명[조건] : 조건을 만족하는 배열 선택

arr1 = np.array([10,20,30,40])
arr2 = np.array([1,2,3,4])
arr3 = np.arange(5)

A = np.array([1,2,3,4]).reshape(2,2)
B = np.array([9,8,7,6]).reshape(2,2)

index1 = np.array([0,10,20,30,40,50])
