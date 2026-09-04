class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        if nums.count(0) > 1:
            pass
        else:
            prod = 1
            index = -1
            for i,n in enumerate(nums):
                if n == 0:
                    index = i
                else:
                    prod *= n
            if index == -1:
                for i in range(len(nums)):
                    result[i] = prod // nums[i]
            else:
                result[index] = prod
        return result