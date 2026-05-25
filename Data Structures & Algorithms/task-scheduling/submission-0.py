from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = max(count.values())
        max_count = list(count.values()).count(max_freq)

        intervals = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), intervals)
        