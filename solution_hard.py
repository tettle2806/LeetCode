from typing import List


class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        # Remove leading whitespace
        s = s.lstrip()

        # Check for sign
        sign = 1
        if s.startswith('+'):
            s = s[1:]
        elif s.startswith('-'):
            sign = -1
            s = s[1:]

        # Convert digits to integer
        result = 0
        for c in s:
            if not c.isdigit():
                break
            digit = int(c)
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit

        return sign * result



"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution2:
    def findMedianSortedArrays(self, nums1:List[int], nums2:List[int]) -> float:
        for num in nums2:
            nums1.append(num)

        sorted_nums1 = sorted(nums1)
        if len(sorted_nums1) % 2 != 0:
            index = int((len(sorted_nums1) - 1)  / 2)
            print(sorted_nums1[index])
            return sorted_nums1[index]
        else:
            index = int(len(sorted_nums1) / 2)
            print((sorted_nums1[index] + sorted_nums1[index - 1]) / 2)
            return (sorted_nums1[index] + sorted_nums1[index - 1]) / 2





a = Solution2().findMedianSortedArrays(nums1=[1,3], nums2=[2])