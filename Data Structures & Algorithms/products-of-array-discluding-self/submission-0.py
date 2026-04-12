class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        answer=[1]*len(nums)
        for i in range(0,len(nums)):
            answer[i]=prod
            prod*=nums[i]
        sum=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=sum
            sum*=nums[i]
        return answer
