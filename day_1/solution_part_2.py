from collections import Counter
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

similarity_score = 0

for num in sorted_left_list:
    similarity_score += num * sorted_right_list.count(num)
    

print(f"Similarity Score is: {similarity_score}")
