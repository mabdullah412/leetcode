class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        table = {}
        
        for i in range(len(arr)):
            if 2*arr[i] in table:
                return True
            elif arr[i]/2 in table:
                return True
            else:
                table[arr[i]] = i
                
        return False