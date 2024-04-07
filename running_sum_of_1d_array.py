class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        for i in range(len(nums)):
            last_sum = 0

            if i != 0:
                last_sum = running_sum[i-1]

            running_sum.append(last_sum + nums[i])

        return running_sum