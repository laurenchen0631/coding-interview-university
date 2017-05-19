from collections import deque


class BinarySearchTree:

    class Node:
        def __init__(self, val, parent=None, left=None, right=None):
            self.val = val
            self.parent = parent
            self.left = left
            self.right = right

        @property
        def val(self):
            return self.__val

        @val.setter
        def val(self, val):
            if val is not None:
                self.__val = val
            else:
                raise TypeError("value must be combarable object")

        @property
        def left(self):
            return self.__left

        @left.setter
        def left(self, val):
            if val is None:
                self.__left = None
            elif type(val) is BinarySearchTree.Node:
                self.__left = val
            else:
                node = BinarySearchTree.Node(val, self)
                self.__left = node

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, val):
            if val is None:
                self.__right = None
            elif type(val) is BinarySearchTree.Node:
                self.__right = val
            else:
                node = BinarySearchTree.Node(val, self)
                self.__right = node

    @staticmethod
    def is_binary_search_tree(root):
        if root is None:
            return False
        nodes = []
        self.__inorder_traverse(root, nodes)
        for i in range(len(nodes)-1):
            if nodes[i+1].val < node[i].val:
                return False
        return True

    def __init__(self):
        self.__root = None

    def __len__(self):
        return self.get_node_count()

    def __del__(self):
        self.delete_tree()

    def __contains__(self, val):
        return self.is_in_tree(val)

    def __iter__(self):
        return self.__next(self.__root)

    def __next(self, root):
        if root:
            yield from self.__next(root.left)
            yield root.val
            yield from self.__next(root.right)

    # insert value into tree
    def insert(self, val):
        if self.__root:
            parent = self.__root
            while True:
                if val < parent.val:
                    if parent.left:
                        parent = parent.left
                    else:
                        parent.left = val
                        return
                elif parent.val < val:
                    if parent.right:
                        parent = parent.right
                    else:
                        parent.right = val
                        return
                else:
                    return
        else:
            self.__root = BinarySearchTree.Node(val)

    # get count of values stored
    def get_node_count(self):
        if not self.__root:
            return 0

        queue = deque([self.__root])
        count = 0
        while queue:
            count += 1
            node = queue.pop()
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        return count

    # prints the values in the tree, from min to max
    def print_values(self):
        values = []
        self.__inorder_traverse(self.__root, values)
        print(" ".join(values))

    def __inorder_traverse(self, root, arr):
        if root is None:
            return
        self.__inorder_traverse(root.left, arr)
        arr.append(str(root.val))
        self.__inorder_traverse(root.right, arr)

    def delete_tree(self):
        self.__root = None

    # returns true if given value exists in the tree
    def is_in_tree(self, val):
        return self.__get_node(val) is not None

    def __get_node(self, val):
        root = self.__root
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None

    # returns the height in nodes (single node's height is 1)
    def get_height(self):
        return self.__height(self.__root)

    def __height(self, root):
        if root is None:
            return 0
        return 1 + max(self.__height(root.left), self.__height(root.right))

    # returns the minimum value stored in the tree
    def get_min(self):
        if self.__root is None:
            return None
        return self.__get_min(self.__root).val

    def __get_min(self, root):
        while root.left:
            root = root.left
        return root

    # returns the maximum value stored in the tree
    def get_max(self):
        if self.__root is None:
            return None
        parent = self.__root
        while parent.right:
            parent = parent.right
        return parent.val

    def delete_value(self, val):
        root = self.__get_node(val)
        if root is None:
            return

        # node has 2 children
        if root.left and root.right:
            successor = self.__get_min(root.right)
            root.val = successor.val
            # set root to sucessor and delete by no child or one child process
            root = successor

        # node doesn't have any child
        if not root.left and not root.right:
            if root.parent is None:
                self.__root = None
            elif root.parent.left is root:
                root.parent.left = None
            else:
                root.parent.right = None
        # node have one child
        else:
            child = root.left if root.left else root.right
            child.parent = root.parent
            if root.parent is None:
                self.__root = child
            elif root.parent.left is root:
                root.parent.left = child
            else:
                root.parent.right = child

    # returns next-highest value in tree after given value, -1 if none
    def get_successor(self, val):
        if not self.__root:
            return None

        # go to the nearest ancestor where given value is in left subtree
        successor = None
        root = self.__root
        while root:
            if val < root.val:
                successor = root
                root = root.left
            # if we find the node of the val, we search its right substree
            else:
                root = root.right
        if successor is None:
            return None
        else:
            return successor.val
