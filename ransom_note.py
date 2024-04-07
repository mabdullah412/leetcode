class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alph_count = 26
        freq_count = []

        for i in range(alph_count):
            freq_count.append(0)

        for ch in magazine:
            index = ord(ch) - 97
            freq_count[index] += 1
        
        for ch in ransomNote :
            index = ord(ch) - 97
            
            if freq_count[index] <= 0:
                return False

            freq_count[index] -= 1

        return True
