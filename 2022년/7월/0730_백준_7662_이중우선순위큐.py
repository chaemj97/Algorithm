from sys import stdin
import heapq
input = stdin.readline

# 테스트 케이스
T = int(input())
for _ in range(T):
    # 연산의 개수
    k = int(input())
    # 최소힙, 최대힙 동시에
    min_heap = []
    max_heap = []
    used = [False] * 1000001

    for i in range(k):
        oper, num = input().split()
        # 삽입
        if oper == 'I':
            heapq.heappush(min_heap,(int(num),i))
            heapq.heappush(max_heap,(-int(num),i))
            # 삽입 표시해주기
            used[i] = True

        # 삭제
        else:
            # 최댓값 삭제
            if num == '1':
                # 최소힙에서 삭제해서 남아있지 않다면 최대힙에서 삭제해야함
                # used[max_heap[0][1]] == False : heap에 없다 == (최소힙에서 삭제)
                while max_heap and not used[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                # 데이터가 남아있어야 버릴 수 있음
                if max_heap:
                    used[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            # 최솟값 삭제
            else:
                while min_heap and not used[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    used[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # 한쪽이 다 비워진 경우 대비
    while max_heap and not used[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not used[min_heap[0][1]]:
        heapq.heappop(min_heap)

    # 결과
    # 데이터의 최댓값과 최솟값 출력
    if max_heap and min_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print('EMPTY')