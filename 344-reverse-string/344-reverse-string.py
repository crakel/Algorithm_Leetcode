class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 내장함수 풀이
        # s = s.reverse()
        
        # 투포인터 풀이
        start, end = 0, len(s)-1
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1