# String 

+ [To Lower Case](#to-lower-case)

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(char)+32) if 65 <= ord(char) <= 90 else char for char in str])
```
