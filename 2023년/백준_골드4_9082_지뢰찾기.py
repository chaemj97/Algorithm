'''
    접근법
        가능한 지뢰의 수 중 최댓값
            가능한 다 설치
            
        3가지 경우
        1. 맨앞
            num[0] > 0 면 설치
        2. 중간
            num[i] > 0 and num[i-1] > 0 면 설치 
        3. 맨뒤
            num[n-1] > 0 면 설치
    
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 배열 크기
    n = int(input())
    num = list(map(int,input().rstrip()))
    arr = input().rstrip()
    
    answer = 0
    for i in range(n):
        # 맨 앞
        if i == 0:
            # 맨 앞 지뢰 O, 뒤 확인 안해도 됨
            if num[0]:
                num[0] -= 1
                num[1] -= 1
                answer += 1
        # 맨 뒤
        elif i == n-1:
            # 맨 뒤 지뢰 설치 O, 앞 확인 안해도 됨
            if num[n-1]:
                num[n-1] -= 1
                answer += 1
        # 나머지
        else:
            # 해당 위치 지뢰 설치 O, 앞 확인
            if num[i] and num[i-1]:
                num[i] -= 1
                num[i-1] -= 1
                num[i+1] -= 1
                answer += 1
    print(answer)
    