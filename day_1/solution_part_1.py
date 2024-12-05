
with open('day_1/input.txt', 'r')as f:
    file = f.read()


temp = file.strip() 
temp = temp.replace('\n', '   ')

mixed_list = temp.split('   ')

left_list = []
right_list = []

for idx, item in enumerate(mixed_list):
    if idx%2 == 0:
        left_list.append(int(item))
    else:
        right_list.append(int(item))

sorted_left_list = sorted(left_list)
sorted_right_list = sorted(right_list)

total_distance = 0

while sorted_right_list:
    distance = abs(sorted_left_list[-1] - sorted_right_list[-1])
    total_distance += distance
    sorted_left_list.pop()
    sorted_right_list.pop()

print(f"Total_distance is: {total_distance}")

    

