# This file converts the ungrouped json list to a grouped json dictionary.

import json

# Read input data from "output.json" file
with open("output.json", "r") as input_file:
    data = json.load(input_file)

records = data.get("Record", [])

grouped_data = {}

for record in records:
    record_type = record.get("type")
    if record_type not in grouped_data:
        grouped_data[record_type] = []
    grouped_data[record_type].append(record)

# Write the grouped data to "groupedData.json" file
with open("groupedData.json", "w") as output_file:
    json.dump(grouped_data, output_file, indent=2)