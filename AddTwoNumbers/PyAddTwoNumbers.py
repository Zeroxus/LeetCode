# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = l1
        num2 = l2
        sentinel = ListNode(0)
        d = sentinel
        sum = 0
        while (num1 != None) or (num2 != None):
            sum //=10
            if num1 != None:
                sum +=num1.val
                num1 = num1.next
            if num2 != None:
                sum += num2.val
                num2 = num2.next
            d.next = ListNode(sum%10)
            d = d.next
        if sum//10==1:
            d.next = ListNode(1)
        return sentinel.next