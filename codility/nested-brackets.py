# Nested Brackets
def solution(S):
    # write your code in Python 3.6
    stack = []
    extra = 0
    for c in S:
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            extra+= 1
    return 0 if stack or extra > 0 else 1
solution("(()(()(())())")