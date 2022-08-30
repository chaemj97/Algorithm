
N = int(input())
arr = list(map(int,input().split()))


min_s = arr
max_s = arr

# 메모리 초과 때문에
for i in range(1,N):
    a,b,c = map(int,input().split())
    max_s = [a + max(max_s[0],max_s[1]), b + max(max_s), c + max(max_s[1],max_s[2])]
    min_s = [a + min(min_s[0],min_s[1]), b + min(min_s), c + min(min_s[1],min_s[2])]

print(max(max_s),min(min_s))