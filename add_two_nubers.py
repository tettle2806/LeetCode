from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

"""
Roman to integer
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000
                          }
        int_value = 0
        for i in range(len(s)):
            if s[i] in roman_numerals:
                if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                    int_value -= roman_numerals[s[i]]
                else:
                    int_value += roman_numerals[s[i]]
            else:
                break
        return int_value
