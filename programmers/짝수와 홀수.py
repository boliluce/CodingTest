def solution(num):
    #return "Even" if num%2==0 else "Odd"
    return ["Even", "Odd"][num&1]

print(solution(3))
print(solution(4))
