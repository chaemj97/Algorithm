# https://chaemi720.tistory.com/148

# 세로 R칸, 가로 C칸
R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]

result = 0

# 시간초과 때문에 set
s = set([(0,0,arr[0][0])])

while s and result <26:
    # set은 랜덤으로 pop
    r,c,ls =s.pop()
    # 말이 지날 수 있는 최대의 칸?
    result = max(result,len(ls))
    # 4방향 확인
    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr = r + dr
        nc = c + dc
        # 범위 내에 있고 지금까지 지나온 모든 칸에 적혀 있는 알파벳과 다르다면
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in ls:
            # 추가
            s.add((nr,nc,ls+arr[nr][nc]))

print(result)