'''
    접근법
        1. k : 왼쪽부터 앞에것이 더 작은 것 선택
        2. m : 오른쪽부터 s[k]보다 큰 거 찾기
        3. s[k]와 s[m] 바꾸기
        4. s[k]뒤 뒤집기
    
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = list(input().rstrip())
    length = len(s)
    
    # s 다음 단어 만들기
    
    k = -1
    for i in range(length-1):
        # 오름차순?
        if s[i] < s[i+1]:
            k = i
    
    # 문자가 다 오름차순 == 마지막 단어
    if k == -1:
        print(''.join(s))
        continue
    
    for j in range(length-1,-1,-1):
        if s[k] <s[j]:
            m = j
            break
        
    s[k],s[m] = s[m],s[k]
    s = s[:k+1] + list(reversed(s[k+1:]))
    print(''.join(s))
    