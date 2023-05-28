'''
    접근법
        1. 몇번째 대각선인지 계산
        [1/1]
        [1/2,2/1]
        [3/1,2/2,1/3]
        [1/4, 2/3, 3/2, 4/1] 
        
        2. 대각선 방향
        홀수번째 대각선 : 오른쪽 위로 ex) [3/1,2/2,1/3]
        짝수번째 대각선 : 왼쪽 아래로 ex) [1/4, 2/3, 3/2, 4/1] 
        
        3. line번째 대각선 원소
        a/b -> a+b = line+1
        
        홀수번째 대각선에서 n(n >= 0)번째 원소 : c = n, r = line+1-n
        짝수번째 대각선에서 n번째 원소 :  r = n, c = line+1-n
'''

import sys
input = sys.stdin.readline

x = int(input())
# 1. 몇번째 대각선인가?
line = 1
while x > line:
    x -= line
    line += 1

# 2. 홀수번째 대각선 ? 짝수번째 대각선?
if line%2: # 홀수번째 : 오른쪽 위로
    a = line+1-x
    b = x
    
else: # 짝수번째 : 왼쪽 아래로
    a = x
    b = line+1-x
    
print(a,'/', b,sep='')