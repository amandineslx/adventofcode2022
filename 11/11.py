INPUT_FILE = '11-input.txt'
MAX_NUMBER_OF_ROUNDS = 10000

class Monkey:
    def __init__(self, number):
        self.number = number
        self.activity = 0
        self.items = []
        self.operation = ''
        self.divisibility_test = -1
        self.monkey_number_if_true = -1
        self.monkey_number_if_false = -1

    def to_string(self):
        return f'Monkey {self.number}: activity={self.activity}, items=({self.items}), operation={self.operation}, divisibility_test={self.divisibility_test}, monkey_if_true={self.monkey_number_if_true}, monkey_if_false={self.monkey_number_if_false}'

    def inspect_item(self, item, global_modulo=None):
        self.activity += 1
        new_item_value = worry_about_item(item, self.operation)
        new_item_value = feel_relief(new_item_value, global_modulo)
        return new_item_value, self.get_monkey_target_number(new_item_value)

    def get_monkey_target_number(self, item):
        if item % self.divisibility_test == 0:
            return self.monkey_number_if_true
        else:
            return self.monkey_number_if_false

    def throw_item(self, new_item_value, monkey_target):
        monkey_target.items.append(new_item_value)

    def finish_round(self):
        self.items = []

def worry_about_item(item, operation):
    old = item
    return int(eval(operation))

def feel_relief(item, global_modulo=None):
    if not global_modulo:
        return item // 3
    else:
        return item % global_modulo

def initialize_monkeys():
    monkeys = []
    with open(INPUT_FILE) as f:
        monkey = None
        for line in f.readlines():
            if line != '\n':
                line_parts = line[:-1].split()
                if line_parts[0] == 'Monkey':
                    monkey = Monkey(line_parts[1].split(':')[0])
                    monkeys.append(monkey)
                elif line_parts[0] == 'Starting':
                    for i in range(2, len(line_parts)):
                        monkey.items.append(int(line_parts[i].split(',')[0]))
                elif line_parts[0] == 'Operation:':
                    monkey.operation = line[:-1].split('=')[1][1:]
                elif line_parts[0] == 'Test:':
                    monkey.divisibility_test = int(line_parts[3])
                elif line_parts[0] == 'If':
                    if line_parts[1] == 'true:':
                        monkey.monkey_number_if_true = int(line_parts[5])
                    elif line_parts[1] == 'false:':
                        monkey.monkey_number_if_false = int(line_parts[5])
                #print(monkey.to_string())
    print_monkeys(monkeys)
    return monkeys

def print_monkeys(monkeys):
    for monkey in monkeys:
        print(monkey.to_string())

def take_rounds(monkeys):
    global_modulo = 1
    for monkey in monkeys:
        global_modulo *= monkey.divisibility_test
    for i in range(MAX_NUMBER_OF_ROUNDS):
        print(f"ROUND {i}")
        for monkey in monkeys:
            for item in monkey.items:
                #print(f"Monkey={monkey.number}, item={item}")
                throw = monkey.inspect_item(item, global_modulo)
                monkey.throw_item(throw[0], monkeys[throw[1]])
            monkey.finish_round()
        print_monkeys(monkeys)

def get_most_actives_monkeys_cumulated(monkeys):
    monkey_activities = [monkey.activity for monkey in monkeys]
    monkey_activities.sort(reverse=True)
    return monkey_activities[0] * monkey_activities[1]

monkeys = initialize_monkeys()
take_rounds(monkeys)
print(get_most_actives_monkeys_cumulated(monkeys))
