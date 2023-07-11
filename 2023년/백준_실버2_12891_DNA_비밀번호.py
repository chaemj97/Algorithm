'''
    접근법
        길이 최대 100만
        맨 앞 삭제, 맨 뒤 추가로 진행
'''
import sys
input = sys.stdin.readline

# dna 문자열 길이, 비밀번호 길이
s,p = map(int,input().split())
dna = list(input().rstrip())
goal = list(map(int,input().split()))

dna_s = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}

answer = 0

cnt = [0,0,0,0]
# 초기 p개
for i in range(p):
    cnt[dna_s[dna[i]]] += 1

# 비밀번호로 가능한가?
def check(goal, cnt):
    for k in range(4):
        if goal[k] > cnt[k]:
            return False
    return True

if check(goal, cnt):
    answer += 1
    
# 한 칸 씩 뒤로 밀기
for j in range(s-p):
    # 맨 앞 빼기
    cnt[dna_s[dna[j]]] -= 1
    # 맨 뒤 추가
    cnt[dna_s[dna[j+p]]] += 1

    if check(goal, cnt):
        answer += 1
        
print(answer)