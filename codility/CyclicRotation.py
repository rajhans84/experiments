# CyclicRotation
def solution(A, K):
    n = len(A)
    B = [None]*n
    for i in range(len(A)): 
        j = (i + K) % n
        B[j] = A[i]
    return B        
print(solution([3, 8, 9, 7, 6], 3))