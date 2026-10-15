import sys
from stats import average_by_city, read_valid, warmest_city
lines = sys.stdin.read().splitlines()
valid_lines = read_valid(lines)
print(len(lines),len(lines) - len(valid_lines),average_by_city(valid_lines)[warmest_city(valid_lines)], sep ='\n')