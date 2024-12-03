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






a = Solution().myAtoi(" -042")