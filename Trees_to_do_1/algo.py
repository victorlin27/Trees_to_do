class Node:
    def __init__(self,val):
        self.value= val
        self.left = None
        self.right =None

class BST:
    def __init__(self):
        self.root = None

# create a method tot ake in the value of a node. Then create that node and detemrin what way tos end it on you BST with the rule less than goes to left greater than goes to right and equal goes to right

    def add(self,val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return self
        runner = self.root
        while runner != None:
            if new_node.value >runner.value :
                if runner.right == None:
                    runner.right = new_node
                    return self
                else:
                    runner = runner.right
            elif new_node.value< runner.value:
                if runner.left ==None:
                    runner.left = new_node
                    return self
                else:
                    runner = runner.left
            else:
                if runner.right == None:
                    runner.right = new_node
                    return self
                else:
                    runner = runner.right

    def contains(self, val):
            return self._contains(val, self.root)
        
    def _contains(self, val, cur_node):
            if cur_node is None:
                return False
            elif val == cur_node.val:
                return True
            elif val < cur_node.val:
                return self._contains(val, cur_node.left)
            else:
                return self._contains(val, cur_node.right)
            
    def min(self):
        if self.root is None:
            return None
        else:
            return self._min(self.root)
        
    def _min(self, cur_node):
        if cur_node.left is None:
            return cur_node.val
        else:
            return self._min(cur_node.left)
        
    def max(self):
        if self.root is None:
            return None
        else:
            return self._max(self.root)
        
    def _max(self, cur_node):
        if cur_node.right is None:
            return cur_node.val
        else:
            return self._max(cur_node.right)