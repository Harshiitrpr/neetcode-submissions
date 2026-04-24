class Solution:
    delimiter = chr(200)
    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        if n < 1:
            return ""
        ans = ""
        for i in range(n):
            ans += strs[i] + self.delimiter
        return ans


    def decode(self, s: str) -> List[str]:
        l = s.split(self.delimiter)
        l.pop()
        return l
