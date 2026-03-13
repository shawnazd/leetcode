class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_frequency = {}
        total_length = 0
        
        for ch in chars:
            if ch in char_frequency:
                char_frequency[ch] += 1
            else:
                char_frequency[ch] = 1
        
        for word in words:
            word_frequency = {}
            for ch in word:
                if ch in word_frequency:
                    word_frequency[ch] += 1
                else:
                    word_frequency[ch] = 1
            
            can_form_word = True
            for ch in word_frequency:
                if ch not in char_frequency or word_frequency[ch] > char_frequency[ch]:
                    can_form_word = False
                    break
            
            if can_form_word:
                total_length += len(word)
        
        return total_length