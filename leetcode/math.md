# Math 

+ [Fizz Buzz](#fizz-buzz)
+ [Reverse Integer](#reverse-integer)
+ [Sqrt(x)](#sqrt(x))

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

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1,-1][x < 0]
        x_rev = sign * int(str(abs(x))[::-1])
        return x_rev if -(2**31)-1 < x_rev < 2**31 else 0
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid > x:
                hi = mid - 1
            elif mid * mid < x:
                lo = mid + 1
            else:
                return mid
        return hi
```
