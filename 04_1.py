with open("input/04.txt", "r") as f:
    passports = [" ".join(group.split("\n")).strip() for group in f.read().split("\n\n")]

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def valid_passport(passport: str) -> bool:
    fields = set(fv.split(":")[0] for fv in passport.split())
    return required_fields.issubset(fields)


print(sum(valid_passport(p) for p in passports))
