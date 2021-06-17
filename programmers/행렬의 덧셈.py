def solution(arr1, arr2):
    # answer = []
    # for x,y in zip(arr1,arr2):
    #     a = []
    #     for j,k in zip(x,y):
    #         a.append(j+k)
    #     answer.append(a)
    # return answer
    return [[j+k for j,k in zip(x, y)] for x,y in zip(arr1, arr2)]

def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]


# print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

str = [[[j,k] for j,k in zip(a,b)] for a,b in zip(arr1,arr2)]
print(str)

str = [[j+k] for x,y in zip(arr1, arr2) for j,k in zip(x,y)]
print(str)
