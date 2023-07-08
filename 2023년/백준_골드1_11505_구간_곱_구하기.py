'''
    접근법
        2042. 구간 합 구하기
        위 문제와 같은 접근
        ->세그먼트 트리
'''
import sys
input = sys.stdin.readline

# 수의 개수, 수 변경 횟수, 구간의 곱 횟수
n,m,k = map(int,input().split())
num = [int(input()) for _ in range(n)]

seg_tree = [0 for _ in range(n*4)]

# 세그먼트 트리 만들기 - 구간의 곱
# idx : seg_tree의 idx
# left, right : 데이터 구간
def make_seg(idx,left,right):
    # 1. 구간의 수가 1개
    if left == right:
        seg_tree[idx] = num[left]
        return seg_tree[idx] 
    # 2. 구간의 수가 여러개
    mid = (left + right)//2
    left_value = make_seg(idx*2,left,mid)
    right_value = make_seg(idx*2+1,mid+1,right)
    seg_tree[idx] = (left_value*right_value)%(10**9+7)
    return seg_tree[idx]
make_seg(1,0,n-1)

# 수 바꾸기 -> b번째 수가 들어간 seg 모두 바꿔야 함
def change_seg(idx,left,right,b,c):
    # 1. 구간 내에 b가 없다.
    if b < left or right < b: 
        return 
    
    # 2. 구간에 데이터가 1개인데 그게 b다
    if left == right == b:
        seg_tree[idx] = c
        return 
    
    # 3. 구간 내에 b가 있다.
    mid = (left + right)//2
    change_seg(idx*2,left,mid,b,c)
    change_seg(idx*2+1,mid+1,right,b,c)
    seg_tree[idx] = (seg_tree[idx*2]*seg_tree[idx*2+1])%(10**9+7)
    
# b~c 구간의 곱 출력하기
def find_seg(idx,left,right,b,c):
    # 1. 원하는 구간이 현재 구간에 포함되지 X
    if c < left or right < b:
        return 1
    
    # 2. 원하는 구간이 현재 구간에 포함
    if b <= left and right <= c:
        return seg_tree[idx]
    
    # 3. 원하는 구간과 현재 구간이 일부 겹친다.
    mid = (left + right)//2
    left_value = find_seg(idx*2,left,mid,b,c)
    right_value = find_seg(idx*2+1,mid+1,right,b,c)
    return left_value*right_value

for _ in range(m+k):
    a,b,c = map(int,input().split())
    # 수 바꾸기
    if a == 1:
        b -= 1
        change_seg(1,0,n-1,b,c)
    # 구간 곱 구하기
    else:
        b -= 1
        c -= 1
        print(find_seg(1,0,n-1,b,c)%(10**9+7))