import sys
sys.stdin = open('sample_input_6.txt')

# 가장 높은 상자의 index 찾기
def max_v(ls):
    max_value = arr[0]
    max_idx = 0
    for i in range(len(ls)):
        if max_value < ls[i]:
            max_value = ls[i]
            max_idx = i
    return max_idx

# 가장 낮은 상자의 index 찾기
def min_v(ls):
    min_value = arr[0]
    min_idx = 0
    for j in range(len(ls)):
        if min_value > ls[j]:
            min_value = ls[j]
            min_idx = j
    return min_idx

for tc in range(1,11):
    # 덤프 횟수
    D = int(input())
    # 상자의 높이
    arr = list(map(int,input().split()))

    # 가장 높은 상자의 높이 -1, 가장 낮은 상자의 높이 +1

    while D:
        arr[max_v(arr)] -= 1
        arr[min_v(arr)] += 1
        D -= 1

        # 덤프가 끝나기 전에 가장 높은 상자의 높이와 가장 낮은 상자의 높이의 차이가 1이내이면 멈추기
        if arr[max_v(arr)] - arr[min_v(arr)] <= 1:
            result = arr[max_v(arr)] - arr[min_v(arr)]
            break
    # 덤프 다 한 후 가장 높은 상자의 높이와 가장 낮은 상자의 높이의 차 구하기
    result = arr[max_v(arr)] - arr[min_v(arr)]
    print('#{} {}'.format(tc,result))