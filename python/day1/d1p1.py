left_arr = []
right_arr = []

with open('python\day1\input.txt', 'r', encoding="utf-8") as file:
    for line in file.readlines():
        left, right = line.split()
        left_arr.append(int(left))
        right_arr.append(int(right))

distance_sum = sum([abs(left - right) for (left, right) in zip(sorted(left_arr), sorted(right_arr))])
print(distance_sum)
