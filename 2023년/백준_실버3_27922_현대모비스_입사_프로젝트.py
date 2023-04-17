'''
    접근법 1
        역량 3개 중 2개 선택
            2개 역량의 합이 큰 순서대로 정렬 후 상위 K개 더하기
        비교

'''
import sys
input = sys.stdin.readline

# 강의의 총 개수, 수강할 강의 수
N,K = map(int,input().split())
lecture = [list(map(int,input().split())) for _ in range(N)]

answer = 0
# 역량 3개 중 2개 선택
for a,b in [[0,1],[0,2],[1,2]]:
    # 2 역량의 합이 큰 순서대로 정렬
    lecture.sort(key=lambda x:-(x[a]+x[b]))
    s = 0
    for i in range(K):
        s += lecture[i][a] + lecture[i][b]
    answer = max(answer,s)
    
print(answer)