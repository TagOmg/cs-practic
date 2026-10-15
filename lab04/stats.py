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


def read_valid(lines):
    inf = []
    for line in lines:
        try:
            inf.append(parse_record(line))
        except ValueError:
            count += 1
    return inf

def average_by_city(inf):
    average_cities_temp = dict()
    for record in inf:
        average_cities_temp.setdefault(record["city"], []).append(record['temp'])
    for city in average_cities_temp:
        average_temp = sum(average_cities_temp[city])/len(average_cities_temp[city])
        average_cities_temp[city] = average_temp
    return average_cities_temp

def warmest_city(inf):
    inf.sort(key=lambda x: x['city'])
    return max(inf, key=lambda x: x['temp'])['city']
