# 7 4 2 0 0 6 0 7 0
boxes = list(map(int,input().split()))
# 입력이 제대로 되었는지 확인!

# 해야할 일 : 낙차가 가장 큰 상자의 낙차 구하기
# 1. 모든 열에 대해서 가장 꼭대기에 있는 상자의 낙차 구하기
# 2. 낙차구하기 : 나보다 오른쪽(인덱스가 큰)인 요소의 값이
#    나보다 작으면 -> 낙차 +1
# 금지 sum, max, min, count
max_value = 0
for i in range(len(boxes)):
    # boxes[i] 현재 열의 박스 높이
    # i 열보다 오른쪽에 있는 애들은 다 보기
    cnt = 0 # 낙차
    for j in range(i+1, len(boxes)):
        if boxes[i] > boxes[j]: # 오른쪽에 있는 열의 높이가 더 작으면
            cnt += 1
    # j 반복이 다 돌고 나면 cnt에 i번째열 상자의 낙차가 저장되어 있음
    if max_value < cnt:
        max_value = cnt

print(max_value)
