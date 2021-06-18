def solution(arr):
    del arr[arr.index(min(arr))]
    return arr if arr else [-1]


print(solution([4,3,2,1]))
print(solution([10]))