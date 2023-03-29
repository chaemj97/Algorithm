# hh:mm을 m분으로 바꾸기
def TimeChange(time):
    hh = int(time[:2])
    mm = int(time[3:])
    return hh*60 + mm

# m분을 hh:mm으로 바꾸기
def Time(time):
    hh = str(time//60).zfill(2)
    mm = str(time%60).zfill(2)
    t = hh + ':' + mm
    return t

def solution(n, t, m, timetable):
    # 온 순서대로 정렬
    timetable.sort()
    
    # 셔틀 출발 시간
    busTime = 9*60
    # 셔틀에 탄 크루
    passenger =[list() for _ in range(n)]
    
    # 셔틀 운행 번호 
    busNum = 0
    # 크루 대기 번호
    num = 0
    
    while busNum < n and num < len(timetable):
        # 크루의 도착시간을 분으로 변경
        arriveTime = TimeChange(timetable[num])
        # 크루가 버스 출발 전에 도착했고 자리가 남았다면 -> 타자
        if arriveTime <= busTime and len(passenger[busNum]) < m:
            passenger[busNum].append(arriveTime)
            num += 1
        # 다음 버스
        else:
            busNum += 1
            busTime += t
    
    # 마지막 셔틀 버스에 자리가 남았다면 마지막 셔틀버스 출발시간에 오면 됨
    if len(passenger[-1]) < m:
        return Time(9*60 + (n-1)*t)
    # 아니라면 맨 마지막 탑승자보다 1분 빨리 오자
    else:
        lastpassenger = passenger[-1][-1]
        return Time(lastpassenger-1)