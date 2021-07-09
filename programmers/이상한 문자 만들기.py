def solution(s):
    for i in range(len(s)):
        s[i] = [s[i].lower(), s[i].upper()][i&1]
    return s

print(solution("try hello would"))