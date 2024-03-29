from numpy import array

INPUT_FILE = '14-input.txt'
SECOND_PART = True

class FallingIndefinitelyBlockError(Exception):
    pass

class Cave:
    def __init__(self):
        self.occupied_spaces = dict()
        self.sand_x = 500
        self.max_y = None

    @staticmethod
    def get_instance_from_file(file_name):
        cave = Cave()
        with open(file_name) as f:
            lines = f.readlines()
            for line in lines:
                line = line[:-1]
                pairs = line.split(" -> ")
                if len(pairs) == 1:
                    x,y = pairs[0].split(",")
                    cave.add_block(x=int(x), y=int(y))
                for i in range(len(pairs)-1):
                    axs,ays = pairs[i].split(",")
                    ax,ay = int(axs),int(ays)
                    bxs,bys = pairs[i+1].split(",")
                    bx,by = int(bxs),int(bys)
                    if ax == bx:
                        if ax not in cave.occupied_spaces:
                            cave.occupied_spaces[ax] = set()
                        blocks = [i for i in range(min(ay,by), max(ay,by)+1)]
                        cave.occupied_spaces[ax] = cave.occupied_spaces[ax].union(blocks)
                    elif ay == by:
                        column_indexes = [i for i in range(min(ax,bx), max(ax,bx)+1)]
                        for i in column_indexes:
                            cave.add_block(x=i, y=ay)
        cave.max_y = cave._get_max_y()
        return cave

    def get_below_occupied_block_y(self, x, y):
        if x not in self.occupied_spaces and SECOND_PART:
            return self.max_y + 2
        arr = array(list(self.occupied_spaces[x]))
        superior_values = arr[arr > y]
        if not superior_values.any():
            if SECOND_PART:
                return self.max_y + 2
            else:
                raise FallingIndefinitelyBlockError()
        return superior_values.min()

    def add_block(self, sandblock=None, x=None, y=None):
        if sandblock:
            x = sandblock.x
            y = sandblock.y
        if x not in self.occupied_spaces:
            self.occupied_spaces[x] = set()
        self.occupied_spaces[x] = self.occupied_spaces[x].union([y])

    def is_occupied(self, x, y):
        condition = x in self.occupied_spaces and y in self.occupied_spaces[x]
        if SECOND_PART:
            return y == self.max_y + 2 or condition
        else:
            return condition

    def get_min_x(self):
        return min(self.occupied_spaces.keys())

    def get_max_x(self):
        return max(self.occupied_spaces.keys())

    def _get_max_y(self):
        m = 0
        for col in list(self.occupied_spaces.values()):
            if max(col) > m:
                m = max(col)
        return m

    def print(self):
        min_x = self.get_min_x()
        max_x = self.get_max_x()
        max_y = self.max_y
        grid = ["" for i in range(max_y+2 if SECOND_PART else max_y+1)]
        for y in range(max_y+1):
            for x in range(min_x, max_x+1):
                if x in self.occupied_spaces and y in self.occupied_spaces[x]:
                    grid[y] += "#"
                else:
                    grid[y] += "."
        source_index = 500-min_x
        grid[0] = grid[0][:source_index] + "o" + grid[0][source_index + 1:]
        if SECOND_PART:
            for x in range(min_x, max_x+1):
                grid[max_y+1] += "#"
        for line in grid:
            print(line)

class SandBlock:
    def __init__(self, cave):
        self.x = cave.sand_x
        self.y = 0
        self.cave = cave

    def is_outside(self):
        return False if SECOND_PART else (self.x < min(self.cave.occupied_spaces.keys()) or self.x > max(self.cave.occupied_spaces.keys()))

    def can_fall_in_straight_line(self):
        return not self.cave.is_occupied(self.x, self.y + 1)

    def can_fall_diagonally_left(self):
        return not self.cave.is_occupied(self.x - 1, self.y + 1)

    def can_fall_diagonally_right(self):
        return not self.cave.is_occupied(self.x + 1, self.y + 1)

    def can_fall(self):
        return self.can_fall_in_straight_line() or self.can_fall_diagonally_left() or self.can_fall_diagonally_right()

    def fall_in_straight_line(self):
        self.y = self.cave.get_below_occupied_block_y(self.x, self.y) - 1

    def fall_diagonally_left(self):
        self.x -= 1
        self.y += 1 # y is increasing going down

    def fall_diagonally_right(self):
        self.x += 1
        self.y += 1 # y is increasing going down

    def fall(self):
        is_static = False
        while not is_static:
            if not self.is_outside():
                if self.can_fall_in_straight_line():
                    self.fall_in_straight_line()
                elif self.can_fall_diagonally_left():
                    self.fall_diagonally_left()
                elif self.can_fall_diagonally_right():
                    self.fall_diagonally_right()
                else:
                    is_static = True
            else:
                # can never be reached in SECOND_PART as is_outside will always return False
                raise FallingIndefinitelyBlockError()

def count_sand_blocks():
    cave = Cave.get_instance_from_file(INPUT_FILE)
    #cave.print()
    counter = 0
    sandblock = SandBlock(cave)

    while sandblock.can_fall():
        #cave.print()
        try:
            sandblock.fall()
            cave.add_block(sandblock)
        except FallingIndefinitelyBlockError:
            return counter
        counter += 1
        sandblock = SandBlock(cave)

    return counter+1

def print_cave_for_test():
    cave = Cave.get_instance_from_file(INPUT_FILE)
    cave.print()

print(count_sand_blocks())
# print_cave_for_test()
