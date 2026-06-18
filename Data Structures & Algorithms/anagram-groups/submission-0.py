class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        freq_dict = {}
        result_list = []

        for st in strs:
            freq_dict[st] = Counter(st)

            if len(result_list) == 0:
                result_list.append([st])
            else:
                group_found = False
                for result_groups in result_list:
                    if freq_dict[st] == freq_dict[result_groups[0]]:
                        result_groups.append(st)
                        group_found = True
                        break
                
                if not group_found:
                    result_list.append([st])
            
        return result_list

        