def solution(arr):
    answer = []
    for val in arr:
        if answer[-1:] == [val]: continue
        answer.append(val)
    # for idx in range(1,len(arr)) :
    #     if arr[idx-1] != arr[idx] :
    #         answer.append(arr[idx-1])
    # answer.append(arr[idx])
    return answer

print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([1, 1, 3, 3, 0, 1, 0]))
