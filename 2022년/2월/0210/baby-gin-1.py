# 탐욕 알고리즘: 각 상황에서 최선의 선택을 해 나가면서 해를 찾는 과정

arr = [1, 1, 1, 4, 6, 5]
N = 6
# numbers : 각 숫자들의 개수를 포함하는 배열
numbers = [0] * 10
# 각 요소의 개수 세기
for i in range(N):
    numbers[arr[i]] += 1

# 앞쪽부터 run인지 triplet인지 검사, triplet부터 검사
i = 0
while i < 10:
    if numbers[i] >= 3: # 같은 숫자가 3개 이상 -> triplet!
        numbers[i] -= 3
    if numbers[i] > 0: # run인지 검사 - > 연속 3개의 숫자가 1개 이상씩 있는가
        if i < 7:
            if numbers[i] == numbers[i+1] and numbers[i] == numbers[i+2]:
                numbers[i] -= 1
                numbers[i+1] -= 1
                numbers[i+2] -= 1
    i += 1

if sum(numbers) == 0:
    print('baby-gin')
else:
    print('not baby-gin')
