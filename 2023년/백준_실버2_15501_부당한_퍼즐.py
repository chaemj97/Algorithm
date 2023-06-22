'''
    접근법
        시작점을 기준으로 two리스트를 one으로 만들기
        (순방향, 역방향 따로)
        둘 중 하나라도 one과 같으면 good
    
'''
import sys
input = sys.stdin.readline

n = int(input())
# one 수열이 two 수열이 될 수 있는지 확인
one = list(map(int,input().split()))
two = list(map(int,input().split()))

# 순방향
# 시작 인덱스
first_idx = two.index(one[0])
two_True = two[first_idx:] + two[:first_idx]

# 역방향
two = two[::-1]
# 시작 인덱스
first_idx = two.index(one[0])
two_False = two[first_idx:] + two[:first_idx]

# print(two_True, two_False)
if one == two_True or one == two_False:
    print('good puzzle')
else:
    print('bad puzzle')