# Array 

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    count = max_count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0

    return max(count, max_count)
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    flat_list = []
    matrix = []

    for sublist in nums:
        for item in sublist:
            flat_list.append(item)

    if len(flat_list) != r * c:
        return nums
    else:
        for i in range(0,len(flat_list),c):
            matrix.append(flat_list[i:i+c])
        return matrix
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    m = len(M)
    if m < 1:
        return M
    n = len(M[0])

    s = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            c = 1
            v = M[i][j]

            for k in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
                x = i + k[0]
                y = j + k[1]

                if x < 0 or x >= m:
                    continue
                if y < 0 or y >= n:
                    continue

                c += 1
                v += M[x][y]

            s[i][j] = v // c
    return s
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    translation = {0:1, 1:0}
    return [list(map(lambda x: translation[x], row[::-1])) for row in A]
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
def transpose(self, A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
def moveZeroes(self, nums: list) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != 0:
            slow += 1
```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
def sortedSquares(self, A: List[int]) -> List[int]:
    result = [None for _ in A]
    left, right = 0, len(A) - 1
    for index in range(len(A)-1, -1, -1):
        if abs(A[left]) > abs(A[right]):
            result[index] = A[left] ** 2
            left += 1
        else:
            result[index] = A[right] ** 2
            right -= 1
    return result
```
