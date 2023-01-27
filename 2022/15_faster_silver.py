import re

lines = [l.strip() for l in open("input/day15.txt").readlines()]

observed_y = 2000000


def points_in_range(start, end):
    distance = abs(start[0] - end[0]) + abs(start[1] - end[1])
    for x in range(start[0] - distance, start[0] + distance + 1):
        if abs(start[0] - x) + abs(start[1] - observed_y) <= distance:
            if (x, observed_y) not in sensors and (x, observed_y) not in beacons:
                not_sensors.add((x, observed_y))


sensors = set()
beacons = set()
beaconsd = set()
not_sensors = set()
out_of_range = set()
for line in lines:
    sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r'\d+', line))
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    sensors.add((sensor_x, sensor_y))
    beacons.add((beacon_x, beacon_y))
    beaconsd.add((beacon_x, beacon_y, distance))
    points_in_range([sensor_x, sensor_y], [beacon_x, beacon_y])

print("Silver:", len(not_sensors))
