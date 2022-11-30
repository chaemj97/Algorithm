class MyQueue:
    def __init__(self):
        self.front = self.rear = -1
        self.queue = [0] * 5
    def enqueue(self,data):
        # 제일 뒤에 삽입
        if self.is_full():
            print('큐가 다 찼습니다.')
        else:
            self.rear += 1
            self.queue[self.rear] = data

    def dequeue(self):
        # 현재 가장 앞에 있는 요소를 반환하고 (삭제)
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            self.front += 1
            return self.queue[self.front]

    def is_full(self):
        if self.rear == len(self.queue)-1:
            return True
        else:
            return False

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

# queue = MyQueue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(6)
#
# print(queue.dequeue())

#교수님 git에는 원형큐
class CircleQueue:
    def __init__(self):
        self.front = self.rear = 0
        self.queue = [0] * 5
    def enqueue(self,data):
        # 제일 뒤에 삽입
        if self.is_full():
            print('큐가 다 찼습니다.')
        else:
            self.rear  = (self.rear + 1) % len(self.queue)
            self.queue[self.rear] = data

    def dequeue(self):
        # 현재 가장 앞에 있는 요소를 반환하고 (삭제)
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]

    def is_full(self):
        if (self.rear + 1) % len(self.queue) == self.front:
            return True
        else:
            return False

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

queue = CircleQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())