import re

def parse_matches(matches):
    result = 0
    for match in matches:
        num_1 = int(match[0][4:-1].split(',')[0])
        num_2 = int(match[0][4:-1].split(',')[1])

        result += num_1*num_2
    return result
    

with open('day_3/input.txt', 'r') as f:
    file = f.read()


    pattern = re.compile(r'mul\(\d*,\d*\)')
    matches = pattern.finditer(file)

print(f"Result is: {parse_matches(matches)}")











