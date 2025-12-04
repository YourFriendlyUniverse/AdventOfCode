def part_one(first: int, last: int):
    invalid_in_range = 0
    for i in range(last - first + 1):
        num = first + i
        mid = len(str(num)) // 2
        if (len(str(num)) % 2 == 0 and str(num)[:mid] == str(num)[mid:]):
            invalid_in_range += num
    return invalid_in_range

def part_two(first: int, last: int):
    invalid_in_range = 0
    for i in range(last - first + 1):
        num = first + i
        for split_idx in range(1, len(str(num)) // 2 + 1, 1):
            substrings = []
            matching = True
            for j in range(0, len(str(num)), split_idx):
                substrings.append(str(num)[j:j+split_idx])
            for idx in range((len(substrings) - 1)):
                if substrings[idx] != substrings[idx + 1]:
                    matching = False
            if matching:
                invalid_in_range += num
                break
    return invalid_in_range

with open('2025/input.txt', 'r') as file:
    total_part_one = 0
    total_part_two = 0
    id_ranges = file.readline().split(",")
    for id_range in id_ranges:
        first, last = id_range.split("-")
        total_part_one += part_one(int(first), int(last))
        total_part_two += part_two(int(first), int(last))

print(f"Part 1: {total_part_one}")
print(f"Part 2: {total_part_two}")