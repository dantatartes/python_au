# String 

+ [To Lower Case](#to-lower-case)
+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
def toLowerCase(self, str: str) -> str:
    return ''.join([chr(ord(char)+32) if 65 <= ord(char) <= 90 else char for char in str])
```

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
def isAnagram(self, s: str, t: str) -> bool:
    return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
def reverseString(self, s):
    low, high  = 0, len(s)-1
    while low < high:

        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1

    return s
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
def reverseVowels(self, s: str) -> str:
    st, en = 0, len(s)-1
    ls = list(s)
    vow = set("aeiouAEIOU")
    while st < en:
        if ls[st] in vow and ls[en] in vow:
            ls[st], ls[en] = ls[en], ls[st]
            st += 1
            en -= 1
        if ls[st] not in vow:
            st += 1
        if ls[en] not in vow:
            en -= 1


    return "".join(ls)
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
def reverseWords(self, s: str) -> str:
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i][::-1]
    return " ".join(s)
```
