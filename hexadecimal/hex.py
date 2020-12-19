import sys
from string import ascii_uppercase


class Node:
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next


class HexNumber:
    def __init__(self, num):
        self.head = Node()
        self.lst = []
        for n in num[::-1]:
            if n not in ascii_uppercase and not n.isdigit():
                raise ValueError
            else:
                self.add_at_tail(n)

    def add_at_tail(self, val) -> None:
        new_node = Node(val)
        if len(self.lst) == 0:
            self.lst.append(new_node)
            self.head = new_node
            return
        lastnode = self.lst[len(self.lst) - 1]
        lastnode.next = new_node
        self.lst.append(new_node)

    def __str__(self):
        return ''.join(reversed(list(x.val for x in self.lst)))


class Solution:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.r = 0
        self.result = HexNumber('')

    def str_to_num(self, st):
        if st in ascii_uppercase:
            return ord(st) - ord('A') + 10
        else:
            return int(st)

    def num_to_str(self, num):
        if num > 9:
            return chr(ord('A') + num - 10)
        return str(num)

    def add(self):
        k1 = len(self.first.lst)
        k2 = len(self.second.lst)

        if k1 != k2:
            mx = max(self.first.lst, self.second.lst, key=len)
            mn = min(self.first.lst, self.second.lst, key=len)
        else:
            mx = self.first.lst
            mn = self.second.lst

        k = len(mn)
        for i in range(k):
            summ = self.str_to_num(mx[i].val) + self.str_to_num(mn[i].val)
            md = summ % 16
            if self.r != 0:
                self.result.add_at_tail(self.num_to_str(md + self.r))
            else:
                self.result.add_at_tail(self.num_to_str(md))
            self.r = summ // 16

        if k1 != k2:
            for nd in mx[k::]:
                self.result.add_at_tail(nd.val)
        if self.r != 0 and self.str_to_num(self.result.lst[-1].val) >= 15:
            self.result.add_at_tail(self.num_to_str(self.r))


if __name__ == '__main__':
    params = sys.argv
    sol = Solution(HexNumber(params[1]), HexNumber(params[2]))
    sol.add()
    print(sol.result)
