from helper import visualize_tree
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.nof_nodes = 0
    
    def insert_recursive(self,value):
        pass
   
    def insert_iterative(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            head = self.root
            while head:
                if value < head.val:
                    tail = head.left
                    if not tail:
                        head.left = new_node
                        break
                    
                else: # here value >= head.val
                    tail = head.right
                    if not tail:
                        head.right = new_node
                        break
                head = tail
    
    def find_min_value(self, node):
        head = node
        while head.left:
            head = head.left
        return head.val
    def remove_recursive(self,value):
        self._remove_recursive(self.root, value)
    
    def _remove_recursive(self, root, value):
        if not root:
            return
        if root.val < value:
            root.left = self._remove_recursive(root.left, value)
        elif root.val > value:
            root.right = self._remove_recursive(root.right, value)
        else: # base case
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # both child present, replace by successor
            # inorder_successsor_val = self.find_min_value(head.left)
            root.val = find_min_value(root.right)
            root.right = self._remove_recursive(root.right, root.val)
        return root

    def remove_iterative(self, value):
        root = self.root
        self._remove_iterative(root, value)

    def _remove_iterative(root, value):
        pass

if __name__=="__main__":
    array1 = [40, 20, 30, 60,50,10]
    bst1 = BST()
    for el in array1:
        bst1.insert_iterative(el)
    visualize_tree(bst1.root, prefix="bst1")
    array2 = [50, 40, 30,20,70]
    bst2 = BST()
    for el in array2:
        bst2.insert_iterative(el)
    visualize_tree(bst2.root, prefix="bst2")
        
if __name__ == "__main1__":
    my_bst = BST()
    # Create a sample binary search tree
    # array = [10, 15, 7, 13, 25, 9,6]
    # random.shuffle(array)
    array = [25, 10, 6, 15, 13, 9, 7]

    #           25
    #          /
    #         10
    #      /      \
    #     6        15
    #      \       /
    #       9     13
    #        \
    #         7

    for val in array:
        my_bst.insert_iterative(val)
    visualize_tree(my_bst.root, prefix="binary_search_tree")
    
    # Add more values
    #                 25
    #             /       \
    #           10         26
    #       /         \
    #      6          15
    #       \       /    \
    #        9     13     23
    #         \            \
    #          7            24 

    my_bst.insert_iterative(23)
    my_bst.insert_iterative(26)
    my_bst.insert_iterative(24)
    visualize_tree(my_bst.root)

    # Remove 15
    #                 25
    #             /       \
    #           10         26
    #       /         \
    #      6          23
    #       \       /    \
    #        9     13     24
    #         \            
    #          7             
    my_bst.remove_recursive(15)
    visualize_tree(my_bst.root, prefix="binary_search_tree")

    #                 25
    #             /       \
    #           10         26
    #       /         \
    #      6          23
    #       \       /    \
    #        9     13     24
    #         \      \       
    #          7      16       
    #                /  \
    #               15  17

    my_bst.insert_iterative(16)
    my_bst.insert_iterative(17)
    my_bst.insert_iterative(15)
    visualize_tree(my_bst.root, prefix="binary_search_tree")


    #                 25
    #             /       \
    #           13         26
    #       /         \
    #      6           23
    #       \        /    \
    #        9      16     24
    #         \    /  \       
    #          7  15    17
    my_bst.remove_recursive(10)
    visualize_tree(my_bst.root, prefix="binary_search_tree")