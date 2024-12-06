class Solution:
    def reverse(self, x: int) -> int:

        reverse_str:str = ''
        lst = []
        a = str(x)
        for i in a:
            lst.append(i)

        if lst[0] == '-':
            reverse_str = '-'
            lst.pop(0)

        lst_reverse = list(reversed(lst))


        for i in lst_reverse:
            reverse_str += reverse_str.join(i)

        print(int(reverse_str))
        if -2**31 <= int(reverse_str) <= 2**31 - 1:
            return int(reverse_str)
        else:
            return 0


"""
Maximum Number of Integers to Choose From a Range I
"""


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0  # Initialize the count of numbers that aren't banned and whose sum is within max_sum

        current_sum = 0

        banned_set = set(banned)  # Convert the banned list to a set for faster lookups

        # Iterate through the numbers from 1 to n

        for i in range(1, n + 1):

            # Check if adding the current number would exceed the maximum allowed sum

            if current_sum + i > maxSum:
                break  # If it would, break out of the loop early

            # Check if the current number is not banned

            if i not in banned_set:
                count += 1  # Increment the count of valid numbers

                current_sum += i  # Add the current number to the sum

        # Return the final count of valid numbers

        return count