# https://chaemi720.tistory.com/152

def solution(d, budget):
    answer = 0
    # 최대한 많은 부서의 물품을 구매 -> 신청 금액이 낮은 부서부터 지원
    # 지원금액을 오름차순으로 정렬
    d.sort()
    
    for i in d:
        # 이 부서를 지원해도 되는가? == 이 부서를 지원해줘도 예산이 남는가?
        if budget - i >= 0:
            budget -= i
            answer += 1
            
    return answer