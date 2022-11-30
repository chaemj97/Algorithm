arr = [2,5,7,1,9,10,2,3,6]
N = len(arr)
K = 4
# idx : 조합 포함여부 결정할 idx번째 요소
# selected : 조합 포함여부 표시 배열
# cnt : 조합에 포함된 요소 개수(K를 넘어갈 수 없다)
def solve(idx,seleted,cnt):
    if cnt == K: # 조합이 안성되었음
        print(seleted)
        return

    if idx == N: # 모든 요소를 다 결정했다고 해서 결과가 나온건 아님
        # 그냥 아무연산 안하면 됨 : 다 확인했으나 답 없음
        return
    seleted[idx] = 1
    solve(idx+1,seleted,cnt+1)
    seleted[idx] = 0
    solve(idx + 1, seleted, cnt)

solve(0,[0]*N,0)