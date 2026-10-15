import sys

def parse_record(lines):
    line = lines.split(';')
    if len(line) != 3:
        raise ValueError('Недостаточно данных')
    elif line[0] == '' or line[2] == '':
        raise ValueError('Недостаточно данных')
    else:
        try:
            return dict(city = line[0], temp = float(line[1]), date = line[2])
        except ValueError:
            raise ValueError('Температура записана не числом')


def read_valid():
    inf = []
    for lines in sys.stdin.read().splitlines():
        try:
            inf.append(parse_record(lines))
        except ValueError:
            pass
    return inf

def average_by_city(inf):
    average = 0
    for city in inf:
        average += city.get('temp')
    return round(average/len(inf), 1)

def warmest_city(inf):
    inf.sort(key=lambda x: x['city'])
    return max(inf, key=lambda x: x['temp'])['city']
print(warmest_city(read_valid()))
