INPUT_FILE = '08-input.txt'

def get_input():
    input = []
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            input.append(line[:len(line)-1])
    return input

def get_tree_value(input, x, y):
    return int(input[y][x])

def is_tree_visible_left(input, x, y):
    tree_value = get_tree_value(input, x, y)
    if x == 0:
        return True
    for i in range(x):
        if get_tree_value(input, i, y) >= tree_value:
            return False
    return True

def is_tree_visible_right(input, x, y):
    tree_value = get_tree_value(input, x, y)
    if x == len(input[0]) - 1:
        return True
    for i in range(len(input[0]) - x - 1):
        if get_tree_value(input, len(input[0]) - 1 - i, y) >= tree_value:
            return False
    return True

def is_tree_visible_up(input, x, y):
    tree_value = get_tree_value(input, x, y)
    if y == 0:
        return True
    for i in range(y):
        if get_tree_value(input, x, i) >= tree_value:
            return False
    return True

def is_tree_visible_down(input, x, y):
    tree_value = get_tree_value(input, x, y)
    if y == len(input) - 1:
        return True
    for i in range(len(input) - y - 1):
        if get_tree_value(input, x, len(input) - 1 - i) >= tree_value:
            return False
    return True

def is_tree_visible(input, x, y):
    is_tree_visible = is_tree_visible_left(input, x, y)
    is_tree_visible |= is_tree_visible_right(input, x, y)
    is_tree_visible |= is_tree_visible_up(input, x, y)
    is_tree_visible |= is_tree_visible_down(input, x, y)
    return is_tree_visible

def get_visible_trees():
    input = get_input()
    visible_trees = 0
    for i in range(len(input[0])):
        for j in range(len(input)):
            if is_tree_visible(input, i, j):
                visible_trees += 1
    return visible_trees

print(get_visible_trees())
