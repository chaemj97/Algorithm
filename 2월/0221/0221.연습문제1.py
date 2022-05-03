class MyStack():
    # top 변수를 이용해서 구현
    def __init__(self):
        self.top = -1
        self.size = 10
        self.stack = [0] * self.size

    # item 을 마지막 요소 뒤에 추가
    def push(self,item):
        if self.top == self.size-1:
            print('Stack Full')
        else:
            self.top += 1
            self.stack[self.top] = item

    # 마지막 요소를 반환하고 삭제
    def pop(self):
        if self.top == -1:
            print('Empty Stack')
        else:
            self.top -= 1
        return self.stack[self.top+1]

    # peek, isEmpty도 추가로 구현
    def peek(self):
        return self.stack[self.top]

    def isEmpty(self):
        if self.top == -1:
            return 'Empty'
        else:
            return 'Not Empty'

mystack = MyStack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
print(mystack.pop())
print(mystack.pop())
print(mystack.peek())
print(mystack.isEmpty())
print(mystack.pop())
print(mystack.isEmpty())
# 출력결과
# 3 2 1 Not Empty 1 Empty