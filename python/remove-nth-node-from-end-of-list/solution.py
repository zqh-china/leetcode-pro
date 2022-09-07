

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        testNode = head
        while testNode is not None:
            length += 1
            testNode = testNode.next
        rmIndex = length - n
        if rmIndex == 0:              # 删除头节点
            return head.next
        p = head
        j = 0
        while p is not None and j < rmIndex-1:
            p = p.next
            j += 1
        if p is None or p.next is None:
            return
        q = p.next
        p.next = q.next  
        return head

# 双指针
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        faster = head
        slower = head
        if faster.next is None:
            return
        for i in range(n):
            faster = faster.next
        if faster is None:
            return head.next
        while faster.next is not None:
            faster = faster.next
            slower = slower.next
        slower.next = slower.next.next
        return head

# 递归
class Solution3:
    curr = 0
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return
        head.next = self.removeNthFromEnd(head.next, n)
        self.curr += 1
        if self.curr == n:
            return head.next
        return head



if __name__ == '__main__':
    s = Solution3()
    l = ListNode(1, ListNode(2))
    s.removeNthFromEnd(l, 2)
