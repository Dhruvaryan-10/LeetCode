class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        chars = sorted(freq, key =freq.get, reverse ='true')
        result = []
        for ch in chars:
            result.append(ch*freq[ch])
        return "".join(result)