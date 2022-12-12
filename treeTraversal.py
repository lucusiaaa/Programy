class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def preorder(self):
        global returned
        returned_local = []
        self._preorder(returned_local)
        returned = returned_local
        return returned

    def _preorder(self, returned):
        returned.append(self.value)
        if self.left_child is not None:
            self.left_child._preorder(returned)
        if self.right_child is not None:
            self.right_child._preorder(returned)

    def inorder(self):
        global returned
        returned_local = []
        self._inorder(returned_local)
        returned = returned_local
        return returned

    def _inorder(self, returned):
        if self.left_child is not None:
            self.left_child._inorder(returned)
        returned.append(self.value)
        if self.right_child is not None:
            self.right_child._inorder(returned)

    def postorder(self):
        global returned
        returned_local = []
        self._postorder(returned_local)
        returned = returned_local
        return returned

    def _postorder(self, returned):
        if self.left_child is not None:
            self.left_child._postorder(returned)
        if self.right_child is not None:
            self.right_child._postorder(returned)
        returned.append(self.value)


returned = []

root = Node("a")

root.left_child = Node("b")
root.right_child = Node("c")

root.left_child.left_child = Node("d")
root.left_child.right_child = Node("e")

print(root.preorder())
print(root.inorder())
print(root.postorder())
