def get_updates(item_list):
    updates = [list(map(int, item.split(','))) for item in item_list if ',' in item]
    return updates

def get_rules(item_list):
    rules = [tuple(map(int, item.split('|'))) for item in item_list if '|' in item]
    return rules

def is_valid(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def check_updates(updates, rules):
    good_updates = []
    middle_numbers_added = 0

    for update in updates:
        if is_valid(update, rules):
            good_updates.append(update)
            middle_index = len(update) // 2
            middle_numbers_added += update[middle_index]

    return good_updates, middle_numbers_added

with open('day_5/input.txt') as f:
    mixed = [line.strip() for line in f.readlines()]

rules = get_rules(mixed)
updates = get_updates(mixed)

good_updates, middle_numbers_added = check_updates(updates, rules)

print(f"Valid updates = {len(good_updates)}\nMiddle numbers added up = {middle_numbers_added}")



