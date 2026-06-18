class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        perfix_multipy_list = [nums[0]]
        sufix_multipy_list = [0]*len(nums)

        for i in range(1,len(nums)):
            perfix_multipy_list.append(perfix_multipy_list[i-1]*nums[i])
        
        sufix_multipy_list[-1] = nums[-1]
        for i in range(len(nums)-2,0,-1):
            sufix_multipy_list[i] = nums[i] * sufix_multipy_list[i+1]

            # sufix_multipy_list.insert(0,sufix_multipy_list[0]*nums[i-1])

        result_list = []

        for i in range(0, len(nums)):
            if i==0:
                result_list.append(sufix_multipy_list[i+1])
            elif i==len(nums)-1:
                result_list.append(perfix_multipy_list[i-1])
            else:
                result_list.append(perfix_multipy_list[i-1] * sufix_multipy_list[i+1])

        return result_list
        