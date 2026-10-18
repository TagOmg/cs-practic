levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

def parse_event(line):
        line = line.rstrip().split(maxsplit = 2)
        
        if line[1] not in levels:
             raise ValueError('Нет уровня или неизвестный уровень')
        
        return dict(time = line[0], level = line[1], message = line[2])



def count_levels(lines):  
        level_counts = dict(DEBUG = 0, INFO = 0, WARNING = 0, ERROR = 0, BROKEN = 0)

        for line in lines:
            if len(line) != 0:
                try:
                    match parse_event(line):
                        case {'level': lvl} if lvl in levels:
                            level_counts[lvl] +=1
                except ValueError:
                    level_counts['BROKEN'] +=1
                    continue

        return dict(sorted(level_counts.items()))

def top_errors(lines,n):
    errors = []

    for line in lines:
        if len(line) != 0:
            try:
                new_line =  parse_event(line)
                match new_line:
                    case {'level': lvl} if lvl == 'ERROR':
                        errors.append(new_line)
            except ValueError:
                continue

    errors.sort(key=lambda x: x["message"])

    lst_tuple = []
    count = 0

    for index,message in enumerate(errors):
        if index+1 < len(errors) and message['message'] == errors[index+1]['message']:
            count +=1
        else:
             lst_tuple.append((message['message'], count+1))
             count = 0

    lst_tuple.sort(key=lambda x: x[1],reverse=True)

    return lst_tuple[:n]

def format_report(count,errors):
    result = ''
    lst = []

    lst.append("Отчет по журналу\n\n")

    for line in tuple(count.items()):
        lst.append(f'{line[0]}: {line[1]}\n')

    lst.append("\nЧастые ошибки:\n")

    for error in errors:
        lst.append(f'- {error[0]} — {error[1]}\n')

    result = ''.join(lst)

    return result
