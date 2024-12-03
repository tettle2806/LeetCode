# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = int(''.join(map(str, l1)))
        num2 = int(''.join(map(str, l2)))
        result = []
        x = num1 + num2
        while x > 0:
            result.append(x % 10)
            x //= 10


        print(result)
        return result
