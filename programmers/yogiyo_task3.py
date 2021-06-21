def solution(s):
    count = 0
    if s.count('a')%3!=0: return 0
    for i in range(1, len(s)-1):
        for j in range(i+1, len(s)):
            if s[:i].count('a')==s[i:j].count('a')==s[j:].count('a'):
                count += 1

    return count

s1 = "babaa"
s2 = "ababa"
s3 = "aba"
s4 = "bbbbb"
s5 = "bbbbbbbbbbbbbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

# print(solution(s1))
# print(solution(s2))
# print(solution(s3))
# print(solution(s4))
print(solution(s5))