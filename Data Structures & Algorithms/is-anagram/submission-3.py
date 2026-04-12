class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            if s[i] in dict:
                dict[s[i]]+=1
            else:
                dict[s[i]]=1
        for i in range(0,len(t)):
            if t[i] in dict:
                dict[t[i]]-=1
            else:
                return False
        for val in dict.values():
            if val != 0:
                return False
        return True     