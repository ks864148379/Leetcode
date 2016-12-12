# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        ans = []
        d = [root]
        c = 1
        r = 0
        st = 0
        while st < len(d):
            if d[st].left != None:
                d.append(d[st].left)
                r += 1
            if d[st].right != None:
                d.append(d[st].right)
                r += 1
            c -= 1
            if c == 0:
                ans.append(d[st].val)
                c = r
                r = 0
            st += 1
        return ans
