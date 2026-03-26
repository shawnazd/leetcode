class Solution:
    def addBinary(self, binary1: str, binary2: str) -> str:
        num1 = int(binary1, 2)
        num2 = int(binary2, 2)
        total = num1 + num2
        result_binary = bin(total)[2:]
        return result_binary