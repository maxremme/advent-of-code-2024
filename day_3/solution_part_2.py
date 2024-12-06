import re

def parse_matches(matches):

    def parse_numbers(match):
        #extract numbers from matches
        num_1 = int(match[4:-1].split(',')[0])
        num_2 = int(match[4:-1].split(',')[1])
        return num_1, num_2

    do_multiply = True
    result = 0

    for match in matches:
        match = match[0]

        if match == "don't()":
            do_multiply = False
            continue
            
        elif match == 'do()':
            do_multiply = True
            continue
            

        if do_multiply:

            num_1 = parse_numbers(match)[0]
            num_2 = parse_numbers(match)[1]

            result += num_1*num_2

    return result
    

with open('day_3/input.txt', 'r') as f:
    file = f.read()
    
    # regex for mul(digits,digits) or for do() and don't() statements
    pattern = re.compile(r'mul\(\d*,\d*\)|do\(\)|don\'t\(\)')
    mul_matches = pattern.finditer(file)


print(f"Result is: {parse_matches(mul_matches)}")