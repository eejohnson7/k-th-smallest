'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k): 
        stack = []
        current = root
        count = 0
    
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
    
            current = stack.pop()
            count += 1
            if count == k:
                return current.data
            current = current.right

        return -1
        