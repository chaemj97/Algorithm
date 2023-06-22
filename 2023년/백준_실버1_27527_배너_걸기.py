'''
    접근법
        m개의 구간에 존재하는 a의 값이 cnt개 이상 존재해야 함

        1. 처음 길이 m의 구간의 요소 개수 세기
            1. cnt개 존재하는지 계속 확인
        2. 1번에서 해결이 되지 않았다면 구간을 1칸씩 뒤로 밀기
            1. 이전 구간의 맨 앞 제외 + 바로 뒤 추가
    
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))

# m개의 구간에서 cnt개 이상의 값이 같아야 함
cnt = 9*m/10
if cnt != int(cnt):
    cnt = int(cnt)+1
    
count = {}
answer = 'NO'
# 앞의 m개 각 Ai 개수 세기
for i in range(m):
    now = A[i]
    count[now] = count.get(now,0) + 1
    # cnt개가 있는가?
    if count[now] == cnt:
        answer = 'YES'
        break

# 그 다음 m개 리스트 개수 세기
for j in range(m,n):
    # 이전 범위의 맨 앞 빼기
    pre = A[j-m]
    count[pre] -= 1
    # 새로운 Ai 추가
    next = A[j]
    count[next] = count.get(next,0) + 1
    # cnt개가 있는가? 
    if count[next] == cnt:
        answer = 'YES'
        break

print(answer)
    