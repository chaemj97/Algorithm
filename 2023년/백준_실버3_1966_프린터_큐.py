'''
    접근법 1
        단계 따라 작성하기 -> 시뮬레이션

        현재 문서의 중요도가 가장 높다면 출력
            출력하면 중요도를 -1로 바꾸기
        가장 높지 않다면 다음 문서 확인

'''

import sys
input = sys.stdin.readline

# 테스트 케이스 수
T = int(input())
for tc in range(T):
    # 문서의 개수, K의 인쇄 순서가 궁금함
    N, K = map(int,input().split())
    # 문서의 중요도
    important = list(map(int,input().split()))

    # 프린트 순서
    print_order = 0
    idx = 0
    while True:
        # 현재 문서의 중요도가 가장 높다면 출력
        if important[idx] == max(important):
            important[idx] = -1
            print_order += 1
            # 몇번째로 인쇄되었는지 알고싶은 문서인가?
            if idx == K:
                break
        # 중요도가 가장 높지 않다면 다음 문서 확인하자
        else:
            idx = (idx+1) % len(important)

    print(print_order)
