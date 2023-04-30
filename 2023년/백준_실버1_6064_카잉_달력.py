'''
    접근법 1
        예제 1
        M,N,x,y = 10,12,3,9
        
        x가 3인 해 : 3번째, 13번째, 23번째, 33번째...
        y가 9인 해 : 9번째, 21번째, 33번째, 45번째...
        
        둘 다 가능 : 33번째 -> 답

'''

import sys
input = sys.stdin.readline

# 테스트 케이스
T = int(input())
for _ in range(T):
    M,N,x,y = map(int,input().split())
    
    answer = x
    # 해가 유효한지 표현
    flag = False
    # 정답은 최대 m*n이다.
    while answer <= M*N:
        '''
        if (answer - x)%M == 0 and (answer-y)%N == 0:
            flag = True
            break
        '''
        if (answer-y)%N == 0:
            flag = True
            break
        # 앞자리가 x인 해의 다음 가능 경우는 M번째 후이다.
        answer += M
        
    if flag:
        print(answer)
    else:
        print(-1)
    