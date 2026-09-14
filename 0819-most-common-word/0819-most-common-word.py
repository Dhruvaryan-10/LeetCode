class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph = paragraph.lower()
        for p in "?.,'!;":
            paragraph = paragraph.replace(p," ")
        freq = {}
        for word in paragraph.split():
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1
        best_word = ""
        best_count = 0
        for word, count in freq.items():
            if count > best_count:
                best_word = word
                best_count = count
        return best_word