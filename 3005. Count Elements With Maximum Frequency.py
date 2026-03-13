class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freq = {}
        
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        max_freq = 0
        
        for i in freq:
            if freq[i] > max_freq:
                max_freq = freq[i]
            
        total = 0
        
        for i in freq:
            if freq[i] == max_freq:
                total += freq[i]
            
        return total