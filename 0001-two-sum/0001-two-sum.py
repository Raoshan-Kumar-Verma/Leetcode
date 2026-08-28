class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Approach
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return
        temp = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in temp:
                return [temp[diff], i]
            temp[n] = i
        return 