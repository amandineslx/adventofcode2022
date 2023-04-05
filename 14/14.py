from numpy import array

INPUT_FILE = '14-input-test.txt'

class FallingIndefinitelyBlockError(Exception):
    pass

class Cave:
    def __init__(self):
        self.occupied_spaces = dict()
        self.sand_x = 500

    def get_width(self):
        return len(self.occupied_spaces)

    def get_below_occupied_block_y(self, x, y):
        if x not in self.occupied_spaces:
            raise FallingIndefinitelyBlockError()
        arr = array(list(self.occupied_spaces[x]))
        return arr[arr > y].min()

    def add_block(self, sandblock=None, x=None, y=None):
        if sandblock:
            x = sandblock.x
            y = sandblock.y
        if x not in self.occupied_spaces:
            self.occupied_spaces[x] = dict()
        self.occupied_spaces[x] = self.occupied_spaces[x].union([y])

    def is_occupied(self, x, y):
        return x in self.occupied_spaces and y in self.occupied_spaces[x]

class SandBlock:
    def __init__(self, cave):
        self.x = cave.sand_x
        self.y = 0
        self.cave = cave

    def is_outside(self):
        return self.x < min(self.cave.occupied_spaces.keys()) or self.x > max(self.cave.occupied_spaces.keys())

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
        self.y += 1

    def fall_diagonally_right(self):
        self.x += 1
        self.y += 1

    def fall(self):
        is_static = False
        while not is_static:
            print(f"{self.x},{self.y},{is_static}")
            if not self.is_outside():
                if self.can_fall_in_straight_line():
                    print("can fall in straight line")
                    self.fall_in_straight_line()
                elif self.can_fall_diagonally_left():
                    print("can fall in diagonally left")
                    self.fall_diagonally_left()
                elif self.can_fall_diagonally_right():
                    print("can fall in diagonally right")
                    self.fall_diagonally_right()
                else:
                    is_static = True
            else:
                raise FallingIndefinitelyBlockError()

def populate_cave():
    cave = Cave()
    with open(INPUT_FILE) as f:
        lines = f.readlines()
        for line in lines:
            line = line[:-1]
            #print(line)
            pairs = line.split(" -> ")
            if len(pairs) == 1:
                x,y = pairs[0].split(",")
                cave.add_block(x=int(x), y=int(y))
            for i in range(len(pairs)-1):
                axs,ays = pairs[i].split(",")
                ax,ay = int(axs),int(ays)
                bxs,bys = pairs[i+1].split(",")
                bx,by = int(bxs),int(bys)
                #print(f"ax={ax},ay={ay},bx={bx},by={by}")
                if ax == bx:
                    if ax not in cave.occupied_spaces:
                        cave.occupied_spaces[ax] = set()
                    blocks = [i for i in range(min(ay,by),max(ay,by)+1)]
                    #print(f"same x = {ax}")
                    #print(blocks)
                    cave.occupied_spaces[ax] = cave.occupied_spaces[ax].union(blocks)
                elif ay == by:
                    #print(f"same y = {ay}")
                    column_indexes = [i for i in range(min(ax,bx),max(ax,bx)+1)]
                    #print(column_indexes)
                    for i in column_indexes:
                        if i not in cave.occupied_spaces:
                            cave.occupied_spaces[i] = set()
                        cave.occupied_spaces[i] = cave.occupied_spaces[i].union([ay])
    return cave

def count_sand_blocks():
    cave = populate_cave()
    counter = 0
    sandblock = SandBlock(cave)

    while sandblock.can_fall():
        print(cave.occupied_spaces)
        print(counter)
        try:
            sandblock.fall()
            cave.add_block(sandblock)
        except FallingIndefinitelyBlockError:
            return counter
        counter += 1
        sandblock = SandBlock(cave)

    return counter

print(count_sand_blocks())
