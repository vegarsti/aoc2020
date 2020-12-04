from typing import Callable, Dict, List, Tuple, cast

with open("input/04.txt", "r") as f:
    passports = [" ".join(group.split("\n")).strip() for group in f.read().split("\n\n")]


def height_rule(s: str) -> bool:
    if len(s) < 4:
        return False
    num, cm_or_in = int(s[:-2]), s[-2:]
    if cm_or_in not in {"cm", "in"}:
        return False
    if cm_or_in == "cm":
        return 150 <= num <= 193
    return 59 <= num <= 76


def hair_color_rule(s: str) -> bool:
    if len(s) != 7:
        return False
    bang, color = s[0], s[1:]
    if bang != "#":
        return False
    return all(c in "0123456789abcdef" for c in color)


field_rules: List[Tuple[str, Callable[[str], bool]]] = [
    ("byr", lambda s: 1920 <= int(s) <= 2002),
    ("iyr", lambda s: 2010 <= int(s) <= 2020),
    ("eyr", lambda s: 2020 <= int(s) <= 2030),
    ("hgt", height_rule),
    ("hcl", hair_color_rule),
    ("ecl", lambda s: s in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}),
    ("pid", lambda s: len(s) == 9 and s.isdigit()),
]


def valid_passport(passport: str) -> bool:
    field_values: Dict[str, str] = dict(cast(Tuple[str, str], (tuple(fv.split(":")))) for fv in passport.split())
    for field, rule in field_rules:
        value = field_values.get(field)
        if value is None:
            return False
        if not rule(value):
            return False
    return True


print(sum(valid_passport(p) for p in passports))
