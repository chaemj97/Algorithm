import sys
sys.stdin = open('sample_input_6.txt')


for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    # 덤프 횟수 만큼 평탄화 작업을 반복(반복문)
    # 최대 높이 찾고
    # 최저 높이 찾아서
    # 최대 높이 -1
    # 최저 높이 +1
    for _ in range(N):
        max_idx = 0
        min_idx = 0
        for i in range(100):  # 상자 높이 중 최고, 최저 찾기 반복문
            if boxes[i] > boxes[max_idx]:
                max_idx = i
            if boxes[i] < boxes[min_idx]:
                min_idx = i
        # 반복문이 끝나면 최고 높이와 최저 높이의 위치를 알 수 있음
        # 덤프 작업
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    # 덤프작업후에 최대, 최소 높이 찾기
    max_idx = 0
    min_idx = 0
    for i in range(100):  # 상자 높이 중 최고, 최저 찾기 반복문
        if boxes[i] > boxes[max_idx]:
            max_idx = i
        if boxes[i] < boxes[min_idx]:
            min_idx = i

    print(f'#{tc} {boxes[max_idx] - boxes[min_idx]}')
