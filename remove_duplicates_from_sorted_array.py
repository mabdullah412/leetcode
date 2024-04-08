class Solution:
    def removeDuplicates(self, nums) -> int:
        p1 = 0
        p2 = 1
        count = 0
        hset = set()        # extra mem

        while p1 < len(nums) and p2 < len(nums):
            
            if nums[p1] not in hset:        # if first num not in set, add and move both forward
                hset.add(nums[p1])
                count += 1
                p1 += 1
                p2 += 1
            
            else:                           # if in set, check for second num, 
                if nums[p2] not in hset:    # if not in set, add and swap with first num, move both forward
                    hset.add(nums[p2])
                    count += 1
                    temp = nums[p1]
                    nums[p1] = nums[p2]
                    nums[p2] = temp
                    p1 += 1
                    p2 += 1
                
                else:                       # if in set, move second forward only
                    p2 += 1

        if nums[p1] not in hset:
            hset.add(nums[p1])
            count += 1

        return count