class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_counter = Counter(s1)

        i = 0
        j = len(s1) - 1

        s2_counter = Counter(s2[i:j])
        while j < len(s2):
            if s2[j] in s2_counter:
                s2_counter[s2[j]]+=1
            else:
                s2_counter[s2[j]] = 1
                    
            if s2_counter == s1_counter:
                return True
                
            if s2[i] in s2_counter:
                s2_counter[s2[i]]-=1
            else:
                del s2_counter[s2[i]]
            i+=1
            j+=1
            
        
        return False
