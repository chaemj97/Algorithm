arr = [1,2,3,4]
N = len(arr)
perm = [0]*N
used = [0]*N # idx 번째 요소가 사용되었는지 표시하는 배열
# 새로운 배열의 idx번째 자리에 어떤 숫자를 넣을지 결정
def solve(idx,perm,used):
    if idx == N:
        print(perm)
        return
    # idx 번째 자리에 들어갈 수 있는 숫자 : 모든 요소가 다 들어갈 수 있음
    # 각 요소를 모두 넣어주기
    for i in range(N):
        if not used[i]:
            perm[idx] = arr[i]
            used[i] = 1
            solve(idx+1,perm,used)
            used[i] = 0
solve(0,perm,used)

# used 빼면 중복순열, 있으면 순열