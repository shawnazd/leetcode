class Solution:
    def addDigits(self, num: int) -> int:

        result = 0

        while num > 9:
            add_digit = 0
            while num > 0:
                digit = num % 10
                add_digit += digit
                num //= 10
            num = add_digit
            
        return num 