# https://chaemi720.tistory.com/151

from itertools import combinations

# 소수 확인
def prime(sum):
    for i in range(2,sum):
        # 하나라도 나누어 떨어지면 소수 아님
        if not sum%i:
            return False
    # 2~(자기자신-1) 중 하나라도 나누어 떨어지지 않으면 소수
    return True
            

def solution(nums):
    answer = 0
    # 3개씩 조합으로 뽑아보자
    for three in list(combinations(nums,3)):
        # 합 구하기
        three_sum = sum(three)
        # 그 합이 소수인가?
        if prime(three_sum):
            # 맞으면 +1
            answer += 1

    return answer



# 시간초과 대비용

# from itertools import combinations

# def solution(nums):
#     cnt = 0
#     # 3개씩 조합으로 뽑기
#     for num in list(combinations(nums, 3)):
#         # 합
#         N = sum(num)
        
#         # 소수인지 확인
#         # 2~int(루트(N))까지 확인
#         for i in range(2, int(N**0.5)+1):
#             # 나누어 떨어지면 소수X
#             if N % i == 0:
#                 break
#         # 하나라도 나누어 떨어지지 않으면 소수
#         else:
#             cnt += 1
        
#     return cnt