from node import Node

class Splay:
    root = None

    def __init__(self, init_tree_type, arr):
        if(init_tree_type == 'normal'):
            self.binary_tree_gen(arr)
        elif(init_tree_type == 'left'):
            self.left_weighted_tree_gen(arr)
        elif(init_tree_type == 'right'):
            self.right_weighted_tree_gen(arr)

    # Iterates through binary tree pathing to target value, if End of tree is encountered, splays on the 'closest' value, being the previous node encountered
    def find(self, value):
        if(self.root):
            previous = None
            current = self.root
            while True:
                if(current == None):
                    self.splay(previous)
                    return current
                elif(value == current.value):
                    self.splay(current)
                    return current
                elif(value > current.value):
                    previous = current 
                    current = current.right
                elif(value < current.value):
                    previous = current 
                    current = current.left

    def splay(self, node):
        print('splaying')

    def insert_node(self, node, root):
        if(node.value > root.value):
            if(root.right):
                self.insert_node(node, root.right)
            else:
                root.right = node
                node.parent = root
        elif(node.value < root.value):
            if(root.left):
                self.insert_node(node, root.left)
            else:
                root.left = node
                node.parent = root


    def binary_tree_gen(self, arr):
        if(len(arr) == 1):
            self.root = Node(arr[0])
            return
        if(len(arr) > 1):
            self.root = Node(arr[0])
            for i in range(1, len(arr)):
                new_node = Node(arr[i])
                self.insert_node(new_node, self.root)
    
    def left_weighted_tree_gen(self, arr):
        if(len(arr) == 1):
            self.root = Node(arr[0])
            return
        if(len(arr) > 1):
            arr.sort()
            self.root = Node(arr[-1])
            current = self.root
            for i in reversed(range(len(arr)-1)):
                if(arr[i] < current.value):
                    new_node = Node(arr[i])
                    current.left = new_node
                    new_node.parent = current
                    current = new_node
    
    def right_weighted_tree_gen(self, arr):
        if(len(arr) == 1):
            self.root = Node(arr[0])
            return
        if(len(arr) > 1):
            arr.sort()
            self.root = Node(arr[0])
            current = self.root
            for i in range(1, len(arr)):
                if(arr[i] > current.value):
                    new_node = Node(arr[i])
                    current.right = new_node
                    new_node.parent = current
                    current = new_node

    def print_tree(self):
        levels = []
        last_depth = 0

        def breadth_bins(node, depth):
            def bin_insert(value, bin_depth):
                try:
                    levels[bin_depth].append(value)
                except IndexError:
                    levels.append([])
                    levels[bin_depth] = [value]

            bin_insert(node.value, depth)

            if(node.left):
                breadth_bins(node.left, depth+1)
            else:
                bin_insert("N", depth+1)
            if(node.right):
                breadth_bins(node.right, depth+1)
            else:
                bin_insert("N", depth+1)

        if(self.root):
            traverser = self.root
            breadth_bins(traverser, 0)
            for i in range(len(levels)):
                print("Depth {depth}: {spaces}{values}".format(depth=i+1, spaces=(len(levels)-i)*" ", values=" ".join(str(k) for k in levels[i])))


        
splay_tree = Splay('normal', [5, 6, 8, 3, 8, 3, 5, 8, -4, -2, -70])
splay_tree.print_tree()
print('')
left_splay_tree = Splay('left', [5, 6, 8, 3, 8, 3, 5, 8, -4, -2, -70])
left_splay_tree.print_tree()
print('')
right_splay_tree = Splay('right', [5, 6, 8, 3, 8, 3, 5, 8, -4, -2, -70])
right_splay_tree.print_tree()

node = splay_tree.find(-4)
if(node): 
    print(node.value) 
else: 
    print(node)

node = splay_tree.find(80)
if(node): 
    print(node.value) 
else: 
    print(node)
