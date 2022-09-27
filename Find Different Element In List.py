import time
import random


def solution(A, B):
    for i in range(len(A)):
        if A[i] not in B:
            return A[i]


def solution2(A, B):
    H = set(B)
    for i in range(len(A)):
        if A[i] not in H:
            return A[i]


L = list(range(0, 100000))
L[-3] = -random.randint(0, 100000)
R = list(range(0, 100000))
st = time.time()
# solution(L, R)
print("elapsed 1", time.time() - st)
st = time.time()
solution2(L, R)
print("elapsed 2", time.time() - st)

# elapsed 2 0.00803828239440918 на 100000
#
