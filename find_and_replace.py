# Script for finding particular string from text files and replacing it/them with zeros.
# Can be used to e.g., anonymize content.
#
# Python things to use 
# 1) Open files to read and write!
# 2) No csvwriter or such needed, already opened file object knows how to "write".
#    Write line by line!
# 3) The file is read in as list of strings, where len is number of rows.
#    Use readlines() method!
# 4) List of source files to process is read from extrenal xlsx file using pandas
#
# To use script, change input and output folders below.
# Also modify markers and columns read from your look-up-table to suit the purpose.

from cmath import nan
import os
import pandas as pd

# folder and file for output
output_folder = 'C:/Users/folder' #change to your folder!!!
#output_file = 'newfile.txt'
# folder and file for input
input_folder = 'C:/Users/' #change to your folder!!!
#input_file = 'mock_identifieble_file.txt'

# marker/replacement string to look for in ananonymized source files 
# strings after marker are replaced by replacement string
# change according to need!!!
target_marker = "at"            
replacement_string = '00000000'

# Import data of files to processe
# this is look-up-table with source and target filenames at designated columns
xlsx = pd.ExcelFile("C:/Users/folder")  #change to your folder!!!
df = pd.read_excel(xlsx, "sheet1") #sheet name in xlsx file, change if needed

# Constants used in selecting columns from external file table
COLUMN_FILTER = 4       #columns for file filter, 1=select, otherwise=skip
COLUMN_NEWNAME = 5      #column for new filenames
COLUMN_OLDNAME_IMP = 3  #column for old/source files


# Define function for processing/ananonymizing one file
def anon(output_folder, output_file, input_folder, input_file, target_marker, replacement_string):    
    #open outputfile
    print("enter function anon")
    print("inputname: " + input_file + " outputname: " + output_file)
    with open(os.path.join(output_folder, output_file), "wt",  newline='') as outputfile:    
        #open input file
        with open(os.path.join(input_folder, input_file), "rt") as f:

            # read all lines
            lines = f.readlines()   
            print(f"Number of lines: {len(lines)} ")                                    

            # FIND and REPLACE targets on line 3 (or in python [2]). Target is found after word "at"
            # target example: 220922/18:45:11.634
            # to be ralced always with: 000000/00:00:00.000
            line2_alter = lines[2]            
            char_to_anon_first = line2_alter.find(target_marker) + 3
            char_to_anon_last = len(line2_alter)-2
            line2_alter = line2_alter[char_to_anon_first:char_to_anon_last] 
            print("Target string: " +  line2_alter  + ' set to zeros.')
            lines[2] = lines[2].replace(line2_alter, "000000/00:00:00.000")

            # Write to output, line by line       
            for l in lines:
                outputfile.write(l)  



# Some df processin not used now...
#print(df.index)
#print(df.columns)
#idfs = df.items()
#dfloc = df.iloc[:,2]
#print(dfloc)

# df processing notes...
#Get the number of rows: len(df)
#Get the number of columns: len(df.columns)


# Loop through rows (participant per row)
for i in range(0,len(df)):    
    print(str(i))

    # Select only subset of files to process based on filter variable extranal file/table
    if df.iloc[i,COLUMN_FILTER] == 1:
        output_file = str(round(df.iloc[i,COLUMN_NEWNAME])) + ".imp"
        input_file = str(df.iloc[i,COLUMN_OLDNAME_IMP])
    else:
        continue
    
    # Skip if the source file is missing
    if input_file == "nan": 
        print("continue isnan:" + str(input_file == "nan"))
        continue
    print("do it, dont' skip! (continue)")

    print(output_file + " " + input_file )
    #for j in range(0,len(df.columns)):
     #   print(df.iloc[i,j])

    # do anonymization for indexed file
    anon(output_folder, output_file, input_folder, input_file, target_marker, replacement_string)

# Everething is completed
print("Done.")