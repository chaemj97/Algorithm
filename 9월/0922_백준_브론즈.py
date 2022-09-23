# 2609 최대공약수와 최소공배수
# one, two = map(int,input().split())

# def gcd(a,b):
#     while b>0:
#         a,b = b, a%b
#     return a

# def lcm(a,b):
#     return (a*b)//gcd(a,b)

# print(gcd(one,two))
# print(lcm(one,two))

# 10250 ACM 호텔
# T = int(input())
# for _ in range(T):
#     H,W,N = map(int,input().split())
#     if N%H:
#         num = str(N%H)
#         num += str(N//H+1).zfill(2)
#     else:
#         num = str(H)
#         num += str(N//H).zfill(2)
#     print(num)

