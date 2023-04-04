'''
    접근법 1
        수열의 중복을 제거 후 오름차순 정렬
        이 후 중복 조합으로 M개씩 뽑기
'''
from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
# 수열 중복제거 + 오름차순
arr = sorted(set(map(int,input().split())))

# 중복 조합
for com in combinations_with_replacement(arr,M):
    print(*com)