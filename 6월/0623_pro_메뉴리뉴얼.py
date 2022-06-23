# https://chaemi720.tistory.com/181

from itertools import combinations
from collections import Counter

def solution(orders, course):
    # 손님의 메뉴 조합으로 만들 수 있는 모든 코스
    answer = []
    for n in course:
        cooks = []
        for order in orders:
            # 손님의 메뉴 조합으로 만들 수 있는 코스 중 코스 길이가 n인 코스
            cook = list(combinations(sorted(order),n))
            cooks += cook
        # 중복된거 갯수 세기
        cnt = Counter(cooks)

        # (해당 주문 조합이 나온적이 없거나, 해당 조합을 주문한 사람이 1명인 경우)가 아니라면
        if len(cnt) != 0 and max(cnt.values()) != 1: 
            for c in cnt:
                # 가장 많이 함께 주문된 단품메뉴 조합!!!
                # 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담기
                if cnt[c] == max(cnt.values()):
                    answer += ["".join(c)]
            
    return sorted(answer)