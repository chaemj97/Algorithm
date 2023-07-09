'''
    접근법
        세그먼트 트리
        구간 합
    
'''
import sys
input = sys.stdin.readline

# 숫자의 개수, 턴의 수
n,q = map(int,input().split())
num = list(map(int,input().split()))

# 0. 세그먼트 트리 만들기
seg_tree = [0 for _ in range(n*4)]
def make_seg(idx,left,right):
    # 1. 구간에 데이터가 1개
    if left == right:
        seg_tree[idx] = num[left]
        return seg_tree[idx]
    # 2. 구간에 데이터가 여러개
    mid = (left + right)//2
    # 왼쪽 자식
    left_vlue = make_seg(idx*2,left,mid)
    # 오른쪽 자식
    right_vlue = make_seg(idx*2+1,mid+1,right)
    seg_tree[idx] = left_vlue + right_vlue
    return seg_tree[idx]
make_seg(1,0,n-1)

# 1. 세그먼트 구간 합 구하기
def find_seg(idx,left,right,x,y):
    # 1. 구하려는 구간이 현재 구간과 겹치지 않는다.
    if y < left or right < x:
        return 0
    # 2. 구하려는 구간이 현재 구간을 포함한다.
    if x <= left and right <= y:
        return seg_tree[idx]
    # 3. 구하려는 구간이 현재 구간과 일부 겹친다.
    mid = (left+right)//2
    left_value = find_seg(idx*2,left,mid,x,y)
    right_value = find_seg(idx*2+1,mid+1,right,x,y)
    return left_value+right_value
    
# 2. 세그먼트 값 바꾸기
def change_seg(idx,left,right,a,b):
    # 1. 구간에 데이터가 1개인데 그게 a번째 값이다.
    if left == right == a:
        seg_tree[idx] = b
        return 
    # 2. 현재 구간에 a번째 값이 포함되어 있지 않다.
    if a < left or right < a:
        return
    # 3. 현재 구간에 a번째 값이 포함된다.
    mid = (left+right)//2
    change_seg(idx*2,left,mid,a,b)
    change_seg(idx*2+1,mid+1,right,a,b)
    seg_tree[idx] = seg_tree[idx*2]+seg_tree[idx*2+1]
    return
    
for _ in range(q):
    # x~y의 합 구하기, a번째 수는 b로 바뀍
    x,y,a,b = map(int,input().split())
    # 1. x~y합 구하기
    x, y = min(x,y),max(x,y)
    print(find_seg(1,0,n-1,x-1,y-1))
    # 2. a번째 수를 b로 바꾸기
    change_seg(1,0,n-1,a-1,b)