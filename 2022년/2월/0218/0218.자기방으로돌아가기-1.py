import sys
sys.stdin = open('sample_input.자기방.txt')

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 돌아가야 할 학생들의 수
    N = int(input())
    # 복도가 겹치는건, 방이 양쪽으로 마주보고 있으니 복도의 길이는 방번호의 절반
    c = [0]*200 # 학생들 동선이 겹치는 개수를 셀 배열
    for _ in range(N):
        r1,r2 = map(int,input().split())
        # 1,2 : 0번 복도
        # 3,4 : 1번 복도
        if r1%2 == 0: # 짝수방이면 1 빼주기
            r1 -= 1
            r1 //= 2
        if r2%2 == 0:
            r2 -= 1
            r2 //= 2
        # r1 > r2로 도는 반복문 작성
        # r2가 크게 만들기
        if r1 > r2:
            r1, r2 = r2, r1
        for i in range(r1,r2+1):
            c[i] += 1

    print(f'#{tc} {max(c)}')


