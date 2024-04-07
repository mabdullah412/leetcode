class Solution:
    def isValid(self, ch: str) -> bool:
        if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122 or 48 <= ord(ch) <= 57:
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        p1 = 0                  # start pointer
        p2 = len(s) - 1         # end pointer

        while p1 < p2:

            if not self.isValid(s[p1]):
                p1 += 1
                continue

            if not self.isValid(s[p2]):
                p2 -= 1
                continue

            if s[p1].lower() == s[p2].lower():
                p1 += 1
                p2 -= 1
            else:
                return False

        return True
    