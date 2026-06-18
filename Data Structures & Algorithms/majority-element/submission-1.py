class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # from collections import Counter

        # counter = Counter(nums)
        # max_element = None
        # max_freq = 0
        # for i in counter.keys():
        #     if counter[i] > max_freq:
        #         max_element=i
        #         max_freq=counter[i]

        # return max_element

        max_value, freq = nums[0],1

        for i in nums[1:]:
            if i == max_value:
                freq+=1
            elif freq==0:
                max_value, freq = i,1
            else:
                freq-=1

        return max_value




