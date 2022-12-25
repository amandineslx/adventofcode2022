INPUT_FILE = '09-input.txt'
DIRECTIONS = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

class State:
    def __init__(self):
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
        self.positions = set()

    def move_head(self, direction_char):
        direction = DIRECTIONS[direction_char]
        self.head_x += direction[0]
        self.head_y += direction[1]

    def move_tail(self):
        move = [0, 0]
        move_left = self.should_move_left()
        move_right = self.should_move_right()
        move_up = self.should_move_up()
        move_down = self.should_move_down()

        if move_left:
            move[0] = -1
        elif move_right:
            move[0] = 1
        if move_up:
            move[1] = 1
        elif move_down:
            move[1] = -1

        print(f"Turn: head({self.head_x}, {self.head_y}), tail({self.tail_x}, {self.tail_y}), move({move[0]}, {move[1]})")
        self.tail_x += move[0]
        self.tail_y += move[1]
        self.positions.add((self.tail_x, self.tail_y))

    def should_move_up(self):
        condition = self.head_y == self.tail_y + 2
        condition |= (self.head_x in [self.tail_x - 2, self.tail_x + 2] and self.head_y == self.tail_y + 1)
        return condition

    def should_move_down(self):
        condition = self.head_y == self.tail_y - 2
        condition |= (self.head_x in [self.tail_x - 2, self.tail_x + 2] and self.head_y == self.tail_y - 1)
        return condition

    def should_move_left(self):
        condition = self.head_x == self.tail_x - 2
        condition |= (self.head_y in [self.tail_y - 2, self.tail_y + 2] and self.head_x == self.tail_x - 1)
        return condition

    def should_move_right(self):
        condition = self.head_x == self.tail_x + 2
        condition |= (self.head_y in [self.tail_y - 2, self.tail_y + 2] and self.head_x == self.tail_x + 1)
        return condition

    def perform_instruction(self, line):
        line_parts = line.split()
        for _ in range(int(line_parts[1])):
            self.move_head(line_parts[0])
            self.move_tail()

    def perform_movements(self):
        current_state = State()
        with open(INPUT_FILE) as f:
            for line in f.readlines():
                self.perform_instruction(line[:len(line) - 1])
        return len(self.positions)

current_state = State()

print(current_state.perform_movements())
