INPUT_FILE = "10-input-test-2.txt"

class Machine:
    def __init__(self):
        self.tick = 1
        self.register = 1
        self.cumulated_signal_strengths = 0

    def to_string(self):
        return f"Machine: tick={self.tick}, register={self.register}, signal_strength={self.cumulated_signal_strengths}"

    def perform_instruction(self, line):
        #print(line)
        line_parts = line.split()
        if line_parts[0] == 'noop':
            self.noop()
        elif line_parts[0] == 'addx':
            self.addx(int(line_parts[1]))

    def noop(self):
        self.tick += 1
        if self.on_signal_strength_tick():
            self.add_to_signal_strength()

    def addx(self, x):
        self.noop()
        self.tick += 1
        self.register += x
        if self.on_signal_strength_tick():
            self.add_to_signal_strength()

    def get_signal_strength(self):
        return self.tick * self.register

    def on_signal_strength_tick(self):
        return self.tick <= 220 and self.tick % 40 == 20

    def add_to_signal_strength(self):
        self.cumulated_signal_strengths += self.get_signal_strength()
        print(self.to_string())

def perform_instructions():
    machine = Machine()
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            machine.perform_instruction(line[:len(line)-1])
            #print(machine.to_string())
    return machine.cumulated_signal_strengths

print(perform_instructions())
