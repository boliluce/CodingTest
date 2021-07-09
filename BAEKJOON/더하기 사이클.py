tmp=''
cnt = 0
n=input()

if len(n)==1 :
    n = '0' + n

l,r = list(map(int,map(''.join, n)))
while n!=tmp:
    tmp = str(r) + str(l+r)[-1]
    l,r = list(map(int, map(''.join, tmp)))
    cnt+=1
print(cnt)