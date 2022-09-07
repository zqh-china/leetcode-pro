class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 先循环一边获取长度，再计算中间节点的位置
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        testNode = head
        i = 1
        while testNode.next is not None:
            i += 1
            testNode = testNode.next
        mid = i // 2
        ans = head
        for j in range(mid):
            ans = ans.next
            j += 1
        return ans

# 快慢指针
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        faster = head
        slower = head
        while faster is not None and faster.next is not None:
            slower = slower.next
            faster = faster.next.next
        return slower




if __name__ == "__main__":
    solution = Solution2()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution.middleNode(l)