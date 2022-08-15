# find_and_replace
#
#
# Script for finding particular string from text files and replacing it/them with zeros.
# Can be used to e.g., anonymize content.
#
# Python version: 3.8.10
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
