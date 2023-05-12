import xml.etree.ElementTree as ET
import json
import argparse
from datetime import datetime

# Parse command line arguments
parser = argparse.ArgumentParser(description='Convert export.xml to JSON and filter by creationDate')
parser.add_argument('--startDate', required=False)
parser.add_argument('--endDate', required=False)
args = parser.parse_args()

# Convert date strings to datetime objects if provided
start_date = datetime.strptime(args.startDate, '%Y-%m-%d').date() if args.startDate else None
end_date = datetime.strptime(args.endDate, '%Y-%m-%d').date() if args.endDate else None

file_path = 'export.xml'

def parse_element(element):
    result = {}
    for key, value in element.attrib.items():
        result[key] = value
    for child in element:
        result[child.tag] = parse_element(child)
    return result

with open(file_path, 'r') as file:
    tree = ET.parse(file)
    root = tree.getroot()

    json_data = {}
    for child in root:
        if start_date and end_date:
            parsed_child = parse_element(child)
            creation_date_str = parsed_child.get('creationDate')
            if creation_date_str:
                try:
                    creation_date = datetime.strptime(creation_date_str, '%Y-%m-%d %H:%M:%S %z').date()
                except ValueError:
                    print(f"Warning: Skipping element with invalid creationDate: {creation_date_str}")
                    print(parsed_child)
                    continue

                # Check if creationDate is between startDate and endDate
                if start_date <= creation_date <= end_date:
                    if child.tag not in json_data:
                        json_data[child.tag] = []
                    json_data[child.tag].append(parsed_child)
            else:
                if child.tag not in json_data:
                    json_data[child.tag] = []
                    json_data[child.tag].append(parsed_child)
        else:
            if child.tag not in json_data:
                json_data[child.tag] = []
            json_data[child.tag].append(parse_element(child))

    json_output = json.dumps(json_data, indent=2)

    with open('output.json', 'w') as json_file:
        json_file.write(json_output)
