import sys
import subprocess

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

# Check if 'json' is passed as an argument
use_json_commands = len(sys.argv) > 1 and sys.argv[1] == '--json'

commands = json_commands if use_json_commands else default_commands

for command in commands:
    process = subprocess.Popen(command, shell=True)
    process.wait()
