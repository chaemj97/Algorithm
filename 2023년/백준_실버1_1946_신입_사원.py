'''
    접근법
        최대 인원 선발
        서류 심사가 가장 낮은 사람부터 선발
            직전에 선발된 사람보다 면접 점수가 낮으면 선발
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 지원자의 수
    n = int(input())
    score = [list(map(int,input().split())) for _ in range(n)]
    # 서류 심사 기준 오름차순 
    score.sort()
    # print(score)
    # [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]]
    
    answer = 1
    s = score[0][1] # 4
    for i in range(1,n):
        # s에 해당하는 사람보다 면접점수가 작다?
        if s > score[i][1]:
            answer += 1
            s = score[i][1]
    print(answer)