INPUT_FILE = "10-input.txt"
CYCLES_PADDING = 40
FIRST_CYCLE = 20
LAST_CYCLE = 220

class Machine:
    def __init__(self):
        self.tick = 1
        self.register = 1
        self.cumulated_signal_strengths = 0
        number_of_lines = ((LAST_CYCLE - FIRST_CYCLE) // CYCLES_PADDING) + 1
        self.screen = [[] for _ in range(number_of_lines)]

    def to_string(self):
        result = f"Machine: tick={self.tick}, register={self.register}, signal_strength={self.cumulated_signal_strengths}"
        for i in range(len(self.screen)):
            result += '\n'
            result += ''.join(self.screen[i])
        return result

    def perform_instruction(self, line):
        #print(line)
        line_parts = line.split()
        if line_parts[0] == 'noop':
            self.noop()
        elif line_parts[0] == 'addx':
            self.addx(int(line_parts[1]))

    def noop(self):
        self.add_pixel()
        self.tick += 1
        if self.on_signal_strength_tick():
            self.add_to_signal_strength()

    def addx(self, x):
        self.noop()
        self.add_pixel()
        self.tick += 1
        self.register += x
        if self.on_signal_strength_tick():
            self.add_to_signal_strength()

    def get_signal_strength(self):
        return self.tick * self.register

    def on_signal_strength_tick(self):
        return self.tick <= LAST_CYCLE and self.tick % CYCLES_PADDING == FIRST_CYCLE

    def add_to_signal_strength(self):
        self.cumulated_signal_strengths += self.get_signal_strength()
        print(self.to_string())

    def add_pixel(self):
        line = (self.tick - 1) // CYCLES_PADDING
        col = (self.tick - 1) % CYCLES_PADDING
        print(f"Pixel position: ({line}, {col})")
        if col in [self.register - 1, self.register, self.register + 1]:
            self.screen[line].append('#')
        else:
            self.screen[line].append('.')
        if len(self.screen[line]) != col + 1:
            print(self.to_string())
            raise Exception(f"Misalignment between line length {len(self.screen[line])} and column number {col + 1}")
        print(self.to_string())

def perform_instructions():
    machine = Machine()
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            machine.perform_instruction(line[:len(line)-1])
            #print(machine.to_string())
    return machine.cumulated_signal_strengths

print(perform_instructions())
