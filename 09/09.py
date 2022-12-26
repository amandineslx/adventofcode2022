INPUT_FILE = '09-input.txt'
DIRECTIONS = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.is_final_knot = False

    def to_string(self, knot_number):
        return f"Knot {knot_number}: ({self.x}, {self.y})"

    def move_as_head(self, direction_char):
        direction = DIRECTIONS[direction_char]
        self.x += direction[0]
        self.y += direction[1]

    def move_as_tail(self, head, positions):
        move = [0, 0]
        move_left = self.should_move_left(head)
        move_right = self.should_move_right(head)
        move_up = self.should_move_up(head)
        move_down = self.should_move_down(head)

        if move_left:
            move[0] = -1
        elif move_right:
            move[0] = 1
        if move_up:
            move[1] = 1
        elif move_down:
            move[1] = -1

        #print(f"Turn: head({head.x}, {head.y}), tail({self.x}, {self.y}), move({move[0]}, {move[1]})")
        self.x += move[0]
        self.y += move[1]
        if self.is_final_knot:
            positions.add((self.x, self.y))

    def should_move_up(self, head):
        condition = head.y == self.y + 2
        condition |= (head.x in [self.x - 2, self.x + 2] and head.y == self.y + 1)
        return condition

    def should_move_down(self, head):
        condition = head.y == self.y - 2
        condition |= (head.x in [self.x - 2, self.x + 2] and head.y == self.y - 1)
        return condition

    def should_move_left(self, head):
        condition = head.x == self.x - 2
        condition |= (head.y in [self.y - 2, self.y + 2] and head.x == self.x - 1)
        return condition

    def should_move_right(self, head):
        condition = head.x == self.x + 2
        condition |= (head.y in [self.y - 2, self.y + 2] and head.x == self.x + 1)
        return condition

class State:
    def __init__(self, number_of_knots):
        self.knots = []
        for _ in range(number_of_knots):
            self.knots.append(Knot())
        self.knots[-1].is_final_knot = True
        self.positions = set()

    def perform_instruction(self, line):
        line_parts = line.split()
        for _ in range(int(line_parts[1])):
            self.knots[0].move_as_head(line_parts[0])
            for i in range(len(self.knots) - 1):
                head_knot = self.knots[i]
                tail_knot = self.knots[i+1]
                tail_knot.move_as_tail(head_knot, self.positions)
                print(tail_knot.to_string(i+1))

    def perform_movements(self):
        with open(INPUT_FILE) as f:
            for line in f.readlines():
                self.perform_instruction(line[:len(line) - 1])
        return len(self.positions)

current_state = State(10)

print(current_state.perform_movements())
