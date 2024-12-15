## 스택의 특징
# 1. 한 곳에서만 자료를 넣고 뺄 수 있다.
# 2. LIFO -> Last in first out, 가장 마지막에 넣은게 빨리 나온다.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # 맨 위에 값을 넣음
    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

        return

    # pop 기능 구현
    # 맨 위의 값을 뺌
    def pop(self):
        if stack.is_empty():
            print("Stack is empty")
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    # 맨 위의 값을 조회
    def peek(self):
        if stack.is_empty():
            return "Stack is empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(4)
print(stack.head.data)

stack.push(3)
print(stack.peek())

stack.push(5)
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())