# https://chaemi720.tistory.com/170

from itertools import combinations_with_replacement

def solution(n, info):

    # 라이언이 쏠 수 있는 모든 경우
    result = [-1]
    max_score_dif = 0
    for i in list(combinations_with_replacement(range(0,11),n)):
        # 라이언 과녁
        rion = [0]*11
        for j in i:
            rion[j] += 1
        rion = rion[::-1]
        rion_score = 0
        apeach_score = 0
        
        # 라이언 어피치 점수 계산
        for n in range(0,11):
            if rion[n] > info[n]:
                rion_score += 10-n
            elif info[n]:
                apeach_score += 10-n
                
        # 라이언이 이겼고(점수차가 양수), 점수차가 이전 경우보다 크다면
        score_dif = rion_score - apeach_score
        if score_dif > max_score_dif:
            # 가장 낮은 점수를 더 많이 맞힌 경우가 result -> 뽑을 때 작은 것부터 뽑아서 자동으로 됨
            max_score_dif = score_dif
            result = rion
            
    return result