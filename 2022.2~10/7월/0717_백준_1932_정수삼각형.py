

from sys import stdin
input = stdin.readline

# 삼각형의 크기
n = int(input())
triangle = [list(map(int,input().split())) for _ in range(n)]

# 윗 층 값 더하기
for r in range(1,n):
    for c in range(len(triangle[r])):
        # 오른쪽 대각선뿐 일 경우
        if c == 0:
            triangle[r][c] = triangle[r][c] + triangle[r-1][c]
        # 왼쪽 대각선뿐 일 경우
        elif c == len(triangle[r]) - 1:
            triangle[r][c] = triangle[r][c] + triangle[r-1][c-1]
        # 둘 다 있을 경우 (둘 중 큰거 더하기)
        else:
            triangle[r][c] = triangle[r][c] + max(triangle[r-1][c], triangle[r-1][c-1])

# 마지막 층이 하나하나 선택한 결과 -> 그 중 가장 큰거
print(max(triangle[n-1]))
