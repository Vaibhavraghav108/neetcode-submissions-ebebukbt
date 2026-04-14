class Solution:
    def isPalindrome(self, s: str) -> bool:
        target=""
        for i in range(len(s)):
            if s[i].isalnum():
                target+=s[i].lower()
        left=0
        right=len(target)-1
        while left<right:
            if target[left]!=target[right]:
                return False
            left+=1
            right-=1
        return True
