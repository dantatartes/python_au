# Tree 

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
def maxDepth(self, root: TreeNode) -> int:
    depth = 0
    level = [root] if root else []
    while level:
        depth += 1
        queue = []
        for el in level:
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
        level = queue

    return depth
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    self.helper(root, res)
    return res

def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python
def __init__(self, root):
    self.stack = []
    while root:
        self.stack.append(root)
        root = root.left

def hasNext(self):
    return len(self.stack) > 0

def next(self):
    node = self.stack.pop()
    x = node.right
    while x:
        self.stack.append(x)
        x = x.left
    return node.val
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
def levelOrder(self, root):
    res = []
    self.dfs(root, 0, res)
    return res

def dfs(self, root, level, res):
    if not root:
        return
    if len(res) < level+1:
        res.append([])
    res[level].append(root.val)
    self.dfs(root.left, level+1, res)
    self.dfs(root.right, level+1, res)
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
def kthSmallest(self, root, k):
    for val in self.inorder(root):
        if k == 1:
            return val
        else:
            k -= 1

def inorder(self, root):
    if root is not None:
        for val in self.inorder(root.left):
            yield val
        yield root.val
        for val in self.inorder(root.right):
            yield val
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
def isValidBST(self, root):
    output = []
    self.in_order(root, output)

    for i in range(1, len(output)):
        if output[i-1] >= output[i]:
            return False

    return True

def in_order(self, root, output):
    if root is None:
        return

    self.in_order(root.left, output)
    output.append(root.val)
    self.in_order(root.right, output)
```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True
    return self.check(root.left, root.right)

def check(self, left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    a = self.check(left.left, right.right)
    b = self.check(left.right, right.left)
    return a and b
```
