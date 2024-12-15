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

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.get_node(index -1)

        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node

linked_list = Linked_list(5)
linked_list.append(12)
linked_list.append(8)

linked_list.add_node(1,6)
linked_list.add_node(0,7)
linked_list.print_all()

