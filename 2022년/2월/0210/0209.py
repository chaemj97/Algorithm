import sys
sys.stdin = open("inputa.txt")

def getmax(pos):
    maxv = heights[pos-2]
    if maxv < heights[pos-1]:
        maxv = heights[pos-1]
    if maxv < heights[pos+1]:
        maxv = heights[pos+1]
    if maxv < heights[pos+2]:
        maxv = heights[pos+2]
    return  maxv

for tc in range(1,11):
    N = int(input())
    # 빌딩들 높이
    heights = list(map(int,input().split()))
    result = 0
    for i in range(2,N-2):
        m = getmax(i)
        if heights[i] > m:
            result = result + (heights[i]-m)
    print('#{0} {1}'.format(tc,result))
