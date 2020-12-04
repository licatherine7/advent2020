#!/usr/bin/python
arr = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.replace('\n', '')
        arr.append(int(line))

#  find two entries in array that sum to 2020
def part1(array, target):
    for entry in array:
        arg = target - entry
        if arg in array:
            return arg, entry

# find three entries in array that sum to 2020  
def part2(arr, length, target): 
    for i in range(length - 1): 
        s = {} 
        for j in range(i + 1, length): 
            x = target - (arr[i] + arr[j]) 
            if x in s.keys(): 
                return x, arr[i], arr[j]
            else: 
                s[arr[j]] = 1
          
print(part1(arr, 2020))
print(part2(arr, len(arr), 2020))
