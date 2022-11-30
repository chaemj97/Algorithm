
from sys import stdin
input = stdin.readline

# (A^B)%C를 구하라
# 나머지 분배 법칙
# (a*b)%c = ((a%c) * (b%c)) % c
# 지수 법칙
# (5^10) = (5^5)^2
# (5^11) = ((5^5)^2)*5
A, B, C = map(int,input().split())

def multi(A,B):
    # B가 1이면 곱할 필요가 없음
    if B == 1:
        return A % C
    else:
        # 지수 법칙
        mul = multi(A,B//2)
        # B가 짝수라면 : (5^10) = (5^5)^2
        if B % 2 == 0:
            return (mul * mul) % C
        # B가 홀수라면 : (5^11) = ((5^5)^2)*5
        else:
            return (mul * mul * A) % C

print(multi(A,B))
