class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        
        table = str.maketrans("!?',;.", "      ")
        paragraph = paragraph.translate(table)
        
        for s in paragraph.split():
            s = s.lower()
            if s in dic:
                 dic[s] += 1
            else:
                dic[s] = 1
        
        for b in banned:
            if b in dic:
                dic.pop(b)
        
        max_cnt = max(dic.values())
        for key, value in dic.items():
            if value == max_cnt:
                return key 