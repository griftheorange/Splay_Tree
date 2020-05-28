class Node:
        value = None
        left = None
        right = None
        parent = None

        def __init__(self, value, parent=None):
            self.value = value
            self.parent = parent  