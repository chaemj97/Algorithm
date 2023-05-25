'''
    접근법
        r행이 켜질 때 같이 켜지는 행의 개수 찾기
        1. r행이 켜지는 경우
            1) 0의 개수가 k보다 작아야 함
            2) 0의 개수가 홀수면 k의 개수도 홀수여야함
            3) 0의 개수가 짝수면 k의 개수도 짝수여야함
                ex) lamp[r] = [1,1,0,0,1] 일 때 k가 5면 램프는 절대 켜질 수 없음
        2. r행이 켜질 때 같이 켜지는 행
            r행과 똑같은 상태인 경우
    
'''

import sys
input = sys.stdin.readline

# 탁자 크기
n,m = map(int,input().split()) # 최대 50
lamp = [list(map(int,input().rstrip())) for _ in range(n)] # 1 : 켜짐, 0 : 꺼짐

# 껐다켰다 횟수
k = int(input()) # 최대 1000

answer = 0
for r in range(n):
    zero_cnt = lamp[r].count(0)
    # r행이 켜지는 경우
    # 조건 1. r행의 0의 개수가 k보다 작거나 같다.
    # 조건 2. r행의 0의 개수가 홀수면 k도 홀수 or r행의 0의 개수가 짝수면 k도 짝수
    
    # r행이 켜질 때 같이 켜지는 행의 개수
    on_cnt = 0
    if zero_cnt <= k and zero_cnt%2 == k%2:
        # r행과 똑같은 상태의 행
        on_cnt = lamp.count(lamp[r])
        answer = max(answer,on_cnt)
print(answer)