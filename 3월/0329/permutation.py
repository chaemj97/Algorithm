N = 5
arr = [1,2,3,4,5]

# 0번 인덱스부터, N-1번 인덱스까지 들어갈 수 있는 요소 하나씩 넣어보기
# idx에 어떤 숫자를 넣을 것인지 결정
# p_arr : 순열을 저장할 배열
# used : 요소 사용여부 표시 [0,1,0,1,0]
def perm(p_arr,used,idx):
    if idx >= N:
        print(p_arr)
        return
    # p_arr[idx] 요소에 넣을 수 있는 모든 숫자들 다 넣어보기
    # idx보다 앞선 인덱스에서 사용한 숫자는 재사용 X
    for i in range(N): # 모든 요소를 대상으로
        if not used[i]: # i번째 요소가 사용되지 않았따면 사용가능
            p_arr[idx] = arr[i]
            used[i] = 1 # i번 요소 사용했음을 표시
            perm(p_arr,used,idx+1)
            used[i] = 0

perm([0]*N,[0]*N,0)