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



b = Solution().reverse(1534236469)