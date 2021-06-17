def solution(x, n):
    # answer=[x]
    # for i in range(n-1):
    #     answer.append(answer[-1]+x)
    # return answer
    return [i*x+x for i in range(n)]


print(solution(2,5))