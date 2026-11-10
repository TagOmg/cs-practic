paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

def count_by_extension(paths: list[str]) -> dict[str, int]:
    exts = [(p.split("/")[-1].split(".")[-1].lower() if "." in p.split("/")[-1] else "") for p in paths]
    return {e: exts.count(e) for e in exts}


def deepest_path(paths: list[str]) -> str:
    return min(paths, key=lambda p: (-p.count("/"), p)) if paths else ""


def human_size(n_bytes: int) -> str:
    for u in ["Б", "КБ", "МБ", "ГБ", "ТБ"]:
        if n_bytes < 1024 or u == "ТБ":
            return f"{n_bytes} Б" if u == "Б" else f"{n_bytes:.1f} {u}"
        n_bytes /= 1024
