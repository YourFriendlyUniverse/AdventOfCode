with open('2025/input.txt', 'r') as file:
    fresh_idxs = []
    total_fresh = 0

    for line in file:
        line = line.strip()
        if '-' in line:
            first, last = list(map(int, line.split("-")))
            fresh_idxs.append([first, last])
        elif line != "":
            fresh = False
            for idx_range in fresh_idxs:
                if idx_range[0] <= int(line) <= idx_range[1]:
                    fresh = True
            if fresh:
                total_fresh += 1

print(f"Part 1: {total_fresh}")