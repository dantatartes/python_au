# Intervals 

+ [Merge Intervals](#merge-intervals)
+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Insert Interval](#insert-interval)

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
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

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    num_remove = 0
    if not intervals:
        return num_remove
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][0]
    for interval in intervals:
        if interval[0] < end:
            num_remove += 1
        else:
            end = interval[1]
    return num_remove
```

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    l, r = [], []
    for interval in intervals:
        if interval[1] < newInterval[0]:
            l.append(interval)
        elif interval[0] > newInterval[1]:
            r.append(interval)
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
    return l + [[newInterval[0], newInterval[1]]] + r
```

