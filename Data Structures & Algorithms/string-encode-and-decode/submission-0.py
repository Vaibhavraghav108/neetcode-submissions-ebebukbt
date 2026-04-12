class Solution:

    def encode(self, strs: List[str]) -> str:
        hehe=""
        for i in strs:
            x=len(i)
            final=f"{x}#"+i
            hehe+=final
        return hehe

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            lenght=int(s[i:j])
            j+=1
            res.append(s[j:j+lenght])
            i=j+lenght
        return res