import pandas as pd

#Read file into list, stripping '\n'
lines = []
with open(r"C:\Users\clare\Advent-of-code-2023\Day1\input.txt", 'r') as itemlist:
    for item in itemlist:               
        lines.append(item.strip('\n'))      

# Part 1

# Get first calibration value
def get_first_value(string):
    for s in string:
        if s in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return s

# Get last calibration value
def get_last_value(string):
    for s in string[::-1]:
        if s in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return s

def get_calibration_total_pt1(lines):
    total = 0
    for line in lines:
        num = get_first_value(line) + get_last_value(line)
        total = total + int(num)
    return total

print(f"Part 1 solution: {get_calibration_total_pt1(lines)}")

# Part 2

# define list of number strings
numbers = ['1', 'one', '2', 'two', '3', 'three', '4', 'four', '5', 'five', '6', 'six', '7', 'seven', '8', 'eight', '9', 'nine']

def find_first_number(string, numbers): 
    lowest_index = len(string) + 1
    
    for number in numbers: 
        index = string.find(number)
        if index != -1 and index < lowest_index:
            lowest_index = index
            first_number = number      
    return first_number

def find_last_number(string, numbers):
    lowest_index = len(string) + 1
    string = string[::-1]
    
    for number in numbers:
        number_reversed = number[::-1]
        
        index = string.find(number_reversed)
        
        if index != -1 and index < lowest_index:
            lowest_index = index
            last_number = number
            
    return last_number 

def convert_to_digit(number):
    num_dict = {'one': '1',
                'two': '2',
                'three': '3',
                'four' : '4', 
                'five' : '5', 
                'six' : '6', 
                'seven' : '7',
                'eight' : '8', 
                'nine' : '9', 
                'zero' : '0',
                }
    if number in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return number
    else:
        return num_dict[number]

def get_calibration_total_pt2(lines, numbers):
    total = 0
    for line in lines:
        num1 = convert_to_digit(find_first_number(line, numbers))
        num2 = convert_to_digit(find_last_number(line, numbers))
        total = total + int(num1)*10 + int(num2)
    return total

print(f"Part 2 solution: {get_calibration_total_pt2(lines, numbers)}")
