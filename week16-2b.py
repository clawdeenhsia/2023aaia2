class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        #for i in range (3):
        #counter = Counter(words[0]) & Counter(words[1]) & Counter(words[2])
        counter = Counter(words[0])
        for word in words:
            counter &= Counter(word)
        ans =[]
        for c in counter:
            for i in range(counter[c]):
                ans.append(c)
        return ans
