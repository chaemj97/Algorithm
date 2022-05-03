import sys
sys.stdin = open('GNS_test_input.txt')
#
# # T : 테스트 케이스의 개수
# T = int(input())
# for _ in range(T):
#     # tc : 테스트 케이스의 번호, N : 문자열의 길이
#     tc, N = input().split()
#     # arr : 문자열
#     arr = list(input().split())
#     # num : 숫자 순서
#     num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
#     # result : 결과
#     result = []
#     # 순서대로 나타나면 결과에 넣기
#     for i in num:
#         for j in arr:
#             if i == j:
#                 result.append(j)
#     print(f'{tc}')
#     print(*result)

# print('==============')
# 보강
# # T : 테스트 케이스의 개수
# TC = int(input())
# for _ in range(TC):
#     # tc : 테스트 케이스의 번호, N : 문자열의 길이
#     tc, N = input().split()
#     # TEXT : 문자열
#     TEXT = list(input().split())
#     print(tc)
#     for c in ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']:
#         for t in TEXT:
#             if c == t:
#                 print(c, end=' ')
#     print()
#
# print('==============')

# 교수님
GNS_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
def bubble_sort(target,N):
    # 1. 인접한 요소 2개씩 비교해서 큰 것 뒤로 보내기
    # 2. 1번 모든 요소에 대해서 다 실행하면 가장 큰 수가 제일 뒤로 감
    # 1~2번을 N-1번 반복하면 전체 요소에 대해서 정렬 완료
    for j in range(N-1):
        for i in range(N-1-j):
            # 내 뒷 요소랑 비교해서 크면 뒤로 보내기
            if GNS_dict[target[i]] > GNS_dict[target[i+1]]:
                target[i], target[i+1] = target[i+1], target[i]
    return target

def select_sort(target,N):
    # 0번부터 N-1번까지 자리에 들어갈 요소를 순서대로 찾아서 넣어주기
    for i in range(N-1):
        # i번째 들어갈 요소 찾아서 i번째 넣어주기
        min_idx = i
        # i번보다 인덱스가 빠른 것은 비교하지 않는다(이미 자리를 찾았기 때문)
        for j in range(i+1,N):
            if GNS_dict[target[j]] < GNS_dict[target[min_idx]]:
                min_idx = j
        target[i], target[min_idx] = target[min_idx], target[i]
    return target


def counting_sort(target,N):
    # 요소 중 최대값 만큼의 길이
    count = [0] * 10
    # target의 요소를 순서대로 넣어 줄 배열
    new_arr = [None] * N
    # 각 요소가 몇개씩 나왔는지 개수를 세고
    for i in range(N):
        count[GNS_dict[target[i]]] += 1
    # 각 요소가 들어갈 자리를 계산하기 위해서 누적합을 구함
    for i in range(1,len(count)):
        # count[i] = count[i-1] + count[i]
        count[i] += count[i-1]
    print(count)
    # 각 요소가 들어갈 자리에 넣어줌
    for i in range(N):
        count[GNS_dict[target[i]]] -= 1
        new_arr[count[GNS_dict[target[i]]]] = target[i]
    return new_arr


# T : 테스트 케이스의 개수
TC = int(input())
for _ in range(TC):
    # tc : 테스트 케이스의 번호, N : 문자열의 길이
    tc, N = input().split()
    N = int(N)
    # 테스트 케이스
    target = input().split()
    result = counting_sort(target, N)

    print(tc)
    print(*result)
