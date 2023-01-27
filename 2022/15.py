import re

data = [line.strip() for line in open("input/day15.txt", "r")]


class SENSOR:
	def __init__(self, sx, sy, bx, by, d):
		self.x = sx
		self.y = sy
		self.closest = [bx, by]
		self.distance = d


sensors = list()
beacons = list()
x_min, x_max = float('inf'), float('-inf')

for line in data:
	s_x, s_y, b_x, b_y = map(int, re.findall(r'-?\d+', line))
	dist = abs(s_x - b_x) + abs(s_y - b_y)
	mn = min(s_x, s_y) - dist
	mx = max(s_x, s_y) + dist
	x_min = mn if mn < x_min else x_min
	x_max = mx if mx > x_max else x_max
	sensors.append(SENSOR(s_x, s_y, b_x, b_y, dist))
	beacons.append([b_x, b_y])

y = 2000000
# y = 10
silver = 0
for x in range(x_min, x_max):
	for sensor in sensors:
		if abs(x - sensor.x) + abs(y - sensor.y) <= sensor.distance:
			if [x, y] not in beacons and [x, y] not in sensors:
				silver += 1
				break
print("Silver:", silver)

for sensor in sensors:
	for x, y in enumerate(range(sensor.distance + 1, -1, -1)):
		sides = [
			[x + sensor.x, y + sensor.y],
			[-x + sensor.x, y + sensor.y],
			[x + sensor.x, -y + sensor.y],
			[-x + sensor.x, -y + sensor.y]
		]
		for side in sides:
			if 0 <= side[0] <= 4000000 and 0 <= side[1] <= 4000000:
				if side not in beacons and side not in sensors:
					not_in_range = 0
					for s in sensors:
						if (abs(side[0] - s.x) + abs(side[1] - s.y)) > s.distance:
							not_in_range += 1
					if not_in_range == len(sensors):
						print("Gold:", side[0] * 4000000 + side[1])
						exit()
