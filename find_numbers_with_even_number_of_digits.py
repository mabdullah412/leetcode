class Solution:
    def hasEvenDigits(self, num) -> bool:
        digits = 0

        while num > 9:
            num = int(num / 10)
            digits += 1
        digits += 1
        
        if digits % 2 == 0:
            return True
        else:
            return False
        
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for num in nums:
            if self.hasEvenDigits(num):
                count += 1

        return count