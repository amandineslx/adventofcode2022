import re

INPUT_FILE = '15-input.txt'
SECOND_PART = True
MIN_COORDINATES = 0
MAX_COORDINATES = 4000000
FREQUENCY_MULTIPLICATOR = 4000000

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
    if SECOND_PART:
        if l1 < MIN_COORDINATES and l2 < MIN_COORDINATES:
            return []
        elif l1 > MAX_COORDINATES and l2 > MAX_COORDINATES:
            return []
        elif l1 < l2:
            l1 = MIN_COORDINATES if l1 < MIN_COORDINATES else l1
            l2 = MAX_COORDINATES if l2 > MAX_COORDINATES else l2
        else:
            l1 = MAX_COORDINATES if l1 > MAX_COORDINATES else l1
            l2 = MIN_COORDINATES if l2 < MIN_COORDINATES else l2
    xs = []
    if l1 < l2:
        xs.extend(range(l1, l2+1))
    else:
        xs.extend(range(l1, l2+1))
    return xs

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
    #print(f"xs={xs}")
    return xs

def count_places_without_sensor_in_line(y, sensors):
    xs = get_places_without_sensor_in_line(y, sensors)
    return len(xs)

def find_distress_beacon():
    sensors = build_mesh()
    # TODO for each sensor, go one step further in terms of manhattan distance and check if the squares are in range of the other beacons
    # yes -> continue
    # no -> the beacon is there

def compute_distress_beacon_tuning_frequency():
    distress_beacon_position = find_distress_beacon()
    return distress_beacon_position[0] * FREQUENCY_MULTIPLICATOR + distress_beacon_position[1]

#print(find_values('Sensor at x=2, y=18: closest beacon is at x=-2, y=15'))
#print(build_mesh())
#print(count_places_without_sensor_in_line(10))
#print(count_places_without_sensor_in_line(2000000, build_mesh()))
print(compute_distress_beacon_tuning_frequency())
