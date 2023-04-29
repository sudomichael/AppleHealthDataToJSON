import os

input_directory = 'data/mocks'
output_file = 'data/index.js'

files = [f for f in os.listdir(input_directory) if f.endswith('.js')]

with open(output_file, 'w') as outfile:
    # Write import statements
    for file in files:
        file_name = os.path.splitext(file)[0]
        outfile.write(f'import {file_name} from "./{file}";\n')

    # Write default export statement with all objects
    outfile.write('\nexport default {\n')
    for file in files:
        file_name = os.path.splitext(file)[0]
        outfile.write(f'    {file_name},\n')
    outfile.write('};\n')
