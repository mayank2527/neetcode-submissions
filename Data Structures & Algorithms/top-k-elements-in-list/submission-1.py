class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        nums_counter = Counter(nums)

        max_freq = max(nums_counter.values())

        freq_list  = [None]*(max_freq+1)

        for num, freq in nums_counter.items():
            if freq_list[freq] is None:
                freq_list[freq] = []
            freq_list[freq].append(num)

        result_list = []
        for i in freq_list[::-1]:
            if i:
                result_list.extend(i)
        
        return result_list[:k]