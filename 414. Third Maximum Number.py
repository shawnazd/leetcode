from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        frst = scnd = thrd = None
        
        for n in nums:
            if n in [frst, scnd, thrd]:
                continue
            if frst is None or n > frst:
                frst, scnd, thrd = n, frst, scnd
            elif scnd is None or n > scnd:
                scnd, thrd = n, scnd
            elif thrd is None or n > thrd:
                thrd = n

        return thrd if thrd is not None else frst
   
