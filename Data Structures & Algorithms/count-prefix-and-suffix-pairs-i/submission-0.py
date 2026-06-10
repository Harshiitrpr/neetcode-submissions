class TrieNode:
    def __init__(self) -> None:
        # self.value = 0
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def add(self, word) -> int:
        curr = self.root
        res = 0
        for c1, c2 in zip(word, reversed(word)):
            if (c1, c2) not in curr.children:
                curr.children[(c1, c2)] = TrieNode()
            curr = curr.children[(c1, c2)]
            res += curr.count
        curr.count += 1
        return res
    

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        ans = 0
        for word in words:
            ans += trie.add(word)
        return ans
        