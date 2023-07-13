'''
    접근법
        완전탐색 -> 2**n (n 최대 10만) -> 시간초과
        -> 그리디
        
        i번 버튼을 누르면 i-1, i, i+1이 영향을 받는다.
        i번 버튼은 i-1,i,i+1을 누를때 영향을 받는다.
        ## 3가지
        
        -- 버튼을 순서대로 확인 시 
        1번을 바꾸려면 1 or 2번을 바꿔야 함 
        2번을 바꾸려면 2 or 3번을 바꿔야 함 
        3번을 바꾸려면 3 or 4번을 바꿔야 함 
        ## 2가지
        
        -- 1번 버튼을 누르거나/누르지 않았다.
        1번을 바꾸려면 2번을 바꿔야 함
        2번을 바꾸려면 3번을 바꿔야 함
        3번을 바꾸려면 4번을 바꿔야 함
        ## 1가지
'''
import sys
input = sys.stdin.readline

# 전구의 수
n = int(input())
arr = list(map(int,input().rstrip()))
goal = list(map(int,input().rstrip()))

# A을 B로 바꾸기
def check(A,B):
    temp = A[:]
    change = 0
    for i in range(n-1):
        # i번을 바꾸려면 i+1번 전구를 바꿔야함
        # i번 전구의 변화를 줘야하는가?
        if temp[i] != B[i]:
            change += 1
            # i+1번 전구 누르기
            for j in [i,i+1,i+2]:
                if j < n:
                    temp[j] = (temp[j]+1)%2
    # B로 만들 수 있는가?
    if temp == B:
        return change
    # 만들 수 없다.
    else:
        return float('inf')
        

# 1번을 누르지 않았다.
answer1 = check(arr,goal)

# 1번을 눌렀다 -> 1번 2번 상태 바꾸기
arr[0] = (arr[0]+1)%2
arr[1] = (arr[1]+1)%2
answer2 = check(arr,goal)+1

# 결과 출력
answer = min(answer1,answer2)
# 불가능하다?
if answer == float('inf'):
    print(-1)
# 가능하다?
else:
    print(answer)