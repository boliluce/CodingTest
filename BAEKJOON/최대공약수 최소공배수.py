# import math
#
# a,b = list(map(int,input().split(' ')))
#
# print(math.gcd(a,b))
# print(math.lcm(a,b))

# 최대공약수 = 유클리드호제법
# 최소공배수 = 두 자연수의 곱 / 최대공약수
# 유클리드호제법 : A를 B로 나눈 나머지 r (A>B)을 다시 b와 나누어 나머지를 구하며, 나머지가 0이 될때, 나누는 수가 최대공약수이다.

def gcd(a,b):
    if(b==0) : return a
    else : return gcd(b, a%b)


a,b = list(map(int,input().split(' ')))
g=gcd(a,b)
l=a*b//g

print(g)
print(l)
