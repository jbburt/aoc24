import re

with open("day3/input.txt") as f:
    text = f.read()

pat = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pat, text, flags=re.DOTALL)
print(sum([int(a) * int(b) for (a, b) in matches]))

pat_subs = r"don\'t\(\).*?do\(\)"
matches = re.findall(pat_subs, text, flags=re.DOTALL)
for match in matches:
    text = text.replace(match, "")

matches = re.findall(pat, text, flags=re.DOTALL)
print(sum([int(a) * int(b) for (a, b) in matches]))
