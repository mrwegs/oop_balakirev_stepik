class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        obj = root
        index = obj.indx
        while obj.left is not None and obj.right is not None:
            if x[index]:
                obj = obj.left
                index = obj.indx
            else:
                obj = obj.right
                index = obj.indx
        else:
            return obj.value

    @classmethod
    def add_obj(cls, obj: TreeObj, node: TreeObj = None, left: bool = True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj