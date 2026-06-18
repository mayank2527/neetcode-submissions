class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_str = strs[0]

        for st in strs[1:]:
            i,j=0,0
            new_prefix = ''
            while i <len(prefix_str) and j<len(st):
                if prefix_str[i] == st[j]:
                    new_prefix+=prefix_str[i]
                    i+=1
                    j+=1
                else:
                    break

            prefix_str=new_prefix

        return prefix_str
