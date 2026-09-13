class Solution:
    def countSegments(self, s: str) -> int:
       count = 0
       in_word = False
       for ch in s:
            if ch != " ":
                if not in_word:
                    count += 1
                    in_word = True 
            else:
                in_word = False
       return count  

