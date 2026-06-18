class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter

        counter = Counter(nums)
        max_element = None
        max_freq = 0
        for i in counter.keys():
            if counter[i] > max_freq:
                max_element=i
                max_freq=counter[i]

        return max_element