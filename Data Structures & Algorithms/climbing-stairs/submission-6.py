class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2: #why this becuase it will fail for n=1 because you have already dp[2] so out of index
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-2]+dp[i-1]
        
        return dp[n]