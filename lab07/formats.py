



def csv_to_records(text):
    
    lst = []
    lst2 = []
    if len(text) != 0:
        lst = text.split('\n')
        id,city = lst[:1][0].split(',')
        del lst[:1]
    
    for x in lst[:-1]:
        otvet = {}
        lol = x.split(",")

        otvet[id] = lol[0].strip()
        otvet[city] = lol[1].strip()

        lst2.append(otvet)

    return lst2


def parse_settings(lines):
    otvet = {}
    for x in lines:
        if '#' in x:
            x = x[:x.index('#')]
            print(x)
        if ": " in x:
            lol = x.split(': ')      
            try:

                if "." in lol[1]:
                    otvet[lol[0]] = float(lol[1])  
                else:
                    otvet[lol[0]] = int(lol[1])  

            except ValueError:

                if 'true' in lol[1] or 'yes' in lol[1]:
                    otvet[lol[0]] = True
                elif 'false' in lol[1] or 'no' in lol[1]:
                    otvet[lol[0]] = False
                else:
                    otvet[lol[0]] = lol[1]

        elif ":" in x:
            otvet[x[:-1]] = []  
        elif len(x) != 0:
            otvet[next(reversed(otvet))].append(x[4:])
        print(x)
    return otvet

print(parse_settings(["title: Отчёт за март","lol: svo #svo", "decimals: 1", "active: true",
                "columns:", "  - город", "  - цена"]))

def merge_by_key(rows, extra, key):
    pass
def records_to_json(records):
    pass