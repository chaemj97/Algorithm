from pprint import pprint

te = [2, 3, 7, 8, 5 ,4 ,9 ,0 ,6 ,1]
m = max(te)
N = len(te)
# 테트리스 옆으로 눕혀서 놓기
arr = []
for i in te:
    arr += [[1]*i + [0]*(m-i)]
    
# pprint(arr)
arr = list(map(list, zip(*arr)))
# pprint(arr)
# # 채워넣기로 해보자
# # 0행부터 ~ max(te)-1행까지 채워넣기
# # 행
r = 0
# 최소 갯수
cnt = 11
while r < max(te):
    for c in range(N):
        # print(r,c)
        # 0이면 채워야지 -> 막대기 큰거 넣어야함
        if arr[r][c] == 0:
            # 4개짜리부터 넣을 수 있나 확인해보자
            for i in range(4,0,-1):
                if c+i <= N:
                    if 1 not in arr[r][c:c+i]:
                        for k in range(0,i):
                            arr[r][c+k] = cnt
                        cnt += 1
                        break
        
    # 다음 열 확인하자
    r +=1        
print(cnt-11)