input_lines = [l.strip() for l in open("old/2018_4.txt").readlines()]
input_lines.sort()

# Parse the input and create a dictionary of guard sleep times
guards = {}

for line in input_lines:
    # Extract the date, time, and action from the line
    date, time, action = line.split()[:3]
    date = date[1:]
    time = time[:-1]

    # If the action is the start of a shift, update the current guard
    if "Guard" in action:
        guard_id = line.split("#")[1].split()[0]
        if guard_id not in guards:
            guards[guard_id] = []

    # If the action is falling asleep or waking up, update the sleep times
    elif "falls" in action:
        sleep_start = int(time.split(":")[1])
    elif "wakes" in action:
        sleep_end = int(time.split(":")[1])
        guards[guard_id].extend(range(sleep_start, sleep_end))

# Find the guard that has the most minutes asleep
most_asleep_guard = None
most_asleep_minutes = 0

for guard, sleep_times in guards.items():
    # Calculate the total number of minutes slept
    total_sleep = len(sleep_times)

    # Update the most asleep guard if necessary
    if total_sleep > most_asleep_minutes:
        most_asleep_guard = guard
        most_asleep_minutes = total_sleep

# Find the minute that the most asleep guard spends asleep the most
minute_counts = [0] * 60

for minute in guards[most_asleep_guard]:
    minute_counts[minute] += 1

most_asleep_minute = minute_counts.index(max(minute_counts))

# Calculate and print the solution
solution = int(most_asleep_guard) * most_asleep_minute
print(
    f"The ID of the guard multiplied by the minute they spend asleep the most is {solution}.")

# Find the guard that is most frequently asleep on the same minute
most_frequent_guard = None
most_frequent_minute = None
most_frequent_count = 0

for guard, sleep_times in guards.items():
    # Count the number of times each minute appears in the sleep times
    minute_counts = [0] * 60
    for minute in sleep_times:
        minute_counts[minute] += 1

    # Find the minute with the highest count
    frequent_minute = minute_counts.index(max(minute_counts))
    frequent_count = max(minute_counts)

    # Update the most frequent guard and minute if necessary
    if frequent_count > most_frequent_count:
        most_frequent_guard = guard
        most_frequent_minute = frequent_minute
        most_frequent_count = frequent_count

# Calculate and print the solution
solution = int(most_frequent_guard) * most_frequent_minute
print(
    f"The ID of the guard multiplied by the minute they spend asleep the most is {solution}.")
