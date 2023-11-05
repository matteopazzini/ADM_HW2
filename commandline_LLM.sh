#!/bin/bash

# Set the JSON file path
json_file="series.json"

# Check if jq is installed
jq -e . "$json_file" >/dev/null 2>&1 || { echo "Error: jq is not installed or the JSON file is invalid."; exit 1; }

# Process the JSON file
time jq -r '. | {id, title, total_books_count: [.works[]| (.books_count | tonumber)] | add}' "$json_file" | jq -s 'sort_by(-.total_books_count) | .[:5] | .[] | "ID:\(.id) | TITLE:\(.title) | TOTAL_BOOKS_COUNT:\(.total_books_count)"'
