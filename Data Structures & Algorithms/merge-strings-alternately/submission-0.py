class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        new_str = ""
        len_word1 = len(word1)
        len_word2 = len(word2)

        while i < len_word1 and j < len_word2:
            new_str+= word1[i]+word2[j]
            i+=1
            j+=1
        
        if i==len_word1:
            return new_str+word2[j:]
        else:
            return new_str+word1[i:]

        