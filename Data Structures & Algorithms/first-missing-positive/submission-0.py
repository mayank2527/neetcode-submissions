class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_num = float('inf')
        set_nums = set()

        for num in nums:
            if num>0:
                min_num = min(num,min_num)
                set_nums.add(num)

        if min_num > 1:
            return 1
        
        continous_max = min_num+1
        while continous_max in set_nums:
            continous_max = continous_max+1
        
        return continous_max
