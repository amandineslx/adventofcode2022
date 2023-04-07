import re

INPUT_FILE = '15-input-test.txt'
MIN_COORDINATES = 0
MAX_COORDINATES = 20
FREQUENCY_MULTIPLICATOR = 4000000
MESH = []

class Sensor:
    def __init__(self, x, y, beacon):
        self.x = x
        self.y = y
        self.beacon = beacon
        self.compute_manhattan_distance()

    def compute_manhattan_distance(self):
        self.distance_to_beacon = compute_manhattan_distance(self.get_coordinates(), self.beacon)

    def get_coordinates(self):
        return (self.x, self.y)

    def to_string(self):
        return f"Sensor(x={self.x},y={self.y},distance={self.distance_to_beacon})"

def read_coordinates(line):
    regex = r'^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'
    return re.search(regex, line).groups()

def build_mesh():
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            coordinates = read_coordinates(line)
            beacon_coordinates = (int(coordinates[2]),int(coordinates[3]))
            MESH.append(Sensor(int(coordinates[0]), int(coordinates[1]), beacon_coordinates))

def print_mesh():
    print("-----MESH-----")
    for sensor in MESH:
        print(sensor.to_string())
    print("--------------")

# PART 1
def compute_manhattan_distance(coordinates1, coordinates2):
    return abs(coordinates1[0] - coordinates2[0]) + abs(coordinates1[1] - coordinates2[1])

def get_xs_in_manhattan_distance(y, sensor):
    x_abs = sensor.distance_to_beacon - abs(y - sensor.y)
    l1 = -1 * x_abs + sensor.x
    l2 = x_abs + sensor.x
    return [*range(l1, l2+1)]

def get_places_without_sensor_in_line(y, sensors):
    xs = set()
    for sensor in sensors:
        #print(f"Sensor({sensor.x},{sensor.y})")
        xs_for_sensor = get_xs_in_manhattan_distance(y, sensor)
        #print(f"xs_for_sensor({sensor.x},{sensor.y})={xs_for_sensor}")
        xs = xs.union(list(xs_for_sensor))
    for sensor in sensors:
        if sensor.beacon[1] == y:
            if sensor.beacon[0] in xs:
                xs.remove(sensor.beacon[0])
    return xs

def count_places_without_sensor_in_line(y):
    xs = get_places_without_sensor_in_line(y, MESH)
    return len(xs)

# PART 2
def find_coordinates_across_manhattan_distance(sensor):
    coordinates = set()
    x = sensor.x
    y = sensor.y
    d = sensor.distance_to_beacon + 1
    for i in range(d+2):
        print(i)
        coordinates.update([(x-d+i,y+i),(x+d-i,y+i),(x+d-i,y-i),(x-d+i,y-i)])
    print(coordinates)
    return coordinates

def is_within_sensor_manhattan_distance(x, y, sensor):
    manhattan_distance_to_sensor = compute_manhattan_distance((x, y), sensor.get_coordinates())
    return manhattan_distance_to_sensor <= sensor.distance_to_beacon

def can_distress_beacon_be_here(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    if x > MAX_COORDINATES or y > MAX_COORDINATES or x < 0 or y < 0:
        return False
    for sensor in MESH:
        if is_within_sensor_manhattan_distance(x, y, sensor):
            return False
    return True

def find_distress_beacon():
    for sensor in MESH:
        print(sensor.to_string())
        coordinates = find_coordinates_across_manhattan_distance(sensor)
        for coordinate in coordinates:
            if can_distress_beacon_be_here(coordinate):
                print(coordinate)
                return coordinate

def compute_distress_beacon_tuning_frequency():
    print_mesh()
    distress_beacon_position = find_distress_beacon()
    return distress_beacon_position[0] * FREQUENCY_MULTIPLICATOR + distress_beacon_position[1]

build_mesh()
#print(find_values('Sensor at x=2, y=18: closest beacon is at x=-2, y=15'))
#print(build_mesh())
#print(count_places_without_sensor_in_line(10))
#print(count_places_without_sensor_in_line(2000000))
print(compute_distress_beacon_tuning_frequency())
