# https://chaemi720.tistory.com/145
def solution(lottos, win_nums):
    rank = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    # 오른차순 정렬
    lottos.sort()
    win_nums.sort()
    # 당첨 갯수 세기
    cnt = 0
    for i in win_nums:
        for j in lottos:
            if i == j:
                cnt += 1
                break
    # 0이 모두 다 당첨번호라고 생각
    luck = lottos.count(0)
    return rank[cnt+luck],rank[cnt]

def soultion2(lottos, win_nums):
    rank = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]