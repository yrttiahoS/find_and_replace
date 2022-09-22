# Script for replacing ID values (string or number) in xlsx files accoriding to an external map file.
# Can be used to e.g., anonymize content.
#
# To apply for your data, check your data format (columns to modify, datatype, encodig of ID in filenames, etc.)
#
# Python things to use 
# 1) Pandas for xlsx processing. Load, manipulate, and save
import datetime
import pandas as pd

# folder and file for input
# input file is the target file to be anonymized
# map file contains old IDs and new anon IDs
input_folder =      'your path goes here/'
input_file =        'your_target_file.xlsx'
map_file =          'your_map_file_fullpath.xlsx'
map_file_sheet =    '#name_of_sheet'
# folder and file for output
output_folder =     'your_output_folder/'
output_file =       'name_for_new_version_of_target_file_noextension'


# Make date string for output filename.
date_today = str(datetime.date.today())

# Constants used in selecting columns from external file table (map file)
COLUMN_MAP_NEWNAME = 5 # column containing new ID values
COLUMN_MAP_OLDNAME = 1 # column containing old ID values
COLUMN_QC_ID = 0       # column containing old ID values, in the target file

# Import files
# map file
xlsx = pd.ExcelFile(map_file)
df_map = pd.read_excel(xlsx, map_file_sheet) #sheet of adult eeg filenames
# video qc file (or any target file to be anonymized...)
xlsx2 = pd.ExcelFile(input_folder + input_file)
df_qc = pd.read_excel(xlsx2)
# You should never modify something you are iterating over
# ...So make new df_qc
df_qc_new = df_qc.copy()
#ititialize ID column of new df!
df_qc_new.iloc[1:len(df_qc.index),COLUMN_QC_ID] = " _"

#Info about files
df_map.info
print(len(df_map.index)) #number of rows
df_qc.info
print(len(df_qc.index))  #number of rows
print(df_map.columns[COLUMN_MAP_OLDNAME]) #name of column
print(df_map.columns[COLUMN_MAP_NEWNAME]) #name of column
print(df_qc.columns[COLUMN_QC_ID]) #name of column
            
# Update qc data, row by row (updated to copy of data frame)
for i, row_qc in df_qc.iterrows():
    
    #find id of qc row in map file
    for j, row_map in df_map.iterrows():
        
        # First check that ID values are acceptable (should be of specific typa and not be NaN)
        check_oldname = isinstance(row_map[COLUMN_MAP_OLDNAME],str)
        check_newname = not(pd.isna(row_map[COLUMN_MAP_NEWNAME]))
        if check_oldname and check_newname:
            # Check if matching ID found on row of map file
            if row_map[COLUMN_MAP_OLDNAME][0:6] == row_qc[COLUMN_QC_ID]:        
                # Update new anon ID to processed target file 
                df_qc_new.iloc[i,COLUMN_QC_ID] = str(int(row_map[COLUMN_MAP_NEWNAME]))
            
print("loop completed!")

# Save data.
df_qc_new.to_excel(output_folder + output_file + date_today + ".xlsx", index=False) 

# Everething is completed
print("Done.")
