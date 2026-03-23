class Solution:
    def minimumRounds(self, tasks):
        count = {}
        for t in tasks:
            if t in count:
                count[t] += 1
            else:
                count[t] = 1
        
        rounds = 0
        
        for val in count.values():
            if val == 1:
                return -1
            elif val == 2:
                rounds += 1
            else:
                div = val // 3
                mod = val % 3
                if mod != 0:
                    div += 1
                rounds += div
        
        return rounds