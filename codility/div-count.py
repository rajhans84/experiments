# DivCount
import math
def solution(a, b, k):
    s = math.ceil(a/k)
    e = math.floor(b/k)
    return e - s + 1
print(solution(4,101,23))