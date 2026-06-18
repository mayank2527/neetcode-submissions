class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1

        while l<=r:
            if not (96<ord(s[l].lower())<123 or 46<ord(s[l].lower())<58):
                l+=1
                continue
            
            if not (96<ord(s[r].lower())<123 or 46<ord(s[r].lower())<58):
                r-=1
                continue
            
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        
        return True