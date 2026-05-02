class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        tuples = [[position[i], speed[i]] for i in range(n)]
        tuples.sort()
        time = [(target - tuples[i][0])/ tuples[i][1] for i in range(n)]
        ans = 1
        for i in range(n-2, -1, -1):
            if time[i] <= time[i+1]:
                time[i] = time[i+1]
                continue
            else:
                ans += 1
        return ans
