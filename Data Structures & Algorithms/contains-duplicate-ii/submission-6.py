class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_set = set()
        i = 0 

        if len(nums)==1:
            return False

        for i in range(0,k+1):
            if nums[i] not in num_set:
                num_set.add(nums[i])
            else:
                return True

        i=1
        j=k+1

        while(j<len(nums)):
            num_set.remove(nums[i-1])
            if nums[j] in num_set:
                return True
            
            num_set.add(nums[j])            
            i+=1
            j+=1
        
        return False
