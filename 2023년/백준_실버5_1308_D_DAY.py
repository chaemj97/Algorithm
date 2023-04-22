'''
    접근법 1
        윤년은 366일

        datetime 클래스는 날짜와 시간을 동시에 표현하기 위해서 사용

'''
from datetime import datetime
import sys
input = sys.stdin.readline

today = list(map(int,input().split()))
d_day = list(map(int,input().split()))

def get_1000_year_day(start_year):
    year_day = 0
    
    for year in range(start_year,start_year+1000):
        # 400으로 나누어 떨어지면 윤년
        if year % 400 == 0:
            year_day += 366
        # 100으로 나누어 떨어지면 평년
        elif year % 100 == 0:
            year_day += 365
        # 4으로 나누어 떨어지면 윤년
        elif year % 4 == 0:
            year_day += 366
        # 나머지
        else:
            year_day += 365
    return year_day

def check_dday(today,d_day):
    today_date = datetime(year=today[0],month=today[1],day=today[2])
    d_day_date = datetime(year=d_day[0],month=d_day[1],day=d_day[2])
    
    # 날짜 차이
    diff = (d_day_date-today_date).days
    # 1000년동안 날짜
    year_day = get_1000_year_day(today[0])
    
    # 캠프가 1000년 이상?
    if diff >= year_day:
        print('gg')
    else:
        print(f'D-{diff}')
        
check_dday(today,d_day)