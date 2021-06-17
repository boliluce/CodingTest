def solution(array, commands):
    answer = []
    for (i,j,k) in commands:
        answer.append((sorted(array[i-1:j]))[k-1])
        #print(answer)
    return answer

print(solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]]))

# answer = []
# list = [1,5,2,6,3,7,4]
# answer.append((sorted(list[2-1:5]))[3-1])
# print(answer)