PRIORITIES = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
INPUT_FILE = '03-input.txt'

def split_items_in_bag(item_list):
    mid_length = int((len(item_list))/2)
    compartment_one = item_list[:mid_length]
    compartment_two = item_list[mid_length:]
    return compartment_one, compartment_two

def find_common_item_type(compartment_one, compartment_two):
    intersection = set(compartment_one).intersection(set(compartment_two))
    return list(intersection)[0]

def get_item_priority(item_type):
    return PRIORITIES.index(item_type) + 1

def get_priorities_sum_items():
    total = 0
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            print(f"Line: {line}")
            compartment_one, compartment_two = split_items_in_bag(line[:len(line)-1])
            common_item_type = find_common_item_type(compartment_one, compartment_two)
            priority = get_item_priority(common_item_type)
            print(f"Priority: {priority}")
            total = total + priority
            print(f"Total: {total}")
    return total

def get_elves(file_name):
    elves = []
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            elves = elves + [line[:len(line)-1]]
    return elves

def get_elf_group(elves, n):
    first_member = (3*n)
    last_member = (3*n)+2
    print(f"Group IDs: {first_member}-{last_member}")
    return elves[first_member:last_member+1]

def get_elf_group_badge(elf_group):
    intersection = set(elf_group[0]).intersection(set(elf_group[1]))
    intersection = intersection.intersection(set(elf_group[2]))
    if len(intersection) != 1:
        raise Error("The intersection does not contain a single element")
    return list(intersection)[0]

def get_priorities_sum_badges():
    total = 0
    elves = get_elves(INPUT_FILE)
    number_of_groups = int(len(elves)/3)
    for i in range(0, number_of_groups):
        print(f"Iterator: {i}")
        elf_group = get_elf_group(elves, i)
        if len(elf_group) != 3:
            raise Error("The group does not contain 3 elves")
        badge = get_elf_group_badge(elf_group)
        print(f"Badge: {badge}")
        priority = get_item_priority(badge)
        total = total + priority
        print(f"Total: {total}")
    return total

#print(get_priorities_sum_items())
print(get_priorities_sum_badges())
