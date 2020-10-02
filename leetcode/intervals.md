# Intervals 

+ [Merge Intervals](#merge-intervals)

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        intervals.sort(key=lambda interval: interval[0])
        merged = [intervals[0]]
        for interval in intervals:
            prev_interval = merged[-1]
            if interval[0] <= prev_interval[1]:
                prev_interval[1] = max(prev_interval[1], interval[1])
            else:
                merged.append(interval)
        return merged
```
