# https://chaemi720.tistory.com/169

import math

# hh:mm을 minutes로 바꾸기
def changeToMinutes(time):
    H,M = map(int,time.split(':'))
    return H*60 + M

def solution(fees, records):
    # 차량 번호가 작은 자동차부터
    records.sort(key = lambda x:x[6:10])
    
    # 차 번호에 [time]
    cars = {}
    for record in records:
        time, car_num, inout = record.split()
        time_minutes = changeToMinutes(time)
        # 들어온 적 없는 차량?
        if car_num not in cars:
            cars[car_num] = [time_minutes]
        else:
            cars[car_num].append(time_minutes)
    park_time = []
    last_time = 23*60 + 59
    # 차량 주차 시간 구하기
    for car in cars.values():
        parking_time = 0
        for i in range(0,len(car),2):
            try:
                parking_time += car[i+1]-car[i]
            # 그날 출차 되지 않았다면
            except:
                parking_time += last_time - car[i]
        park_time += [parking_time]

    money = []
    # 주차 요금 계산
    for m in park_time:
        # 기본 시간보다 적게 이용시 기본요금만
        if m <= fees[0]:
            money += [fees[1]]
        else:
            money += [fees[1] + math.ceil((m-fees[0])/fees[2])*fees[3]]
            
    return money