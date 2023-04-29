# Converts the grouped JSON file in to individual javascript files for each group/record type

import json
import os

# Ensure the "data" directory exists, if not, create it
if not os.path.exists("data"):
    os.makedirs("data")
    
# Ensure the "data/mocks" directory exists, if not, create it
if not os.path.exists("data/mocks"):
    os.makedirs("data/mocks")

# Read grouped data from "groupedData.json" file
with open("groupedData.json", "r") as input_file:
    grouped_data = json.load(input_file)

# Iterate through each group
for record_type, records in grouped_data.items():
    # Create a JavaScript file within the "data/mocks" directory with the type as the file name
    file_name = f"{record_type}.js"
    file_path = os.path.join("data/mocks", file_name)

    # Write the content of the JavaScript file
    with open(file_path, "w") as output_file:
        output_file.write(f"export default ")
        json.dump(records, output_file, indent=2)
        output_file.write(";")
