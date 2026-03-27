def numSteps(self, s: str) -> int:
    carry = False
    steps = 0
    
    for bit in s[:0:-1]:
        if carry:
            if bit == '0':
                bit = '1'
                carry = False
            else:
                bit = '0'
        if bit == '1':
            steps += 1
            carry = True
        steps += 1
    
    if carry:
        steps += 1
    
    return steps