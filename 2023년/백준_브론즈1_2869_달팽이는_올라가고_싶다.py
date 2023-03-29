'''
    접근법 1
        낮에 올라갔을 때 V보다 큰지 확인
        
        k = 0
        while True:
            k += 1
            if V <= A*k - B*(k-1):
                print(k)
                break
                
        이 코드로 하면 시간 초과
        V <= A*k - B*(k-1) 이 조건을 활용하자
        V-B <= k(A-B)
        (V-B)(A-B) <= k 
        즉, k는 올림((V-B)/(A-B))

        import math
        math.ceil() # 올림
        round() # 반올림
        math.floor() # 내림
'''
import math
import sys
input = sys.stdin.readline

# 낮에 A미터 올라가고 밤에 B미터 미끄러진다. V미터 올라가고 싶다.
A,B,V = map(int,input().split())

print(math.ceil((V-B)/(A-B)))

        
