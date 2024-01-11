#Data Converter
"""
Adjusts the sensitivity for the data for a mislabelled sensor during data collection

Experiment:
    17_Sensor Replacements With FEEL Calibrations

Contributor(s):
    Zadok Tahsoh <zadoknt_asset@outlook.com>

Change Log
----------
- 2023-12-07 :: Completed and ran script successfully
"""
import os
import pandas as pd

            #%% Setting
location = 'location'
group = 'hammer-small-mediumtip_group-C'
event = 'hammer-small-mediumtip'

# Specify the folder path you want to start navigating from
datadir = r'C:\Users\zadok\OneDrive\17_Sensor Replacements With FEEL Calibrations\data\original'

#Sensors to be replaced
old = '54125'
new = '70496'

# Sensor Sensitivities
SN54125 = 10.39
SN70496 = 10.16

scale = SN54125 / SN70496

#%% Navigate through folders and read text files


for location in os.listdir(datadir):
    for group in os.listdir(os.path.join(datadir, location)):
        if group.endswith("C"):
            for event in os.listdir(os.path.join(datadir, location, group)):
                 if event.endswith(("16.txt", "17.txt", "18.txt", "19.txt", "20.txt")):     #adjust files to be converted
                     event = os.path.join(datadir, location, group, event)
                     with open(event, 'r+') as file:
                         lines = file.readlines()
                         print(lines[5], location)       #confirm task at hand
                         if old in lines[2]:
                              sensors = lines[2].replace(old, new)      # replaces the sensor name
                              lines[2] = sensors
                              file.seek(0)
                              file.writelines(lines)
                         else:
                              print(event, 'old sensor not found')
                         content = lines[4:]  #Ignore the first 5 lines of the files
                         numbers = [[float(num) for num in line.strip().split()] for line in content] #Extracts number values from lines and saves in separate columns
                         df = pd.DataFrame(numbers)
                         sens_data = []
                         for num in df.iloc[:,1]:    #accessing the data column to be changed
                           sens_data = pd.concat([df.iloc[:, 1], pd.Series([num * scale for num in df.iloc[:, 1]])], ignore_index=True, axis=0)
                           df.iloc[:, 1] = sens_data
                           data = df.to_csv(index=False, header=False).split()[1:]
                           new_data = (line.replace(',', ' ') for line in data)
                           file.seek(0)
                           for _ in range(5):    #moves the cursor to line 6 of each file
                               file.readline()
                               file.writelines(new_data)
                           





