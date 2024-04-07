class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alph_count = 26
        freq_count = []     # store frequency of each letter

        for i in range(alph_count):     # add zeroes for each letter
            freq_count.append(0)

        for ch in s:                        # append 1 frequency at each letter index
            index = ord(ch) - 97
            freq_count[index] += 1
        
        for ch in t:                        # decrease 1 frequency for each letter
            index = ord(ch) - 97
            
            if freq_count[index] <= 0:      # if decreasing more times than occured, return False
                return False

            freq_count[index] -= 1

        for count in freq_count:            # make sure all are back to zero in the end
            if count > 0:
                return False

        return True
