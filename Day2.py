import re

#Read file into list, stripping '\n'
lines = []
with open(r"C:\Users\clare\Advent-of-code-2023\Day2\input.txt", 'r') as itemlist:
    for item in itemlist:               
        lines.append(item.strip('\n'))     

# Part 1

#Get the game number from each line
def get_game_number(txt):
    return re.findall("Game (\d+):", txt)

#Get the max of a given colour
def get_colour_max(colour, txt):
    x = re.findall(f"(\d+) {colour}", txt)
    x = list(map(int, x))
    return max(x)

#Put it all together
def get_game_total(lines):
    game_total = 0
    for line in lines: 
        #Get game number
        game_number = get_game_number(line)
        
        #Define dictionary of totals
        totals_dict = {'blue': 0,
                       'red': 0,
                       'green': 0
                      }
        #Get totals for each colour
        for colour in totals_dict:
            totals_dict[colour] = get_colour_max(colour, line)
    
        #If blues <= 14, reds <= 12, greens <= 13, add game number to total
        if (totals_dict['blue'] <= 14) and (totals_dict['red'] <= 12) and (totals_dict['green'] <= 13):
            game_total = game_total + int(game_number[0])
            
    return game_total

print(f"Part 1 solution: {get_game_total(lines)}")

# Part 2

def get_game_power(lines):
    power_total = 0
    for line in lines:         
        #Define dictionary of totals
        totals_dict = {'blue': 0,
                       'red': 0,
                       'green': 0
                      }
        #Get totals for each colour
        for colour in totals_dict:
            totals_dict[colour] = get_colour_max(colour, line)
            
        #Calculate game power
        power = totals_dict['blue'] * totals_dict['red'] * totals_dict['green']
        power_total = power_total + power
    
    return power_total

print(f"Part 2 solution: {get_game_power(lines)}")
