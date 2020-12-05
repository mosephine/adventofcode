#! /usr/bin/python

import re
import sys

lines = [line.rstrip('\n').split(' ') for line in open(sys.argv[1])]

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
fields_optional = {"cid"}

passports = []
passport = []
for line in lines:
    if line[0] == '':
        passports.append(passport)
        passport = []
        continue
    for item in line:
        passport.append(item.split(":"))
passports.append(passport)

passports_valid = []
for passport in passports:
    tmp_passport = set()
    for field in passport:
        tmp_passport.add(field[0])
    if tmp_passport == fields or (fields - tmp_passport) == fields_optional:
        passports_valid.append(passport)

print("(Day 4, Part 1) number of valid passports: " + str(len(passports_valid)))

hgt_re = re.compile("(\d+)(cm|in)")
hcl_re = re.compile("#[0-9a-f]{6}")
ecl_re = re.compile("(amb|blu|brn|gry|grn|hzl|oth)")
pid_re = re.compile("^[\d]{9}$")

count_valid = 0
for passport in passports_valid:
    valid = True
    for field in passport:
        if field[0] == "byr":
            if int(field[1]) < 1920 or int(field[1]) > 2002:
                valid = False
                break

        if field[0] == "iyr":
            if int(field[1]) < 2010 or int(field[1]) > 2020:
                valid = False
                break

        if field[0] == "eyr":
            if int(field[1]) < 2020 or int(field[1]) > 2030:
                valid = False
                break

        if field[0] == "hgt":
            match_hgt = hgt_re.search(field[1])
            if match_hgt:
                val = int(match_hgt.group(1))
                units = match_hgt.group(2)
                if units == "cm" and (val < 150 or val > 193):
                    valid = False
                    break
                if units == "in" and (val < 59 or val > 76):
                    valid = False
                    break
            else:
                valid = False
                break


        if field[0] == "hcl":
            match_hcl = hcl_re.search(field[1])
            if not match_hcl:
                valid = False
                break

        if field[0] == "ecl":
            match_ecl = ecl_re.search(field[1])
            if not match_ecl:
                valid = False
                break

        if field[0] == "pid":
            match_pid = pid_re.search(field[1])
            if not match_pid:
                valid = False
                break
            print(field[1])

    if valid:
        count_valid += 1

print("(Day 4, Part 2) number of valid passwords with valid field values: " + str(count_valid))





