import re
import math

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def as_string(self):
        string = ""
        if self.value is not None:
            string += str(self.value)
        else:
            string += "["
            string += self.left.as_string()
            string += ","
            string += self.right.as_string()
            string += "]"
        return string

def add(tree1, tree2):
    root = Tree()
    root.left = tree1
    root.right = tree2
    return root

def parse_entire_tree(input_line):
    tree, idx = parse_tree(input_line)
    return tree

def parse_tree(input_line):
    root = Tree()
    idx = 0
    if input_line[idx] == "[":
        idx += 1
        root.left, read = parse_tree(input_line[idx:])
        idx += read
    if input_line[idx] == ",":
        idx += 1
        root.right, read = parse_tree(input_line[idx:])
        idx += read
    if input_line[idx] == "]":
        idx += 1
        return root, idx
    if input_line[idx].isdigit():
        number = re.search(r'\d+', input_line[idx]).group()
        root.value = int(number)
        return root, len(number)

def find_exploding_node(tree, level):
    if tree.value is not None:
        return None
    if level == 4:
        return tree
    else:
        node = find_exploding_node(tree.left, level+1)
        if node is not None:
            return node
        node = find_exploding_node(tree.right, level+1)
        if node is not None:
            return node

def flatten_tree(tree, flat):
    flat.append(tree)
    if tree.value is not None:
        return
    else:
        flatten_tree(tree.left, flat)
        flatten_tree(tree.right, flat)

    return flat

def explode(tree, node):
    flatted_tree = []
    flatten_tree(tree, flatted_tree)
    found_idx = 0
    for idx in range(0, len(flatted_tree)):
        if flatted_tree[idx] == node:
            found_idx = idx
            break
    idx_left = found_idx + 1
    idx_right = found_idx + 2
    for idx in range(found_idx-1, -1, -1):
        if flatted_tree[idx].value is not None:
            flatted_tree[idx].value += flatted_tree[idx_left].value
            break

    for idx in range(found_idx + 3, len(flatted_tree)):
        if flatted_tree[idx].value is not None:
            flatted_tree[idx].value += flatted_tree[idx_right].value
            break

    flatted_tree[found_idx].left = None
    flatted_tree[found_idx].right = None
    flatted_tree[found_idx].value = 0

def find_node_to_split(tree):
    if tree.value is not None:
        if tree.value > 9:
            return tree
        else:
            return None
    else:
        node = find_node_to_split(tree.left)
        if node is not None:
            return node
        node = find_node_to_split(tree.right)
        if node is not None:
            return node


def reduce(tree):
    node = find_exploding_node(tree, 0)
    while node is not None:
        explode(tree, node)
        node = find_exploding_node(tree, 0)

    node = find_node_to_split(tree)
    if node is not None:
        node.left = Tree()
        node.right = Tree()
        node.left.value = math.floor(node.value / 2)
        node.right.value = math.ceil(node.value / 2)
        node.value = None
        reduce(tree)

def find_calculated_tree(input):
    full_tree = None
    for row in input:
        tree = parse_entire_tree(row)
        if full_tree is None:
            full_tree = tree
        else:
            full_tree = add(full_tree, tree)
            reduce(full_tree)
    return full_tree

def find_magnitude(tree):
    sum = 0
    if tree.left.value is not None:
        sum += tree.left.value * 3
    else:
        sum += find_magnitude(tree.left) * 3
    if tree.right.value is not None:
        sum += tree.right.value * 2
    else:
        sum += find_magnitude(tree.right) * 2
    return sum



input = open("input18", "r").readlines()

for i in range(0, len(input)):
    input[i] = input[i].rstrip()

max_magnitude = 0
for i in range(0, len(input)):
    for y in range(0, len(input)):
        print("i:", i, " y:", y)
        new_input = []
        if i == y:
            break
        new_input.append(input[i])
        new_input.append(input[y])
        full_tree = find_calculated_tree(new_input)
        sum = find_magnitude(full_tree)
        if sum > max_magnitude:
            max_magnitude = sum


print("The answer is: ", max_magnitude)
