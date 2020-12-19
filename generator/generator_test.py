import unittest
from generator.generate_md import *


class TestMdSource(unittest.TestCase):

    def test_lnk(self):
        md = MdSource(*read_txt('in.py'))
        expect_lnk = '+ [Invert Binary Tree](#invert-binary-tree)'

        self.assertEqual(md.get_md_link(), expect_lnk)

    def test_title(self):
        md = MdSource(*read_txt('in.py'))
        expect_title = '## Invert Binary Tree'
        self.assertEqual(md.get_md_title(), expect_title)

    def test_code(self):
        md = MdSource(*read_txt('in.py'))
        expect_code = """```python\ndef invert(root):\n    if not root:\n        return\n    root.left, root.right""" + \
                      """ = root.right, root.left\n    invert(root.left)\n    invert(root.right)\n""" + \
                      """invert(root)\nreturn root\n```\n"""
        self.assertEqual(md.get_md_code(), expect_code)

    def test_task(self):
        md = MdSource(*read_txt('in.py'))
        expect_task = """## Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
```python
def invert(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)
invert(root)
return root
```\n\n"""
        self.assertEqual(md.get_md_task(), expect_task)


class TestWriting(unittest.TestCase):
    def test_write_to_file(self):
        expect_data = """# TREE
+ [Invert Binary Tree](#invert-binary-tree)
<!---->
## Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
```python
def invert(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)
invert(root)
return root
```
"""
        md = MdSource(*read_txt('in.py'))
        s = read_md('tree.md')
        s = prepare_data_to_write(md, s)
        write_to_file('tree.md', s)

        with open('tree.md') as f:
            data = f.read()
        self.assertEqual(data, expect_data)