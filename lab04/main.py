import sys
from stats import average_by_city, read_valid, warmest_city
lines = sys.stdin.read().splitlines()
valid_lines = read_valid(lines)
null_lines = lines.count('')
print(len(valid_lines),len(lines) - len(valid_lines)- null_lines,average_by_city(valid_lines)[warmest_city(valid_lines)], sep ='\n')