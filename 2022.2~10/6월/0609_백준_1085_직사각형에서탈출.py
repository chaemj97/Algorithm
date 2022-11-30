# https://chaemi720.tistory.com/155

# 현 위치 (x,y)
# 직사각형 : (0,0)~(w,h)
x,y,w,h = map(int,input().split())
# 경계선까지 가로 최소 길이
x_min = min(x,w-x)
# 경계선까지 세로 최소 길이
y_min = min(y,h-y)
# 가로 세로 중 최소 길이가 답
result = min(x_min,y_min)
print(result)