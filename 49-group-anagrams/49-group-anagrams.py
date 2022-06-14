class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            word = "".join(sorted(s))
            if word in res:
                res[word].append(s)
            else:
                res[word] = [s]
        
        return res.values()