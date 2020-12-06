import re
filename = "day4input.txt"

with open(filename) as f:
    inputarray = [line.rstrip() for line in f]


def passportList():
    passports = []
    passport = ""
    for line in inputarray:
        if (line == ""):
            passports.append(passport)
            passport = ""
        else:
            passport += line + " "
    passports.append(passport)
    return passports


def containsRequiredFields(passport):
    byr = passport.find("byr:") != -1
    iyr = passport.find("iyr:") != -1
    eyr = passport.find("eyr:") != -1
    hgt = passport.find("hgt:") != -1
    hcl = passport.find("hcl:") != -1
    ecl = passport.find("ecl:") != -1
    pid = passport.find("pid:") != -1
    return byr and iyr and eyr and hgt and hcl and ecl and pid


def getValue(passport, field):
    fieldIndex = passport.find(field + ":")
    value = passport[fieldIndex+4::].split(" ")[0]
    return value


def validateByr(byr):
    return byr >= 1920 and byr <= 2002


def validateIyr(iyr):
    return iyr >= 2010 and iyr <= 2020


def validateEyr(eyr):
    return eyr >= 2020 and eyr <= 2030


def validateHgt(hgt):
    if ("cm" in hgt):
        value = int(hgt[:-2])
        return value >= 150 and value <= 193
    if ("in" in hgt):
        value = int(hgt[:-2])
        return value >= 59 and value <= 76


def validateHcl(hcl):
    pattern = re.compile("#[a-f0-9]{6}$")
    return pattern.search(hcl)


def validateEcl(ecl):
    validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in validEcl


def validatePid(pid):
    pattern = re.compile("[0-9]{9}")
    return len(pid) == 9 and pattern.search(pid)


def isValid(passport):
    if (not containsRequiredFields(passport)):
        return False
    byr = int(getValue(passport, "byr"))
    iyr = int(getValue(passport, "iyr"))
    eyr = int(getValue(passport, "eyr"))
    hgt = getValue(passport, "hgt")
    hcl = getValue(passport, "hcl")
    ecl = getValue(passport, "ecl")
    pid = getValue(passport, "pid")
    return (validateByr(byr) and
            validateIyr(iyr) and
            validateEyr(eyr) and
            validateHgt(hgt) and
            validateHcl(hcl) and
            validateEcl(ecl) and
            validatePid(pid))


def task1():
    passports = passportList()
    validPassports = 0
    for passport in passports:
        if (containsRequiredFields(passport)):
            validPassports += 1
    return validPassports


def task2():
    passports = passportList()
    validPassports = 0
    for passport in passports:
        if (isValid(passport)):
            validPassports += 1
    return validPassports


print("Task 1 result: ", task1())
print("Task 2 result: ", task2())
