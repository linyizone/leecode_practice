class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        y = set()
        len1 = len(nums)
        for i in range(len1):
            if target-nums[i] in y:
                return [nums.index(target-nums[i]), i]
            y.add(nums[i])
        return None