'''
    접근법
        정렬 후 i번째 전화번호가 i+1번째 전화번호의 접두어인지 확인
'''

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 전화번호 수
    n = int(input())
    p_num = [input().rstrip() for _ in range(n)]
    p_num.sort()
    
    # 일관성 default는 yes 
    answer = 'YES'
    for i in range(n-1):
        # i번째 전화번호가 i+1번째 전화번호 접두어인가?
        if p_num[i+1].startswith(p_num[i]):
        # if p_num[i] == p_num[i+1][:len(p_num[i])]:
            answer = 'NO'
            break
    print(answer)