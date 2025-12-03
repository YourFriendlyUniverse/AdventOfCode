with open('input.txt', 'r') as file:
    joltage_output = 0
    for line in file:
        line = line.strip()
        first_digit_idx = 0
    
        for i in range(len(line) - 1):
            if int(line[i]) > int(line[first_digit_idx]):
                first_digit_idx = i

        second_digit_idx = first_digit_idx + 1

        for i in range(second_digit_idx, len(line)):
            if int(line[i]) > int(line[second_digit_idx]):
                second_digit_idx = i

        joltage_output += int(line[first_digit_idx] + line[second_digit_idx])
    
print (joltage_output)