# Updates file names to be more legible. 
# I.e, HKQuantityTypeIdentifierAppleStandTime.js -> StandTime.js

import os

data_directory = "data/mocks"

# Iterate through the files in the "data" directory
for filename in os.listdir(data_directory):
    new_filename = filename

    # If the file name starts with "HKQuantityTypeIdentifierApple", remove that string
    if filename.startswith("HKQuantityTypeIdentifierApple"):
        new_filename = filename.replace("HKQuantityTypeIdentifierApple", "")

    # If the file name starts with "HKQuantityTypeIdentifier", remove that string
    elif filename.startswith("HKQuantityTypeIdentifier"):
        new_filename = filename.replace("HKQuantityTypeIdentifier", "")
        
    # If the file name starts with "HKCategoryTypeIdentifier", remove that string
    elif filename.startswith("HKCategoryTypeIdentifier"):
        new_filename = filename.replace("HKCategoryTypeIdentifier", "")
        
    # If the file name starts with "HKCategoryTypeIdentifier", remove that string
    elif filename.startswith("HKDataType"):
        new_filename = filename.replace("HKDataType", "")

    # Rename the file if the new name is different from the original name
    if new_filename != filename:
        original_path = os.path.join(data_directory, filename)
        new_path = os.path.join(data_directory, new_filename)
        os.rename(original_path, new_path)
