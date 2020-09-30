# Linked-list 

+ [234. Palindrome Linked List](#https://leetcode.com/problems/palindrome-linked-list/)
+ [206. Reverse Linked List](#https://leetcode.com/problems/reverse-linked-list/)

## 234. Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow = reversed(slow)
        fast = head

        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next

        return True

def reversed(head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
```

## 206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
```
