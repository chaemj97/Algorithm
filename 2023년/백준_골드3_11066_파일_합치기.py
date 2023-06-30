'''
    접근법
        dp[i][j]
        두 개의 파일 합치기
        i~k번 파일과 k+1~j번 파일
        dp[i][k] + dp[k+1][j] + sum(novel[i:j+1]) # k는 i~j
        
'''
import sys
input = sys.stdin.readline

# 테스트 케이스
T = int(input())
for _ in range(T):
    # 소설 장 수
    n = int(input())
    novel = [0]+list(map(int,input().split()))
    
    # dp[i][j] : i에서 j까지 합치는데 필요한 최소 비용
    dp = [[0]*(n+1) for _ in range(n+1)]
    
    # 파일 길이 (j-i+1)
    for d in range(2,n+1):
        # 파일 시작점
        for i in range(1,n-d+2):
            # 파일 연결하는 부분중 최소 
            l = []
            for k in range(i,i+d-1):
                l.append(dp[i][k]+dp[k+1][i+d-1])
            
            dp[i][i+d-1] = min(l) + sum(novel[i:i+d])
    # 결과 출력
    print(dp[1][n])