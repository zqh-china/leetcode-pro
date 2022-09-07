# Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # 哪一个链表首个值小，就返回哪个链表头
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
                        
    


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    r = s.mergeTwoLists(l1, l2)
    print('OK')
    print('hhh')