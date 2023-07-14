import sys
input = sys.stdin.readline
# 용액의 수
N = int(input())
liquids = list(map(int,input().split()))

# 양끝에서 중앙으로
one_idx = 0
two_idx = N-1
answer = abs(liquids[one_idx] + liquids[two_idx])
answer_one = one_idx
answer_two = two_idx

# one_idx는 two_idx보다 항상 작다
while one_idx < two_idx:
    # 합
    s = liquids[one_idx] + liquids[two_idx]
    # 합이 answer보다 0에 가까운가?
    if abs(s) < answer:
        answer = abs(s)
        answer_one = one_idx
        answer_two = two_idx
        # 0인가?
        if answer == 0:
            break
    # 합이 음수인가? -> 음수의 절댓값 낮추기
    if s < 0:
        one_idx += 1
    # 합이 양수인가?
    else:
        two_idx -= 1

# 정답 출력
print(liquids[answer_one],liquids[answer_two])