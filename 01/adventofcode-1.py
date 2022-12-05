INPUT_FILE = 'adventofcode-1-input.txt'

def get_max_calories():
    with open(INPUT_FILE) as f:
        max = 0
        current = 0
        for line in f.readlines():
            print(f"line: {line}")
            print(f"current: {current}")
            print(f"max {max}")
            if line == '\n':
                if current > max:
                    max = current
                current = 0
            else:
                current = current + int(line)
    return max

def get_three_top_calories():
    elves = []
    with open(INPUT_FILE) as f:
        current = 0
        for line in f.readlines():
            print(f"line: {line}")
            print(f"current: {current}")
            if line == '\n':
                elves.append(current)
                current = 0
            else:
                current = current + int(line)
    print(f"Elves: {elves}")
    elves.sort(reverse=True)
    print(f"Sorted elves: {elves}")
    return elves[0] + elves[1] + elves[2]

#print(get_max_calories())
print(get_three_top_calories())
