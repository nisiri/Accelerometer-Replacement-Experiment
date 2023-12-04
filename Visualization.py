"""
Provide visualization of calibration data compared with collected data

Experiment:
    17_Sensor Replacements With FEEL Calibrations

Contributor(s):
    Zadok Tahsoh <zadoknt_asset@outlook.com>
    Benjamin Davis <btdavis@asset-us.com>

Change Log
----------
- 2023-07-21 :: Created Force Difference Graph
- 2023-07-25 :: Added Localization Accuracy and Force Error
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% LOAD DATA

test_group_A = r"C:\Users\zadok\Desktop\ASSET\Exp17\results\results_calibration-group-A_test-group-A_2023-07-07T141712.xlsx"
test_group_B = r"C:\Users\zadok\Desktop\ASSET\Exp17\results\results_calibration-group-A_test-group-B_2023-07-14T141316.xlsx"
test_group_C = r"C:\Users\zadok\Desktop\ASSET\Exp17\results\results_calibration-group-A_test-group-C_2023-07-14T144321.xlsx"

#%% READ DATA
# Read data from each sheet in the Excel file
df_read_A = pd.read_excel(test_group_A, sheet_name='corr - FEEL Summary')
df_read_B = pd.read_excel(test_group_B, sheet_name='corr - FEEL Summary')
df_read_C = pd.read_excel(test_group_C, sheet_name='corr - FEEL Summary')	

# Read data for the different graphs
# Localization Accuracy
localization = df_read_A ['2.1.4'].iloc[17][:-13]
localization2 = df_read_B ['2.1.4'].iloc[17][:-13]
localization3 = df_read_C ['2.1.4'].iloc[17][:-13]

# Force Difference
fd_force_mean = df_read_A ['2.1.4'].iloc[21]
fd_force_mean2 = df_read_B ['2.1.4'].iloc[21]
fd_force_mean3 = df_read_C ['2.1.4'].iloc[21]

fd_force_std = df_read_A['2.1.4'].iloc[23][-8:-3]
fd_force_std2 = df_read_B['2.1.4'].iloc[23][-8:-3]
fd_force_std3 = df_read_C['2.1.4'].iloc[23][-8:-3]

# Force Error
fe_force_mean = df_read_A ['2.1.4'].iloc[26][:-1]
fe_force_mean2 = df_read_B ['2.1.4'].iloc[26][:-1]
fe_force_mean3 = df_read_C ['2.1.4'].iloc[26][:-1]

fe_force_std = df_read_A['2.1.4'].iloc[28][-9:-5]
fe_force_std2 = df_read_B['2.1.4'].iloc[28][-9:-5]
fe_force_std3 = df_read_C['2.1.4'].iloc[28][-9:-5]

#%% GRAPHS

# Localization Accuracy
x = [float(localization), float(localization2), float(localization3)]
y = [float(localization), float(localization2), float(localization3)]

fig, ax = plt.subplots()


ax.set(xlim=(0, 3), ylim=(0, 100),
       xticks=np.arange(3), xticklabels=['test_group_A', 'test_group_B', 'test_group_C'],
       yticks=np.arange(0, 100, 10))
ax.bar(np.arange(3), y, color=['red', 'orange', 'green'], alpha=0.7, capsize=6, label='Localization Accuracy')

# tick_colors = ['red', 'orange', 'green']
# for tick_label, color in zip(ax.get_xticks(), tick_colors):
#     tick_label.set_color(color)

ax.set_title('Localization')
plt.ylabel('Localization Accuracy (%)')
plt.legend()

plt.show()

#%% Force Difference
x = [float(fd_force_mean), float(fd_force_mean2), float(fd_force_mean3)]
# Force Difference
y = [float(fd_force_mean), float(fd_force_mean2), float(fd_force_mean3)]
yerr = [float(fd_force_std), float(fd_force_std2), float(fd_force_std3)]

fig, ax = plt.subplots()

ax.set(xlim=(0, 100), xticks=np.arange(0, 100, 10),
       ylim=(0, 150), yticks=np.arange(0, 150, 20))

ax.plot(x, y, color='steelblue')
ax.errorbar(x, y, yerr, linewidth=2, capsize=6)
ax.set_title('Force Difference')
plt.ylabel('Force Difference (lbf)')

plt.plot(x[0],y[0], 's', label='test_group_A', color='red')
plt.plot(x[1],y[1], 's', label='test_group_B', color='orange')
plt.plot(x[2],y[2], 's', label='test_group_C', color='green')
plt.legend()

plt.show()

#%% Force Error
x = [float(fe_force_mean), float(fe_force_mean2), float(fe_force_mean3)]
y = [float(fe_force_mean), float(fe_force_mean2), float(fe_force_mean3)]
yerr = [float(fe_force_std), float(fe_force_std2), float(fe_force_std3)]

fig, ax = plt.subplots()

ax.set(xlim=(0, 30), xticks=np.arange(0, 30, 5),
       ylim=(0, 30), yticks=np.arange(0, 30, 5))

ax.plot(x, y, color='steelblue')
ax.errorbar(x, y, yerr, linewidth=2, capsize=6)
ax.set_title('Force Error')
plt.ylabel('Force Error (lbf)')

plt.plot(x[0],y[0], 's', label='test_group_A', color='red')
plt.plot(x[1],y[1], 's', label='test_group_B', color='orange')
plt.plot(x[2],y[2], 's', label='test_group_C', color='green')
plt.legend()

plt.show()