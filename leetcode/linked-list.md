# Linked-list 

+ [Reverse Linked List](#reverse-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle](#linked-list-cycle)
+ [Linked List Cycle II](#linked-list-cycle-ii)

## Reverse Linked List

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

## Palindrome Linked List

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

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        curr_A, curr_B = headA, headB
        while curr_A != curr_B:
            if not curr_A:
                curr_A = headB
            else:
                curr_A = curr_A.next

            if not curr_B:
                curr_B = headA
            else:
                curr_B = curr_B.next

        return curr_A

```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow, fast, have_cycle = head, head.next, False
        while slow:
            if not fast or not fast.next:
                return
            elif slow == fast and not have_cycle:
                slow, fast, have_cycle = head, fast.next, True
            if slow == fast and have_cycle:
                return slow
            if have_cycle:
                fast = fast.next
            else:
                fast = fast.next.next
            slow = slow.next
```
