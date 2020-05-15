# PermMissingElem
def solution(A):
    sum = 0
    n = len(A) + 1
    for i, v in enumerate(A):
        sum+=v
    seriesSum = n * (n +1) // 2
    return   seriesSum - sum
print(solution([1, 5,4, 2]))