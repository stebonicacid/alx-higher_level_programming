#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import json
import sys

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return []

args = sys.argv[1:]
items = load_from_json_file('add_item.json')
items += args
save_to_json_file(items, 'add_item.json')
