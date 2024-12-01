left_arr = []
right_map = {}

with open('AOC-2024\python\day1\input.txt', 'r', encoding="utf-8") as file:
    for line in file.readlines():
        left, right = line.split()
        left_arr.append(int(left))
        right = int(right)
        if right in right_map:
            right_map[right] += 1
        else:
            right_map[right] = 1

similarity_score = sum([left * right_map[left] for left in left_arr if left in right_map])
print(similarity_score)
