'''
The data we need to retrieve
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote
'''
import datetime
import csv
import random
import numpy
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election-Analysis","Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Election-Analysis","analysis", "election_analysis.txt")

#Using the open() function with the "w" mode we will write the data to file. 
with open(file_to_save, "w") as txt_file:

    #Write some data to the file
    txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")

#Close the file
txt_file.close()

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    print(election_data)

# To do: perform analysis.
with open(file_to_load, 'r') as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
     #   print(row)
    
# Close the file.
election_data.close()

#dir os

