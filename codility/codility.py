
def solution(S, K):
    h = { i: 1 for i in S}
    for v in S:
        h[v] += 1
    y = ''    
    y = y.join(val+str(key+1) for key, val in enumerate(h))
    
    return y

print(solution('ABBBCCDDCCC',3))

