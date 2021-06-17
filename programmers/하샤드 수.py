def solution(x):
    return x%sum(list(map(int,str(x))))==0

print(solution(18))