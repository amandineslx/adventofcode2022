INPUT_FILE = '08-input.txt'

def get_input():
    input = []
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            input.append(line[:len(line)-1])
    return input

def get_tree_value(input, x, y):
    return int(input[y][x])

def get_tree_visibility_left(input, x, y):
    tree_value = get_tree_value(input, x, y)
    if x == 0:
        return True, 0
    for i in range(x - 1, -1, -1):
        if get_tree_value(input, i, y) >= tree_value:
            return False, x - i
    return True, x

def get_tree_visibility_right(input, x, y):
    tree_value = get_tree_value(input, x, y)
    if x == len(input[0]) - 1:
        return True, 0
    for i in range(x + 1, len(input[0])):
        if get_tree_value(input, i, y) >= tree_value:
            return False, i - x
    return True, len(input[0]) - x - 1

def get_tree_visibility_up(input, x, y):
    tree_value = get_tree_value(input, x, y)
    if y == 0:
        return True, 0
    for i in range(y - 1, -1, -1):
        if get_tree_value(input, x, i) >= tree_value:
            return False, y - i
    return True, y

def get_tree_visibility_down(input, x, y):
    tree_value = get_tree_value(input, x, y)
    if y == len(input) - 1:
        return True, 0
    for i in range(y + 1, len(input)):
        if get_tree_value(input, x, i) >= tree_value:
            return False, i - y
    return True, len(input) - y - 1

def get_tree_visibility(input, x, y):
    left = get_tree_visibility_left(input, x, y)
    right = get_tree_visibility_right(input, x, y)
    up = get_tree_visibility_up(input, x, y)
    down = get_tree_visibility_down(input, x, y)

    is_tree_visible = left[0] or right[0] or up[0] or down[0]
    cynematic_score = left[1] * right[1] * up[1] * down[1]

    return is_tree_visible, cynematic_score

def get_visible_trees():
    input = get_input()
    visible_trees = 0
    max_cynematic_score = 0
    for i in range(len(input[0])):
        for j in range(len(input)):
            tree_visibility = get_tree_visibility(input, i, j)
            print(tree_visibility[1])
            if tree_visibility[0]:
                visible_trees += 1
            if tree_visibility[1] > max_cynematic_score:
                max_cynematic_score = tree_visibility[1]
    return visible_trees, max_cynematic_score

print(get_visible_trees())
