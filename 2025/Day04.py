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
        

with open('2025/input.txt', 'r') as file:
    lines = [line.strip() for line in file]
    total_accessible = 0
    
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if can_access(x, y, lines):
                total_accessible += 1
print(total_accessible)