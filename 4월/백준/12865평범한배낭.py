def check(idx,weight,value):
    global max_value
    # 배낭에 넣을 수 있는 무게 인가
    if weight >= K:
        return
    # 확인?
    if idx == N:
        # 최대 무게인가
        if max_value < value:
            max_value = value
        return
    else:
        # 이번 물건 넣어보기
        used[idx] = 1
        check(idx+1,weight+arr[idx][0],value+arr[idx][1])
        # 이번 물건 안 넣어보기
        used[idx] = 0
        check(idx + 1,weight,value)


# N : 물품 수, K : 버틸 수 있는 무게
N,K = map(int,input().split())
# arr[0][:] : 물건의 무게, arr[1][:] : 해당 물건의 가치
arr = [list(map(int,input().split())) for _ in range(N)]

# 배낭에 넣은 물건들의 가치합의 최댓값 출력
max_value = 0
# 물건 넣었는지 유무
used = [0]*(N+1)

check(0,0,0)

print(max_value)