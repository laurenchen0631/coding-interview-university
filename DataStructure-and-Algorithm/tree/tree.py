class BinaryTree:
    class TreeNode:
        def __init__(self, data, parent=None, left=None, right=None):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right

        @property
        def left(self):
            return self.__left

        @left.setter
        def left(self, node):
            if node is None:
                self.__left = node
            elif type(node) is TreeNode:
                node.parent = self
                self.__left = node
            else:
                self.__left = TreeNode(node, self)

        @property
        def right(self):
            return self.right

        @right.setter
        def right(self, node):
            if node is None:
                self.__right = node
            elif type(node) is TreeNode:
                node.parent = self
                self.__right = node
            else:
                self.__left = TreeNode(node, self)

    def __init__(self, data):
        self.__root = TreeNode(data)

    def height(self):
        return self.__height(self.__root)

    def __height(self, root):
        if tree is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def size(self):
        return self.__size(self.__root)

    def __size(self, root):
        if tree is None:
            return 0
        return 1 + self.size(root.left) + self.size(root.right)

    '''
            A
          /    \
         B      C
        / \    /  \
       D   E  F    G
    '''

    # depth first: ABDECFG
    def perorder_traversal(self, root):
        if root is None:
            return

        print(root.data)
        self.perorder_traversal(root.left)
        self.perorder_traversal(root.right)

    # depth first: DEBFGCA
    def postorder_traversal(self, root):
        if root is None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.data)

    # DBEAFCG
    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.data)
        self.inorder_traversal(root.right)

    # breadth first search
    def levelorder_traversal(self, root):
        next_level = Queue()
        while next_level:
            node = next_level.pop(0)
            print(node.data)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
