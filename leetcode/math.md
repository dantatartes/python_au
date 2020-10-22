# Math 

+ [Fizz Buzz](#fizz-buzz)

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        m = []
        for i in range(1, n+1):
            if i % 15 == 0:
                m.append("FizzBuzz")
            elif i % 3 == 0:
                m.append("Fizz")
            elif i % 5 == 0:
                m.append("Buzz")
            else:
                m.append(str(i))
        return m
```
