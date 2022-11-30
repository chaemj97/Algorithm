one = list(input())
two = list(input())

# 순서대로!!
# 부분 수열이 되는 수열 중 가장 긴 것
# 행 : one, 열 : two
arr = [[0]*(len(two)+1) for _ in range(len(one)+1)]

for i in range(1,len(one)+1):
    for j in range(1,len(two)+1):
        # 문자가 같다면
        if one[i-1] == two[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        # 다르면
        else:
            arr[i][j] = max(arr[i][j-1],arr[i-1][j])

# 결과
print(arr[-1][-1])
