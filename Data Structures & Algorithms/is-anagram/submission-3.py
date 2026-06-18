class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return ''.join(sorted(s)) == ''.join(sorted(t))

        # char_set = []

        if len(s) != len(t):
            return False

        # l, r = 0,0

        # while l < len(s) and r < len(s):
        #     if s[l] == t[r]:
        #         l+=1
        #         r+=1
        #         while l<len(s) and s[l] in char_set:
        #             char_set.remove(s[l])
        #             l+=1
        #     else:
        #         char_set.append(t[r])
        #         r+=1

        # if len(char_set) == 0:
        #     return True
        # return False

        from collections import Counter

        s_counter = Counter(s)
        t_counter = Counter(t)

        for i in s_counter.keys():
            if s_counter[i] != t_counter[i]:
                return False
            
        return True


