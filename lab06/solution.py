paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]
extensions_dict = {}
lst = [     ]

def count_by_extension(paths):
    for path  in paths:
        extension = path.split('/')[-1].split('.')[-1].lower()
        if '.' not in path.split('/')[-1]:
            extension = ''
        elif path.split('/')[-1][0] == '.':
             extension = ''
        extensions_dict.setdefault(extension, 0)
        if extension in extensions_dict:
            extensions_dict[extension] += 1
    return extensions_dict


def deepest_path(paths):
    paths.sort()
    for x in paths:
        lst.append(x.count('/'))
    return paths[lst.index(max(lst))] if len(paths) else ''

def human_size(n_bytes: float) -> str:
    for unit in ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']:
        if n_bytes < 1024 and unit == 'Б':
           return f"{int(n_bytes)} {unit}" 
        elif n_bytes < 1024 or unit == 'ТБ':
            return f"{n_bytes:.1f} {unit}"
        n_bytes /= 1024