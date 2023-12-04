import re

#Read file into list
lines = []
with open(r"C:\Users\clare\Advent-of-code-2023\Day4\input.txt", 'r') as itemlist:
    for item in itemlist:               
        lines.append(item)

# Part 1

#Get list of card numbers from line using regex
def get_card_nums(line):
    x = re.findall("(?<=\:\s)(.*?)(?=\s\|)", line)
    return x[0].split()

#Get list of guesses from line 1
def get_guesses(line):
    guesses = re.findall("(?<=\|\s)(.*?)(?=\n)", line)
    return guesses[0].split()

#Get count of matches
def get_match_count(nums,guesses):
    count = 0
    for n in guesses: 
        if n in nums: 
            count = count + 1
    return count

def get_points(count):
    if count > 0:
        points = 1
        for i in range(0,count-1):
            points = points * 2
    else:
        points = 0
    return points

#Put it all together
def get_point_total(lines):
    point_total = 0
    for line in lines: 
        nums = get_card_nums(line)
        guesses = get_guesses(line)        
        count = get_match_count(nums, guesses)
        points = get_points(count)
        point_total = point_total + points
    return point_total

print(f"Part 1 solution: {get_point_total(lines)}")

# Part 2

#Get number of matches
def get_matches(card_num, lines):
    line = lines[card_num-1]
    nums = get_card_nums(line)
    guesses = get_guesses(line)
    count = get_match_count(nums,guesses)
    return count

#Get dictionary of card count
def get_card_dict(length):
    dict_cards = {1: 1}

    for i in range(1, length):
        dict_cards[i+1] = 1
    return dict_cards

#Get dictionary of card matches
def get_card_matches(lines):
    dict_matches = {1: 0}
    
    for i in range(0, len(lines)):
        dict_matches[i+1] = get_matches(i+1, lines)
    return dict_matches

#Increment card count dictionary given a card number according to its number of matches
def increase_card_count(card_num, dict_cards, dict_matches):
    num_matches = dict_matches[card_num]
    
    if num_matches > 0: 
        for i in range(1, num_matches+1):
            dict_cards[card_num + i] =  dict_cards[card_num + i] + 1
    return dict_cards

def get_total_card_count(dict_cards):
    total = 0
    for i in range(1, len(dict_cards)+1):
        total = total + dict_cards[i]
    return total

#Put it all together
def get_number_of_cards(lines):
    length = len(lines)
    dict_cards = get_card_dict(length)
    dict_matches = get_card_matches(lines)
    
    for i in range(1, length + 1):
        for j in range(0, dict_cards[i]):
            dict_cards = increase_card_count(i, dict_cards, dict_matches)
    return get_total_card_count(dict_cards)

print(f"Part 2 solution: {get_number_of_cards(lines)}")
