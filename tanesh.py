def solution(A):
    result = 0
    for element in A:
        result ^= element
    return result
    pass
