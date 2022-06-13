class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for c in s:
            if c.isalpha() or c.isdigit():
                res.append(c.lower())
        for i in range(len(res)//2):
            if res[i] != res[len(res)-i-1]:
                return False
        return True