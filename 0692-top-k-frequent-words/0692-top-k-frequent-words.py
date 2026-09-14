class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        words_sorted = sorted(freq, key=lambda word: (-freq[word], word))

        return words_sorted[:k]