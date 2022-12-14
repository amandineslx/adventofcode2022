INPUT_FILE = '06-input.txt'

def scan_input(input_signal, sequence_size=4):
    for i in range(len(input_signal) - sequence_size):
        packet = input_signal[i:i+sequence_size]
        print(packet)
        if len(set(packet)) == sequence_size:
            return i+sequence_size

def detect_sequence(sequence_size=4):
    with open(INPUT_FILE, 'r') as f:
        input_signal = f.readlines()[0][:-1]
        return scan_input(input_signal, sequence_size)

#print(detect_sequence())
print(detect_sequence(sequence_size=14))
