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

#create accumulator for total votes
total_votes = 0

#create list to store candidate names
candidate_options=[]

#create dictionary to keep track of votes for each candidate
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print headers
    headers = next(file_reader)
    

    #for loop goes through rows 
    for row in file_reader:
        #counting total votes
        total_votes += 1

        #grabbing candidate name from each row
        candidate_name = row[2]


        #checking if unique
        if candidate_name not in candidate_options:

            #add unique name to candidate list
            candidate_options.append(candidate_name)

            #begin tracking candidate's votes in dictionary
            candidate_votes[candidate_name] = 0
    
        #track candidate votes
        candidate_votes[candidate_name] += 1

#creating dict to store candidate percentages in
candidate_percentages = {}
for candidate_name in candidate_votes:
    
    #getting votes from each candidate
    votes = candidate_votes[candidate_name]

    #calculating vote percentage
    vote_percentage = round(float(votes)/float(total_votes) * 100, 1)

    #printing out the percentage
    print(f"{candidate_name}: {vote_percentage}% ({candidate_votes.get(candidate_name):,}) ")

    #storing to dictionary for later use
    candidate_percentages.update({candidate_name:vote_percentage})
    

#determine winning candidate
#grabs max values for total votes and percentage and saves them to variables
#grabs name of candidate associated with max value in percentages and saves as var
winning_candidate = max(candidate_percentages, key = candidate_percentages.get)
winning_percentage = max(candidate_percentages.values())
winning_total = max(candidate_votes.values())

print(f"""
---------------------------
Winner: {winning_candidate}
Winning Vote Count: {winning_total:,}
Winning Percentage: {winning_percentage}%
----------------------------
""")

    
