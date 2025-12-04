def can_access(x, y, grid):
    if grid[y][x] != '@':
        return False
    
    adjacent_papers = 0
    for y_diff in range(-1, 2):
        for x_diff in range(-1, 2):
            if (len(grid) > (y + y_diff) > -1 and len(grid[0]) > (x + x_diff) > -1):
                if not (x_diff == 0 and y_diff == 0):
                    if grid[y + y_diff][x + x_diff] == '@':
                        adjacent_papers += 1
    return (adjacent_papers < 4)

def accessible_papers(lines):
    list = []
    
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if can_access(x, y, lines):
                list.append([x, y])
    return list

with open('2025/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    total_accessible = accessible_papers(lines)
    new_papers = len(total_accessible)
    total_no_remove = len(total_accessible)
    total = total_no_remove

    while (new_papers != 0):
        for x, y in total_accessible:
            lines[y] = lines[y][:x] + "x" + lines[y][(x + 1):]
        total_accessible = accessible_papers(lines)
        new_papers = len(total_accessible)
        total += len(total_accessible)

print(f"Part 1: {total_no_remove}")
print(f"Part 2: {total}")