class Solution:
    delimiter = '#'
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + self.delimiter + s
        return ans

    def decode(self, s: str) -> List[str]:
        l = []
        pending = 0
        length = ""
        tmp = ""
        for i in range(len(s)):
            if pending == 0:
                if s[i] == self.delimiter:
                    pending = int(length)
                    length = ""
                    if pending == 0:
                        l.append("")
                else:
                    length += s[i]
            else:
                tmp += s[i]
                pending -= 1
                if pending == 0:
                    l.append(tmp)
                    tmp = ""
        return l


