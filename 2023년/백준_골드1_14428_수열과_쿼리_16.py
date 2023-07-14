'''
    접근법
        세그먼트 트리 : [구간의 최솟값, 구간의 최솟값의 인덱스]
    
'''
import sys
input = sys.stdin.readline

# 수열의 크기
n = int(input())
A = list(map(int,input().split()))
# 쿼리의 개수
m = int(input())

# 세그먼트 트리
seg_tree = [0 for _ in range(n*4)]

def make_seg(idx,left,right):
    # 구간의 데이터 1개
    if left == right:
        # [value,idx]
        seg_tree[idx] = [A[left],left]
        return seg_tree[idx]
    
    # 구간의 데이터 여러개
    mid = (left + right)//2
    left_value = make_seg(idx*2,left,mid)
    right_value = make_seg(idx*2+1,mid+1,right)
    if left_value < right_value:
        seg_tree[idx] = left_value
    else:
        seg_tree[idx] = right_value
    return seg_tree[idx]

make_seg(1,0,n-1)

def change_seg(idx,left,right,i,j):
    # 1. 데이터 1개인데 그게 idx이다.
    if left == right == i:
        # [value,idx]
        seg_tree[idx] = [j,i]
        return 
    # 2. 구간에 idx가 없다.
    if i < left or right < i:
        return
    # 3. 구간에 idx가 있다.
    mid = (left + right)//2
    change_seg(idx*2,left,mid,i,j)
    change_seg(idx*2+1,mid+1,right,i,j)

    if seg_tree[idx*2] < seg_tree[idx*2+1]:
        seg_tree[idx] = seg_tree[idx*2]
    else:
        seg_tree[idx] = seg_tree[idx*2+1]

def find_seg(idx,left,right,i,j):
    # 1. 원하는 구간과 현재 구간이 겹치지 않는다.
    if j < left or right < i:
        return [float('inf'),float('inf')]
    # 2. 원하는 구간이 현재 구간을 포함한다.
    if i <= left and right <= j:
        return seg_tree[idx]
    # 3. 원하는 구간과 현재 구간이 일부 겹친다.
    mid = (left + right)//2
    left_value = find_seg(idx*2,left,mid,i,j)
    right_value = find_seg(idx*2+1,mid+1,right,i,j)
    return min(left_value,right_value)
    

for _ in range(m):
    a,i,j = map(int,input().split())
    # Ai를 j로 바꾼다.
    if a == 1:
        change_seg(1,0,n-1,i-1,j)

    # Ai~Aj에서 크기가 가장 작은 값의 인덱스를 출력
    else:
        answer = find_seg(1,0,n-1,i-1,j-1)
        print(answer[1]+1)