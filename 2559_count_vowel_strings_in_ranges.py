#2025-10-16 time: 3:23
class Solution(object):
    def vowelStrings(self, words, queries):
        prefix = [0] * (len(words) + 1)
        
        for i, word in enumerate(words):
            is_vowel_word = word[0] in "aeiou" and word[-1] in "aeiou"
            prefix[i + 1] = prefix[i] + is_vowel_word
        
        result = []
        for x, y in queries:
            result.append(prefix[y + 1] - prefix[x])
        
        return result
