from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def func(index: int) -> int:
            if index <= 1:
                return 1
            return func(index - 1) + func(index - 2)
            
        return func(n)