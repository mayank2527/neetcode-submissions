class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_counter = Counter(s1)

        i = 0
        j = len(s1) - 1

        while j < len(s2):
            if Counter(s2[i:j+1]) == s1_counter:
                return True
            
            i+=1
            j+=1
        
        return False


