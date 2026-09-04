class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        current = 1
        result = 1

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                current += 1
            else:
                current = 1
            result = max(result, current)

        return result