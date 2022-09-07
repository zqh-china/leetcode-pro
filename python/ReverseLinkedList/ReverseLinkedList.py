# 定义节点类
from shutil import register_unpack_format


class Node:
    def __init__(self, val=None, next=None):
        self.val = val       # 本节点的数据
        self.next = next     # 下一节点的位置

# # 定义链表类
# class LinkedList:
#     def __init__(self, lst):
#         self.head = Node(val=lst[0])
#         p = Node()
#         s = Node()
#         p = copy.deepcopy(self.head)
#         for i in range(1, len(lst)):
#             s.val = lst[i]
#             p.next = s
#             p = p.next
    
#     def travel(self):
#         p = Node()
#         p = self.head
#         while p != None:
#             print(p.val)
#             p = p.next

def reverseLinkedList(head):
    curr = head
    prev = None
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev



if __name__ == "__main__":
    # l1 = LinkedList([1, 2, 3, 4, 5])
    # l1.travel()
    n5 = Node(5, None)
    n4 = Node(4, n5)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)


    n1_after = reverseLinkedList(n1)
    print(n1)
    

