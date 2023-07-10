'''
    접근법
        색종이를 붙일수 있는 모든 경우 탐색하기
        붙였다가 안되면 떼기
'''
import sys
input = sys.stdin.readline

# 10 x 10 종이
arr = [list(map(int,input().split())) for _ in range(10)]
# 각 크기의 색종이 개수
paper_cnt = [0,5,5,5,5,5]

# 색종이 붙일 수 있는지 확인
def check_paper(r,c,k):
    # 범위
    if r+k > 10 or c+k > 10:
        return False
    for i in range(r,r+k):
        for j in range(c,c+k):
            if arr[i][j] == 0:
                return False
    return True

# 색종이 붙이기(0), 색종이 떼기(1)
def attach_paper(r,c,k,value):
    for i in range(r,r+k):
        for j in range(c,c+k):
            arr[i][j] = value

def check(a,b):
    global min_paper_cnt
    for r in range(a,10):
        for c in range(b,10):
            if arr[r][c] == 1:
                # 색종이 크기
                for k in range(1,6):
                    # 붙일 수 없다
                    if not check_paper(r,c,k):
                        return
                    # 붙일 수 있다.
                    elif paper_cnt[k] > 0:
                        paper_cnt[k] -= 1
                        # 색종이 붙이기
                        attach_paper(r,c,k,0)
                        # 다음 확인
                        check(a,0)
                        # 색종이 떼기
                        attach_paper(r,c,k,1)
                        paper_cnt[k] += 1
                return 
                        
    # 모든 1을 다 채웠다
    # 사용한 색종이 개수
    min_paper_cnt = min(min_paper_cnt,25-sum(paper_cnt))
    
min_paper_cnt = 25
check(0,0)
# 모두 덮는 것이 불가능?
if min_paper_cnt == 25:
    print(-1)
# 가능
else:
    print(min_paper_cnt)