class Solution:  
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n < 2 or s == s[::-1]:
            return s
        
        max_len = 0
        max_left, max_right = 0, 0
        
        for i in range(n):
            # 홀수
            left, right = i, i
            while True:
                if (left >= 0 and right < n) and s[left] == s[right]:
                    if max_len < right - left + 1:
                        max_len = right - left + 1
                        max_left, max_right = left, right
                    left -= 1
                    right += 1
                else:
                    break
            
            # 짝수
            left, right = i, i+1
            while True:
                if (left >= 0 and right < n) and s[left] == s[right]:
                    if max_len < right - left + 1:
                        max_len = right - left + 1
                        max_left, max_right = left, right
                    left -= 1
                    right += 1
                else:
                    break
        
        return s[max_left:max_right+1]
    
        # 시간초과 (완탐?)
        # res = []
        # for i in range(len(s)):
        #     tmp = ""
        #     for j in range(i, len(s)):
        #         tmp += s[j]
        #         if tmp == tmp[::-1]:
        #             res.append(tmp)
        # return sorted(res, key=len, reverse=True)[0]