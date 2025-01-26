class Solution:
    def wordPattern(self, pattern: str, s: str) -> None:
        matching_pattern = {}
        split_words = s.split()
        unique_letters = set([letter for letter in pattern])
        unique_words = set(split_words)

        if len(unique_letters) != len(unique_words) or len(pattern) != len(split_words):
            return False

        for letter, word in zip(pattern, split_words):
            if letter not in matching_pattern:
                matching_pattern[letter] = word
            
            elif matching_pattern[letter] != word:
                return False
        return True
