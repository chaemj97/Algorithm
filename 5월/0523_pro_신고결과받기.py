# https://chaemi720.tistory.com/137

def solution(id_list, reports, k):
    N = len(id_list)
    answer = [0] * N
    # 신고 당한 사람
    reported = []
    # {신고 한 사람 : 신고 당한 사람}
    reportDic = {id: [] for id in id_list}
    # set으로 중복 제거
    for i in set(reports):
        report = i.split(' ')
        reported.append(report[1])
        reportDic[report[0]].append(report[1])
    # k번 이상 신고 당한 사람 == 정지 된 사람
    K = []
    for j in id_list:
        if reported.count(j) >= k:
            K.append(j)
    # 메일 받는 횟수 구하기
    for key, value in reportDic.items():
        for k in K:
            # 내가 신고해서 정지된 사람
            if k in value:
                answer[id_list.index(key)] += 1
    return answer
print(solution(["con", "ryan"]	,["ryan con", "ryan con", "ryan con", "ryan con"],	3))