class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        sign = 1

        for digit in str(n):
            total += sign * int(digit)
            sign *= -1

        return total