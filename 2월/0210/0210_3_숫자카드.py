import sys
sys.stdin = open('sample_input_3.txt')

# T : 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # N : 카드 장수
    N = int(input())
    # arr : N개의 숫자
    arr = input()

    # 개수 세기
    count = [0]*10
    for i in arr:
        count[int(i)] += 1

    # 개수 가장 큰 거 찾기
    max_v = 0
    idx_v = 0
    for j in range(len(count)):
        if max_v <= count[j]:
            max_v = count[j]
            idx_v = j

    print(f'#{tc} {idx_v} {max_v}')


