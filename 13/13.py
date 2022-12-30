from collections.abc import Iterable
from functools import cmp_to_key

INPUT_FILE = '13-input.txt'
SEPARATOR1 = [[2]]
SEPARATOR2 = [[6]]

def compare(a, b):
    print(a)
    print(b)
    if isinstance(a, int) and isinstance(b, int):
        return (a > b) - (a < b)
    elif isinstance(a, Iterable) and isinstance(b, Iterable):
        if len(a) and len(b):
            comparison = compare(a[0], b[0])
            if comparison != 0:
                return comparison
            else:
                return compare(a[1:], b[1:])
        return compare(len(a), len(b))
    else:
        if isinstance(a, int):
            a = [a]
        if isinstance(b, int):
            b = [b]
        return compare(a, b)

def check_packets_order():
    ordered_packet_ids = []
    with open(INPUT_FILE) as f:
        lines = f.readlines()
        for i in range((len(lines) // 3) + 1):
            #print(f"========== ID {i+1} ==========")
            packet1 = eval(lines[i*3][:-1])
            packet2 = eval(lines[i*3+1][:-1])
            if compare(packet1, packet2) <= 0:
                ordered_packet_ids.append(i+1)
    return ordered_packet_ids

def sum_packet_ids(ordered_packet_ids):
    return sum(ordered_packet_ids)

def order_packets():
    packets = []
    with open(INPUT_FILE) as f:
        lines = f.readlines()
        for i in range((len(lines) // 3) + 1):
            packets.append(eval(lines[i*3][:-1]))
            packets.append(eval(lines[i*3+1][:-1]))
    packets.append(SEPARATOR1)
    packets.append(SEPARATOR2)
    packets = sorted(packets, key=cmp_to_key(compare))
    return packets

def find_decoder_key(packets):
    index_separator1 = packets.index(SEPARATOR1) + 1
    index_separator2 = packets.index(SEPARATOR2) + 1
    return index_separator1 * index_separator2

#ordered_packet_ids = check_packets_order()
#print(ordered_packet_ids)
#print(sum_packet_ids(ordered_packet_ids))
ordered_packets = order_packets()
print(find_decoder_key(ordered_packets))
