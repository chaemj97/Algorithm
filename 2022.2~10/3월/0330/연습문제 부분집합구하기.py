arr = list(range(1,11))
N = 10
# 각 인덱스 요소가 부분집합에 포함되는지 결정
def powerset(selected,idx,sum_v):
    if sum_v > 10:
        # 다른 요소는 골라도 정답이 될 수 없음
        return
    if idx >= N:
        # 모든 요소에 대해서 부분집합 여부 결정
        # print(selected)
        # 원소의 합을 저장할 변수
        sum_e = 0
        sub_set = []
        for i in range(N):
            if selected[i] == 1:
                sum_e += arr[i]
                sub_set.append(arr[i])
        # 부분집합을 출력
        if sum_e == 10:
            print(sub_set)
        return
    else:
        selected[idx] = 1
        powerset(selected,idx+1,sum_v + arr[idx])
        selected[idx] = 0
        powerset(selected, idx + 1,sum_v)

def powerset2(idx,sum_v,sub_set):
    if sum_v > 10:
        return
    if idx >= N:
        if sum_v == 10:
            print(sub_set)
        return
    powerset2(idx + 1, sum_v, sub_set)
    powerset2(idx+1,sum_v+arr[idx],sub_set)
    sub_set.pop()


# powerset([0]*N,0,0)
powerset2(0,0,[])