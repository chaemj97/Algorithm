# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# print(fibo(3)) # 2
# print(fibo(4)) # 3
# print(fibo(5)) # 5
# print(fibo(6)) # 8
# print(fibo(7)) # 13


# def fibo_memoization(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(fibo_memoization(n-1) + fibo_memoization(n-2))
#     return memo[n]
#
# memo = [0, 1]
# print(fibo_memoization(3)) # 2
# print(fibo_memoization(4)) # 3
# print(fibo_memoization(5)) # 5
# print(fibo_memoization(6)) # 8
# print(fibo_memoization(7)) # 13

def fibo_dp(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibo_dp(3)) # 2
print(fibo_dp(4)) # 3
print(fibo_dp(5)) # 5
print(fibo_dp(6)) # 8
print(fibo_dp(7)) # 13