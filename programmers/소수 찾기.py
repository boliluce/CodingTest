import time
from math import sqrt

def solution2(n):
    answer = 0
    for i in range(2, n+1):
        flag = True
        for j in range(2,i):
            if i%j==0:
                flag = False
                break
        if flag : answer = answer + 1
    return answer


def solution(n):
    #에레스토테네스의 체
    list = [True] * n
    for i in range(2, int(sqrt(n))+1):
        if list[i]:
            for j in range(i+i, n, i):
                list[j] = False
    return len([i for i in range(n) if list[i]==True])-2

print("Start solution 1")
start1 = time.time()
print(solution(10000))
print("Time : " + str(time.time()-start1))

print("Start solution 2")
start2 = time.time()
print(solution2(10000))
print("Time : " + str(time.time()-start2))