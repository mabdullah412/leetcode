class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alph_count = 26
        freq_count = []

        for i in range(alph_count):
            freq_count.append(0)

        for ch in s:
            index = ord(ch) - 97
            freq_count[index] += 1
        
        for ch in t:
            index = ord(ch) - 97
            
            if freq_count[index] <= 0:
                return ch

            freq_count[index] -= 1
