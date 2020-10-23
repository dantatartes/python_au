# String 

+ [To Lower Case](#to-lower-case)
+ [Valid Anagram](#valid-anagram)

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(char)+32) if 65 <= ord(char) <= 90 else char for char in str])
```

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])
```
