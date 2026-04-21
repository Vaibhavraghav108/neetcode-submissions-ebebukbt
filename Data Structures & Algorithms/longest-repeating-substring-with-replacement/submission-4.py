class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        left=0
        dict={}
        for right in range(len(s)):
            if s[right] in dict:
                dict[s[right]]+=1
            else:
                dict[s[right]]=1
            
            while (right-left+1)-max(dict.values())>k:
                dict[s[left]]-=1
                left+=1
            longest=max(longest,right-left+1)
        return longest