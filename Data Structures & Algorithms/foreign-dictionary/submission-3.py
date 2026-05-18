from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for w in words for c in w}
        for i in range(n-1):
            a, b = words[i], words[i+1]
            nodata = True
            for j in range(min(len(a), len(b))):
                if a[j] == b[j]:
                    continue
                else:
                    if b[j] not in adj[a[j]]:
                        adj[a[j]].add(b[j])
                        indegree[b[j]] += 1
                    nodata = False
                    break
            if nodata and len(a) > len(b):
                return ""
        queue = deque([a for a in indegree if indegree[a] == 0])
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for child in adj[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        if len(ans) != len(indegree):
            return ""
        return ''.join(ans)

        
                