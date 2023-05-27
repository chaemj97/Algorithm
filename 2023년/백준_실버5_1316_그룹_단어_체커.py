'''
    접근법
        구현
    
'''

import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n):
    s = list(input().rstrip())
    s_set = set()
    for i in range(len(s)):
        # s[i] 이 알파벳이 이전에 안나왔다면 추가
        if s[i] not in s_set:
            s_set.add(s[i])
        # 나왔다면
        else:
            # 직전 문자랑 같으면 통과 / 다르면 break
            if s[i] != s[i - 1]:
                break
    else:
        answer += 1
print(answer)