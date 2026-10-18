levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

file_name = input("Введите имя файла: ")

with open(file_name, 'r' ,encoding='utf-8') as lines, \
     open('report.txt','w', encoding='utf-8') as output:

    count_line = 0
    count_error = 0
    count_bad = 0

    
    for line in lines:
        line = line.rstrip().split(maxsplit = 2)
        count_line +=1
        if 'ERROR' in line:
            count_error += 1
        elif line[1] not in levels:
            count_bad += 1
    output_data = f"""Ввод:              Вывод:
{file_name:<19}{count_line}
{count_error:>20}
{count_bad:>20}
"""
    output.write(output_data)