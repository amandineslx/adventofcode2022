import re

INPUT_FILE = '15-input.txt'

#compute distance from sensor to beacon
#find all xs from y where distance to beacon is inferior to this distance
#set of xs

class Sensor:
    def __init__(self, x, y, beacon):
        self.x = x
        self.y = y
        self.beacon = beacon
        self.compute_manhattan_distance()

    def compute_manhattan_distance(self):
        self.distance_to_beacon = abs(self.x - self.beacon[0]) + abs(self.y - self.beacon[1])

def find_coordinates(line):
    regex = r'^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'
    return re.search(regex, line).groups()

def build_mesh():
    sensors = []
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            coordinates = find_coordinates(line)
            beacon_coordinates = (int(coordinates[2]),int(coordinates[3]))
            sensors.append(Sensor(int(coordinates[0]), int(coordinates[1]), beacon_coordinates))
    return sensors

def get_xs_in_manhattan_distance(y, sensor):
    x_abs = sensor.distance_to_beacon - abs(y - sensor.y)
    l1 = -1 * x_abs + sensor.x
    l2 = x_abs + sensor.x
    xs = []
    if l1 < l2:
        xs.extend(range(l1, l2+1))
    else:
        xs.extend(range(l1, l2+1))
    return xs

def count_places_without_sensor_in_line(y):
    sensors = build_mesh()
    xs = set()
    for sensor in sensors:
        xs_for_sensor = get_xs_in_manhattan_distance(y, sensor)
        print(f"xs_for_sensor({sensor.x},{sensor.y})={xs_for_sensor}")
        xs = xs.union(list(xs_for_sensor))
    for sensor in sensors:
        if sensor.beacon[1] == y:
            if sensor.beacon[0] in xs:
                xs.remove(sensor.beacon[0])
    print(f"xs={xs}")
    return len(xs)

#print(find_values('Sensor at x=2, y=18: closest beacon is at x=-2, y=15'))
#print(build_mesh())
#print(count_places_without_sensor_in_line(10))
print(count_places_without_sensor_in_line(2000000))
