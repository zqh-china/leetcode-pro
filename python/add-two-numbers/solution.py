# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        curr = head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            if l1 is None:
                l1_val = 0
            else:
                l1_val = l1.val
                l1 = l1.next
            if l2 is None:
                l2_val = 0
            else:
                l2_val = l2.val
                l2 = l2.next
            num = l1_val + l2_val + carry
            carry = num // 10
            sum_node = ListNode(num%10)
            curr.next = sum_node
            curr = sum_node
        return head.next






if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    r = s.addTwoNumbers(l1, l2)
    print("OK")
