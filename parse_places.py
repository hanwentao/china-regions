#!/usr/bin/env python3

import csv

def get_full_name(code, places):
    full_name = ''
    for pos in (4, 2, 0):
        if code[pos:pos + 2] != '00':
            full_name = places.get(code, '') + full_name
        code = code[:pos] + '00' + code[pos + 2:]
    assert code == '000000'
    return full_name

places = {}
with open('data/places.txt') as places_file:
    for line in places_file:
        line = line.strip()
        if len(line) > 6 and line[:6].isdigit():
            code, name = line.split()
            places[code] = name
with open('data/locations.csv', 'w') as locations_file:
    writer = csv.DictWriter(locations_file, ('code', 'name', 'full_name'))
    writer.writeheader()
    for code, name in sorted(places.items()):
        full_name = get_full_name(code, places)
        writer.writerow({
            'code': code,
            'name': name,
            'full_name': full_name,
        })
