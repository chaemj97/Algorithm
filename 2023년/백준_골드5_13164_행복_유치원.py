'''
    접근법
        k = 1
            sum(diff)
        k = 2
            sum(diff[1:])
        k = 3
            sum(diff[2:])
        
        sum(diff[k-1:])
    
'''
import sys
input = sys.stdin.readline

# 원생의 수, 조의 수
n,k = map(int,input().split())
# 원생의 키
height = list(map(int,input().split()))

# 바로 옆 원생과의 키 차이
diff = []
for i in range(n-1):
    diff.append(height[i+1]-height[i])
    
diff.sort(reverse=True)

print(sum(diff[k-1:]))

