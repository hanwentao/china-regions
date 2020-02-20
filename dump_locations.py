#!/usr/bin/env python3

import json

def generate_locations(regions, prefix=''):
    for region in regions:
        if 'subregions' in region:
            yield from generate_locations(region['subregions'], prefix + region['name'])
        else:
            yield prefix + region['name']

with open('data/regions.json') as regions_file:
    regions = json.load(regions_file)
with open('data/locations.txt', 'w') as locations_file:
    for location in generate_locations(regions):
        locations_file.write(location + '\n')
