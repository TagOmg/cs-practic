levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

def parse_event(line):
        line = line.rstrip().split(maxsplit = 2)
        if line[1] not in levels:
             raise ValueError('Нет уровня или неизвестный уровень')
        return dict(time = line[0], level = line[1], message = line[2])



def count_levels(lines):  
        level_counts = dict(DEBUG = 0, INFO = 0, WARNING = 0, ERROR = 0, BROKEN = 0)
        for line in lines:
            try:
                new_level = parse_event(line)    
                print(new_level)                      
                match new_level:
                    case {'level': lvl} if lvl in levels:
                        level_counts[lvl] +=1
            except ValueError:
                level_counts['BROKEN'] +=1
                continue
        return level_counts

def top_errors():
    pass