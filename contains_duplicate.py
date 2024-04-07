class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        
        for num in nums:
            if num not in hset:
                hset.add(num)
            else:
                return True

        return False
