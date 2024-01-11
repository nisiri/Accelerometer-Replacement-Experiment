import os
import pandas as pd

# Function to navigate through folders and read text files
def read_text_files(folder_path):
    data = []
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith(".txt"):  # Check if the file is a text file
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'r') as file:
                    content = file.read()
                    data.append({'Filename': filename, 'Content': content})
    return data

# Specify the folder path you want to start navigating from
folder_path = "C:/Users/zadok/OneDrive/17_Sensor Replacements With FEEL Calibrations/data/original2"

# Read text files and organize data into a DataFrame
file_data = read_text_files(folder_path)
df = pd.DataFrame(file_data)

# Print the DataFrame
print(df)

# You can now use the 'df' DataFrame for further analysis or processing
