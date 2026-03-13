class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = {}
        for c in magazine:
            if c in letter_count:
                letter_count[c] += 1
            else:
                letter_count[c] = 1

        for c in ransomNote:
            if c not in letter_count or letter_count[c] == 0:
                return False
            letter_count[c] -= 1

        return True