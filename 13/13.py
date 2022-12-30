from collections.abc import Iterable

INPUT_FILE = '13-input-test.txt'

def compare(a, b):
    #print(a)
    #print(b)
    result = True
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        if a == b:
            return None
        if a > b:
            return False
        return a <= b
    elif isinstance(a, Iterable) and isinstance(b, Iterable):
        min_common_length = min(len(a), len(b))
        if min_common_length == 0:
            return compare(len(a), len(b))
        for i in range(min_common_length):
            comparison = compare(a[i], b[i])
            if comparison == False:
                return False
            elif comparison == True:
                return True
            elif i == min_common_length - 1 and comparison == None:
                return compare(len(a), len(b))
    else:
        if isinstance(a, int):
            a = [a]
        else:
            b = [b]
        result &= compare(a, b)
    #print(f"Comparison result: {result}")
    return result

def check_packets_order():
    ordered_packet_ids = []
    with open(INPUT_FILE) as f:
        lines = f.readlines()
        for i in range(len(lines) // 3):
            #print(f"========== ID {i+1} ==========")
            packet1 = eval(lines[i*3][:-1])
            packet2 = eval(lines[i*3+1][:-1])
            if compare(packet1, packet2):
                ordered_packet_ids.append(i+1)
    return ordered_packet_ids

def sum_packet_ids(ordered_packet_ids):
    return sum(ordered_packet_ids)

ordered_packet_ids = check_packets_order()
print(ordered_packet_ids)
print(sum_packet_ids(ordered_packet_ids))
