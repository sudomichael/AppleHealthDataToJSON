import sys
import subprocess
import argparse

default_commands = [
    "python3 xml_to_json.py",
    "python3 ungrouped_to_grouped_json.py",
    "python3 json_to_js.py",
    "python3 clean_file_names.py"
]

json_commands = [
    "python3 xml_to_json.py",
    "python3 ungrouped_to_grouped_json.py",
    "python3 grouped_json_to_individual_json.py",
    "python3 clean_file_names.py",
    "python3 combine_exports.py"
]

parser = argparse.ArgumentParser(description='Convert export.xml to JSON and filter by creationDate')
parser.add_argument('--json', action='store_true', help='Use JSON commands')
parser.add_argument('--startDate', help='Start date in the format YYYY-MM-DD')
parser.add_argument('--endDate', help='End date in the format YYYY-MM-DD')
args = parser.parse_args()

commands = json_commands if args.json else default_commands

# Extract the startDate and endDate from the arguments, if present
additional_args = []
if args.startDate:
    additional_args.append(f'--startDate={args.startDate}')
if args.endDate:
    additional_args.append(f'--endDate={args.endDate}')

additional_args_str = ' '.join(additional_args)

# Append the additional arguments to each command
commands = [f'{command} {additional_args_str}' for command in commands]

for command in commands:
    process = subprocess.Popen(command, shell=True)
    process.wait()
