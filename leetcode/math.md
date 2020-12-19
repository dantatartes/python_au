# Math 

+ [Fizz Buzz](#fizz-buzz)
+ [Reverse Integer](#reverse-integer)
+ [Sqrt(x)](#sqrt(x))
+ [Palindrome Number](#palindrome-number)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
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
def reverse(self, x: int) -> int:
    sign = [1,-1][x < 0]
    x_rev = sign * int(str(abs(x))[::-1])
    return x_rev if -(2**31)-1 < x_rev < 2**31 else 0
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
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

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x: int) -> bool:
    orig = x
    back_x = 0
    while x > 0:
        back_x = (back_x * 10) + (x % 10)
        x = x // 10
    return orig == back_x
```

## Base 7

https://leetcode.com/problems/base-7/

```python
def convertToBase7(self, num: int) -> str:
    if num == 0:
        return "0"

    based_num = ""

    if num < 0:
        is_negative = True
    else:
        is_negative = False

    num = abs(num)

    while num:
        carry = num % 7
        based_num = str(carry) + based_num
        num //= 7

    if is_negative:
        return f"-{based_num}"

    return based_num
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N: int) -> int:
    a, b = 0, 1
    for i in range(N):
        a, b = b, a + b
    return a
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
def largestPerimeter(self, A: List[int]) -> int:
    A.sort(reverse=True)
    n = len(A)
    for i in range(n-2):
        if A[i] < A[i+1] + A[i+2]:
            return  A[i] + A[i+1] + A[i+2]
    return 0
```
