import sys

def parse_record():
    for lines in sys.stdin.read().splitlines():
        line = lines.split(';')
        if len(line) != 3:
            raise ValueError('Недостаточно данных')
        elif line[0] == '' or line[2] == '':
            raise ValueError('Недостаточно данных')
        else:
            try:
             city,temp,date = line[0],float(line[1]),line[2]
            except ValueError:
                raise ValueError('Температура записана не числом')
        