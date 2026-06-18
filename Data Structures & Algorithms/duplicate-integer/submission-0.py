class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit_set = set()

        for num in nums:
            if num in visit_set:
                return True
            visit_set.add(num)
        
        return False
