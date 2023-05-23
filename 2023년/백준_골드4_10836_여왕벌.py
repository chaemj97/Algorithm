'''
    접근법
        up : 계속 증가하는 값
        왼쪽, 왼쪽위, 위 중 위가 제일 큰 값
    
'''

import sys
input = sys.stdin.readline

# 가로 세로, 날짜 수
m,n = map(int,input().split())
# 애벌레 크기
larva = [[1]*m for _ in range(m)]
# 애벌레가 자라는 정도
up = [0]*(2*m-1) # 계속 증가하는 값
for _ in range(n):
    zero,one,two = map(int,input().split())
    for i in range(zero,zero+one):
        up[i] += 1
    for i in range(zero+one,2*m-1):
        up[i] += 2


# 왼쪽열, 위쪽행 애벌레 성장
k = 0
for j in range(m-1,-1,-1):
    larva[j][0] += up[k]
    k += 1
for j in range(1,m):
    larva[0][j] += up[k]
    k += 1
    
# 나머지 성장
for r in range(1,m):
    for c in range(1,m):
        larva[r][c] = larva[0][c]
        
# 결과 출력
for r in range(m):
    print(*larva[r])

