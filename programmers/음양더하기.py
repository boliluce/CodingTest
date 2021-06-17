def solution(absolutes, signs):
    answer = 0
    for idx, val in enumerate(absolutes):
        answer += val if signs[idx] else -val
    return answer

print(solution([4,7,12],[True,False,True]))