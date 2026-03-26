class Solution:
    def countDigits(self, num: int) -> int:

        n = num
        ans = 0

        while n > 0:
            digit = n % 10
            if num % digit == 0:
                ans += 1
            n //= 10

        return ans