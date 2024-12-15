class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self, value):
        self.head = Node(value) # head에 시작하는 노드를 연결

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self): # 링크드 리스트에 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력하는 함수
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
        #print("출력해보세요")

linked_list = Linked_list(5)
linked_list.append(12)
linked_list.append(8)
print(linked_list.print_all())

