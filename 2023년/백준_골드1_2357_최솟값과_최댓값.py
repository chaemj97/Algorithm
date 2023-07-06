'''
    접근법
        세그먼트 트리 이용
        세그먼트 트리에 각 범위의 [최솟값,최댓값] 저장
    
'''
import sys
input = sys.stdin.readline

# n개의 정수, m개의 쌍
n,m = map(int,input().split())
num = [int(input()) for _ in range(n)]

# 세그먼트 트리 만들기
# seg_tree[1] = [a,b] : idx 0~n-1에서 가장 작은 값, 큰 값
# seg_tree[2] = [c,d] : idx 0~(n-1)//2에서 가장 작은 값, 큰 값
seg_tree = [[] for _ in range(n*4)]

def make_seg_tree(idx,left,right):
    # 구간의 값이 1개
    if left == right:
        seg_tree[idx] = [num[left],num[left]]
        return seg_tree[idx]
    
    # 구간의 값이 여러개
    # 자식 노드 중 최댓값, 최솟값 찾기
    mid = (left + right)//2
    
    # 왼쪽 자식
    left_value = make_seg_tree(idx*2,left,mid)
    # 오른쪽 자식
    right_value = make_seg_tree(idx*2+1,mid+1,right)
    
    min_value = min(left_value[0],right_value[0])
    max_value = max(left_value[1],right_value[1])
    seg_tree[idx] = [min_value, max_value]
    return seg_tree[idx]

# 범위(a~b) 내 최솟값, 최댓값 찾기
def find_min_max(a,b,idx,left,right):
    # 1. 찾으려는 범위가 현재 범위에 겹치지 않는다
    if b < left or right < a:
        # 정수 범위 1~10**9
        return [10**9,1]
    # 2. 찾으려는 범위가 현재 범위를 포함한다.
    if a <= left and right <= b:
        return seg_tree[idx]
    # 3. 찾으려는 범위와 현재 범위가 겹친다.
    mid = (left + right)//2
    # 왼쪽 자식
    left_value = find_min_max(a,b,idx*2,left,mid)
    # 오른쪽 자식
    right_value = find_min_max(a,b,idx*2+1,mid+1,right)
    
    min_value = min(left_value[0],right_value[0])
    max_value = max(left_value[1],right_value[1])
    return [min_value,max_value]

make_seg_tree(1,0,n-1)
# 찾기
for _ in range(m):
    # a번 ~ b번 중 최솟값, 최댓값 찾기
    a,b = map(int,input().split())
    answer = find_min_max(a-1,b-1,1,0,n-1)
    print(answer[0],answer[1])