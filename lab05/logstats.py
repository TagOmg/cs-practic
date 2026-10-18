levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

def parse_event(line):
        line = line.rstrip().split(maxsplit = 2)
        if line[1] not in levels:
             raise ValueError('Нет уровня или неизвестный уровень')
        return dict(time = line[0], level = line[1], message = line[2])



def count_levels(lines):  
    pass

def top_errors():
    pass

