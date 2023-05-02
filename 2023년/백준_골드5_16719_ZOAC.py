'''
    접근법 1
        아직 보여주지 않은 문자 중 추가했을 때의 문자열이 사전 순으로 가장 앞에 오도록 하는 문자를 보여주는 것
        
        # 앞자리가 높을수록 사전순으로 더 크다.
        BZZ > CAA
        # 다음에 뽑을 문자는 뽑은 문자 뒤에서 정해야 함
        # 뒤를 다 확인 후 앞 보기
'''

import sys
input = sys.stdin.readline

alpha = input().rstrip()

def check(s,s_idx):
    global answer
    # 빈 문자면 리턴
    if not s:
        return
    # 현재 문자에서 가장 가장 알파벳 찾기
    min_s = min(s)
    min_s_idx = s.index(min_s)
    
    # 알파벳 위치에 맞게 저장
    answer[s_idx+min_s_idx] = min_s
    print(''.join(answer))
    
    # 해당 문자 기준 뒷 문자열
    check(s[min_s_idx+1:],s_idx+min_s_idx+1)
    # 해당 문자 기준 앞 문자열
    check(s[:min_s_idx],s_idx)

answer = ['']*len(alpha)
check(alpha,0)
