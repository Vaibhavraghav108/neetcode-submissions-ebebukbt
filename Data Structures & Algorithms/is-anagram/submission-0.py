class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
        for i in range(len(t)):
            if t[i] not in dict or dict[t[i]]==0:
                return False
            dict[t[i]]-=1
        return True
        
