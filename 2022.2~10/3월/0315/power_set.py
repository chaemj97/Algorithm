# (1,2,3,4,5)
# 마을이 있다, 주민이 있다.
# 편의상 1번부터 N번까지 번호를 매기겠다...
# 두 그룹으로 나누어라... >> 부분집합
# 각 요소들이 부분집합에 포함되는 경우와, 포함되지 않는 경우
# idx : 부분집합에 포함 여부를 결정할 요소 인덱스
# selected : 각 idx 번째 요소가 부분집합에 포함되는지 표시하는 배열
# [0,0,0,0,0] -> [1,0,0,1,0] : 1,4가 포함
def solve(idx,selected):
    global min_result
    if idx == N: # 모든 부분집합 포함여부 결정된 상황
        # print(selected) : 부분집합 포함 여부
        group1 = []
        group2 = []
        for i in range(N):
            if selected[i]:
                group1.append(arr[i])
            else:
                group2.append(arr[i])
        # 그룹이 만들어진 상태
        # 그룹을 이용해서 필요한 연산 수행

        # 두 개의 그룹으로 만들어서 일을 했을때 업무량의 차이가 최소가 되도록
        # 그룹의 업무량을 각각 출력
        # 각 그룹별로 모두 연결되어있는 그룹??
        work1 = sum(group1)
        work2 = sum(group2)
        result = abs(work1-work2)
        if result < min_result:
            min_result = result
        return
    else:
        # idx 번째 요소의 부분집합 포함여부 결정
        # idx+1 번째 요소의 부분집합 포함여부 결정하기
        selected[idx] = 0 # idx 번째 요소는 부분집합에 포함되지 않는다.
        solve(idx+1,selected)

        selected[idx] = 1 # idx 번째 요소는 부분집합에 포함된다.
        solve(idx + 1, selected)

min_result = 0xfffffffffff
arr = [2,5,7,1,9,10,2,3,6]
N = len(arr)
selected = [0] * N
solve(0,selected)
print(min_result)