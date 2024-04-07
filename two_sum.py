class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i in range(len(nums)):

            if nums[i] in table:                # check if this num can be added to some other existing num to make target
                return [i, table[nums[i]]]

            table[target - nums[i]] = i         # key: diff between target and current num, # key: index
            