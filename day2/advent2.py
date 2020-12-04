#!/usr/bin/python3

arr = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.replace('\n', '')
        line = line.replace(':', '')
        arr.append(line)

#part 1
def count_valid_passwords():
    count = 0
    for line in arr:
        line = line.split(" ")
        # index 0: range of occurrences
        # index 1: required letter
        # index 2: given password
        policy = line[0]
        target_char = line[1]
        password = line[2]

        char_range = parse_policy(policy)
        char_count = password.count(target_char)
        if char_count in range(int(char_range[0]), int(char_range[1])+1):
            count = count + 1
    
    print(count)

def parse_policy(line):
    return line.split('-')

# part 2
def more_valid_passwords():
    count = 0
    for line in arr:
        line = line.split(" ")
        # index 0: range of occurrences
        # index 1: required letter
        # index 2: given password
        policy = line[0]
        target_char = line[1]
        password = line[2]

        char_range = parse_policy(policy)

        if password[int(char_range[0]) - 1] == target_char and password[int(char_range[1]) - 1] == target_char:
            pass
        elif password[int(char_range[0]) - 1] == target_char and password[int(char_range[1]) - 1] != target_char:
            count = count + 1
        elif password[int(char_range[0]) - 1] != target_char and password[int(char_range[1]) - 1] == target_char:
            count = count + 1
    
    print(count)



count_valid_passwords()
more_valid_passwords()