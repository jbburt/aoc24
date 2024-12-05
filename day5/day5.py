with open("day5/input.txt") as f:
    data = f.read()

rules, updates = data.split("\n\n")

# lists of [pageA which must be printed prior, pageB]
rules = [list(map(int, row.strip().split("|"))) for row in rules.strip().split("\n")]

# ordered lists of sequential page updates
updates = [
    [int(n) for n in row.strip().split(",")] for row in updates.strip().split("\n")
]

## P1

tot = 0
for upd in updates:
    valid = True
    for i, page in enumerate(upd):
        for j, pages_in_rule in enumerate(rules):
            if all((p in upd for p in pages_in_rule)):
                if (page == pages_in_rule[1]) and (pages_in_rule[0] not in upd[:i]):
                    valid = False
                    break
        if not valid:
            break
    if valid:
        tot += upd[len(upd) // 2]
print(tot)

## P2


def fix_invalid(sequence: list[int]) -> list[int]:
    for inum, num in enumerate(sequence):
        for rulepages in rules:
            if all((p in sequence for p in rulepages)):
                if (num == rulepages[1]) and (rulepages[0] not in sequence[:inum]):
                    # swap positions of the two pages in the rule
                    new_seq = sequence.copy()
                    k = new_seq.index(rulepages[0])
                    new_seq[inum] = rulepages[0]
                    new_seq[k] = rulepages[1]
                    return fix_invalid(new_seq)
    return sequence


tot = 0
for upd in updates:
    valid = True
    for i, page in enumerate(upd):
        for j, pages_in_rule in enumerate(rules):
            if all((p in upd for p in pages_in_rule)):
                if (page == pages_in_rule[1]) and (pages_in_rule[0] not in upd[:i]):
                    valid = False
                    break
        if not valid:
            break
    if not valid:
        valid_upd = fix_invalid(upd)
        tot += valid_upd[len(valid_upd) // 2]
print(tot)
