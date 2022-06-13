class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for c in s:
            if c.isalpha() or c.isdigit():
                res.append(c.lower())
        
        if res != res[::-1]:
            return False
        return True