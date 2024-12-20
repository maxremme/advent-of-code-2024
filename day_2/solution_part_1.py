
def is_safe(levels):
    levels = [int(x) for x in levels.split(' ')]
    is_ascending = True
    is_descending = True

    for i in range(len(levels)-1):
        difference = abs(levels[i+1]-levels[i])
        if difference < 1 or difference > 3:
            return False

        if levels[i] <= levels[i+1]:
            is_descending = False
        if levels[i] >= levels[i+1]:
            is_ascending = False

    return is_ascending or is_descending

with open('day_2/input.txt', 'r')as f:
    file = f.readlines()
records = [record.strip() for record in file]

good_record_count = 0
records_checked = 0

for record in records:
    records_checked += 1
    if is_safe(record):
        good_record_count+=1

print(f"{records_checked} Records checked, Good records: {good_record_count}")
