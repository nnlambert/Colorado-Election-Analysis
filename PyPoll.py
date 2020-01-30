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

#Initialize a total vote counter
total_votes = 0 

# Candidate Options 
candidate_options = []

# Declaring an empty dictionary to fill with candidate:voter
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    file_reader = csv.reader(election_data)
    
# To do: perform analysis
    # Print the header row
    headers = next(file_reader)
    for row in file_reader:

        # Add to total Vote Count
        total_votes += 1 

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate options
            candidate_options.append(candidate_name)

            # 2. Begin tracking the candidate's votes
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the candidate list
print(candidate_options)

# Print the candidate vote dictionary
print(candidate_votes)

# Print the candidate name from each 
print(total_votes)

# Determine the percentage of votes for each candidate by 
#looping through the counts

# 1. Iterate through the candidate list.
for candidate in candidate_votes:

    #2. Retrieve vote count of a candidate
    vote = candidate_votes[candidate]

    #3. Calculate the percentage of votes
    vote_percentage = round(int(vote) / int(total_votes) * 100)

    #4. Print the candidate name and percentage of votes
    print(f"{candidate} received {vote_percentage}% of the vote.")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count
    if (vote > winning_count) and (vote_percentage > winning_percentage):
        # if true set winning_count = votes and winning_percent = 
        # vote percentage
        winning_count = vote
        winning_percentage = vote_percentage
        # and set the winning_candidate = to candidate's name
        winning_candidate = candidate
        
        #Quick Summary of the results
        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
print(f"{candidate}: {vote_percentage:.1f}% ({vote:,})\n")

# now time to print the winner
#print(f"{winning_candidate} won the election with {winning_percentage}% of the vote and {winning_count} total votes")

# Close the file.
election_data.close()

#dir os
