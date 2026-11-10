



def csv_to_records(text):
    otvet = {}
    lst = []
    lst2 = []

    lst = text.split('\n')
    id,city = lst[:1][0].split(',')

    del lst[:1]
    
    for x in lst[:-1]:
        lol = x.split(",")

        otvet[id] = lol[0]
        otvet[city] = lol[1]

        lst2.append(otvet)

    return lst2



def parse_settings(lines):
    otvet = {}
    for x in lines:
        if '#' in x:
            x = x[:x.index('#')]

        elif ": " in x:
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
        else:
            otvet[next(reversed(otvet))].append(x[4:])
    print(otvet)


def merge_by_key(rows, extra, key):
    pass
def records_to_json(records):
    pass