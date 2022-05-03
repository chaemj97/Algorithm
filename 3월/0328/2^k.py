# 재귀 Recursion
def Power_of_2R(k):
    if k == 0:
        return 1
    else:
        return 2 * Power_of_2R(k-1)

print(Power_of_2R(5)) # 32

# 반복 Iteration
def Power_of_2I(k):
    i = 0
    power = 1
    while i < k:
        power = power * 2
        i += 1
    return power

print(Power_of_2I(5)) # 32