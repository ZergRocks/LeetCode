# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        average_list = []
        node_queue = [root]
        while True:
            level_nodes = [node for node in node_queue]
            node_queue = []
            total = 0
            count = 0
            for node in level_nodes:
                if node.val is not None:
                    total += node.val
                    count += 1
                if node.left is not None:
                    node_queue.append(node.left)
                if node.right is not None:
                    node_queue.append(node.right)
            if count != 0:
                average_list.append(total/count)
            else:
                return average_list