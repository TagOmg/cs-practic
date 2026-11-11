import json

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

        otvet[id.strip()] = lol[0].strip()
        otvet[city.strip()] = lol[1].strip()

        lst2.append(otvet)

    return lst2

def parse_settings(lines):
    otvet = {}
    for x in lines:
        if '#' in x:
            x = x[:x.index('#')].strip()
        if ": " in x:
            lol = x.split(': ')      
            try:
                key = lol[0].strip()
                value = lol[1].strip()
                if "." in lol[1]:
                    otvet[key] = float(value)  
                else:
                    otvet[key] = int(value)  

            except ValueError:

                if 'true' in value or 'yes' in value:
                    otvet[key] = True
                elif 'false' in value or 'no' in value:
                    otvet[key] = False
                else:
                    otvet[key] = value

        elif ":" in x:
            otvet[x[:-1].strip()] = []  
        elif len(x) != 0:
            otvet[next(reversed(otvet))].append(x[4:].strip())
    return otvet

def merge_by_key(rows, extra, key):
    extra_key = next(iter(extra))
    for dic in rows:
        if dic.get(key) == extra_key and next(iter(extra[extra_key])) not in dic :
            dic.update(extra[extra_key])
    return rows



def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)

print(
records_to_json([{"б": 2, "а": 1, 'я':3}]))
