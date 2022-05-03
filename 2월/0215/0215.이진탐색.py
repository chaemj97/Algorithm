import sys
sys.stdin = open('input.이진탐색.txt')

# # 문제
# # 짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임 코드 작성
#
def Search(all_page, page):
    start = 1
    end = all_page
    # 탐색 수
    result = 0

    while start <= end:
        middle = int((start + end) // 2)
        # 중앙값과 찾는 값이 같으면 return
        if middle == page:
            result += 1
            return result
        # 찾는 값이 중앙값보다 크면 시작값 = 중앙값
        elif middle < page:
            start = middle
            result += 1
        # 찾는 값이 중앙값보다 작으면 마지막값 = 중앙값
        else:
            end = middle
            result += 1

# T :  테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # P : 책의 전체 쪽 수, A : A가 찾을 쪽 번호, B : B가 찾을 쪽 번호
    P, A, B = map(int,input().split())

    # A 탐색수
    a = Search(P,A)
    # B 탐색수
    b = Search(P,B)

    # 탐색수가 더 작은 값이 이김 -> 결과도출
    if a < b:
        print(f'#{tc} A')
    elif b < a:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')

# # 재귀
# # result : 탐색 수
# def Search(page, start, end, result):
#     if start > end: # 검색 실패
#         return False
#     else:
#         middle = (start + end) // 2
#         if page == middle: # 검색 성공
#             result += 1
#             return result
#         elif page < middle:
#             result += 1
#             return Search(page, start, middle, result)
#         elif page > middle:
#             result += 1
#             return Search(page, middle, end, result)
#
# # T :  테스트 케이스 수
# T = int(input())
# for tc in range(1,T+1):
#     # P : 책의 전체 쪽 수, A : A가 찾을 쪽 번호, B : B가 찾을 쪽 번호
#     P, A, B = map(int,input().split())
#
#     # A 탐색수
#     a = Search(A,1,P,0)
#     # B 탐색수
#     b = Search(B,1,P,0)
#
#     # 탐색수가 더 작은 값이 이김 -> 결과도출
#     if a < b:
#         print(f'#{tc} A')
#     elif b < a:
#         print(f'#{tc} B')
#     else:
#         print(f'#{tc} 0')









