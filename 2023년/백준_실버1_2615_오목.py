'''
    접근법
    
'''
import sys
input = sys.stdin.readline

# 바둑판
arr = [list(map(int,input().split())) for _ in range(19)]

for r in range(19):
    for c in range(19):
        # 바둑알이 놓임
        if arr[r][c] != 0:
            start = arr[r][c]
            # 가로, 오른쪽 아래 대각선, 세로, 오른쪽 위 대각선 
            for dr,dc in [[0,1],[1,1],[1,0],[-1,1]]:
                # 연속 바둑돌 개수
                cnt = 1
                
                # 한 칸 이동
                nr = r + dr
                nc = c + dc
    
                # 범위 내 + 시작점 바둑돌과 같다
                while 0 <= nr < 19 and 0 <= nc < 19 and start == arr[nr][nc]:
                    cnt += 1
                    
                    # 5개 완성
                    if cnt == 5:
                        # 6개 연속 체크
                        # 연속 5개 바로 앞이 같은 거면 안됨
                        if 0 <= r - dr < 19 and 0 <= c - dc < 19 and start == arr[r-dr][c-dc]:
                            break
                        # 연속 5개 바로 뒤가 같은 거면 안됨
                        if 0 <= nr + dr < 19 and 0 <= nc + dc < 19 and start == arr[nr+dr][nc+dc]:
                            break
                        # 성공
                        print(start)
                        print(r+1,c+1)
                        sys.exit(0)
                    
                    # 이동
                    nr += dr
                    nc += dc
                               
# 아직 판정이 안 난 경우
print(0)