#Data Needed:total votes cast
# list of candidates who got votes
# % of votes candidates received,
# winner of election pop vote
#collect total votes cast
#go through list calculate % of votes for each candidate 
# while generating list of candidates
#find largest % of votes

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resource", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print headers
    headers = next(file_reader)
    print(headers)