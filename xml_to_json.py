### This file converts the export.xml file to a json file.

import xml.etree.ElementTree as ET
import json

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
        if child.tag not in json_data:
            json_data[child.tag] = []
        json_data[child.tag].append(parse_element(child))

    json_output = json.dumps(json_data, indent=2)

    with open('output.json', 'w') as json_file:
        json_file.write(json_output)
