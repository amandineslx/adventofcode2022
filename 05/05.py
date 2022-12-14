CARGO = [
    ['C', 'Z', 'N', 'B', 'M', 'W', 'Q', 'V'],
    ['H', 'Z', 'R', 'W', 'C', 'B'],
    ['F', 'Q', 'R', 'J'],
    ['Z', 'S', 'W', 'H', 'F', 'N', 'M', 'T'],
    ['G', 'F', 'W', 'L', 'N', 'Q', 'P'],
    ['L', 'P', 'W'],
    ['V', 'B', 'D', 'R', 'G', 'C', 'Q', 'J'],
    ['Z', 'Q', 'N', 'B', 'W'],
    ['H', 'L', 'F', 'C', 'G', 'T', 'J']
]
INPUT_FILE = '05-input.txt'

def move(number_of_packages, col_from, col_to, crate_mover_9001=False):
    index_col_from = col_from - 1
    index_col_to = col_to - 1
    moved_crates = CARGO[index_col_from][-number_of_packages:]
    CARGO[index_col_from] = CARGO[index_col_from][:-number_of_packages]
    if not crate_mover_9001:
        moved_crates.reverse()
    CARGO[index_col_to] += moved_crates

def get_result():
    result = ''
    for column in CARGO:
        if column:
            result += column[-1]
    return result

def get_top_packages(crate_mover_9001=False):
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            if line.startswith('move'):
                line_chunks = line.split()
                move(int(line_chunks[1]), int(line_chunks[3]), int(line_chunks[5]), crate_mover_9001)
    return get_result()

#print(get_top_packages())
print(get_top_packages(crate_mover_9001=True))
