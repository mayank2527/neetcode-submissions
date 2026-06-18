class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter

        counter = Counter(nums)

        result = []
        for item, freq in counter.items():
            if freq >= len(nums)//3+1:
                result.append(item)

        return result