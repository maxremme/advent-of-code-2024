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
    bad_updates = []
    middle_numbers_added = 0

    for update in updates:
        if is_valid(update, rules):
            good_updates.append(update)
            middle_index = len(update) // 2
            middle_numbers_added += update[middle_index]
        else:
            bad_updates.append(update)

    return good_updates, bad_updates, middle_numbers_added

def fix_update(update, rules):
    """Sort an update to satisfy the rules using topological sorting."""
    from collections import defaultdict, deque

    # Build a graph from the rules
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    # Only consider rules involving pages in this update
    pages_set = set(update)
    for x, y in rules:
        if x in pages_set and y in pages_set:
            graph[x].add(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Perform topological sorting
    sorted_update = []
    queue = deque([page for page in update if in_degree[page] == 0])

    while queue:
        current = queue.popleft()
        sorted_update.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def fix_bad_updates(bad_updates, rules):
    fixed_updates = []
    middle_numbers_added = 0

    for update in bad_updates:
        fixed_update = fix_update(update, rules)
        fixed_updates.append(fixed_update)
        middle_index = len(fixed_update) // 2
        middle_numbers_added += fixed_update[middle_index]

    return fixed_updates, middle_numbers_added

with open('day_5/input.txt') as f:
    mixed = [line.strip() for line in f.readlines()]

rules = get_rules(mixed)
updates = get_updates(mixed)

good_updates, bad_updates, middle_numbers_added_good = check_updates(updates, rules)
fixed_updates, middle_numbers_added_fixed = fix_bad_updates(bad_updates, rules)

print(f"Valid updates = {len(good_updates)}\nMiddle numbers added up (valid) = {middle_numbers_added_good}")
print(f"Invalid updates fixed = {len(fixed_updates)}\nMiddle numbers added up (fixed) = {middle_numbers_added_fixed}")
