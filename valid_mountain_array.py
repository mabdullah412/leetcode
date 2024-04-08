class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        prev = arr[1]
        increasing = False
        switched = False        # to check if changed from increasing to decreasing or vice versa
        
        if arr[0] < arr[1]:
            increasing = True
        elif arr[0] > arr[1]: 
            increasing = False
        else:
            return False
        
        for i in range(2, len(arr)):
            if arr[i] > prev:
                if not increasing:
                    if switched:
                        return False
                    else:
                        switched = True
                        increasing = True
                        return False
                prev = arr[i]
                    
            elif arr[i] < prev:
                if increasing:
                    if switched:
                        return False
                    else:
                        switched = True
                        increasing = False
                prev = arr[i]
                
            else:
                return False
                
        if switched == False:
            return False
        else:
            return True
        