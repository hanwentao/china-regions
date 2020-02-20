#!/usr/bin/env python3

import json
import textwrap

def is_subregion(small_code, large_code):
    small_pieces = textwrap.wrap(small_code, 2)
    large_pieces = textwrap.wrap(large_code, 2)
    for small_piece, large_piece in zip(small_pieces, large_pieces):
        if not (large_piece == '00' or small_piece == large_piece):
            return False
    return True

def add_place(regions, code, name):
    if isinstance(regions, list):
        for region in regions:
            if is_subregion(code, region['code']):
                add_place(region, code, name)
                return
        regions.append({'code': code, 'name': name})
    else:  # regions is a dict
        region = regions
        subregions = region.setdefault('subregions', [])
        add_place(subregions, code, name)

places = {}
with open('data/places.txt') as places_file:
    for line in places_file:
        line = line.strip()
        if len(line) > 6 and line[:6].isdigit():
            code, name = line.split()
            places[code] = name
regions = []
for code, name in sorted(places.items()):
    add_place(regions, code, name)
with open('data/regions.json', 'w') as regions_file:
    json.dump(regions, regions_file, ensure_ascii=False, indent=2)
