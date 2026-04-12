class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        count=0
        for i in seen:
            if i-1 not in seen:
                current=i
                lenght=1
                while current+1 in seen:
                    current+=1
                    lenght+=1
                count=max(count,lenght)
        return count