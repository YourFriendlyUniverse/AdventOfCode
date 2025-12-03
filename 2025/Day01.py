with open('input.txt', 'r') as file:
    pos = 50
    password1 = 0
    password2 = 0
    for line in file:
        offset = int(line[1:])
        if line[0] == "L":
            prev_pos = pos
            pos -= offset
            if (prev_pos != 0 and pos < 0):
                password2 += 1
        else:
            pos += offset
            if (pos - (offset // 100) * 100 > 100):
                password2 += 1
        password2 += offset // 100
        pos %= 100
        if pos == 0:
            password1 += 1

    password2 += password1

print(f"Part 1: {password1}")
#TODO Part 2 is currently broken
print(f"Part 2: {password2}")