# Election Analysis
## Overview of Analysis
The objective of this analysis was to use python to audit and confirm the results of a local election. The election results were provided as a CSV file. From the results; the total votes, total votes for each candidate, percent of votes for each candidate, votes by county, percentage of votes by county, largest county turnout, and the candidate with the most votes were calculated and saved to a text file.

## Election Audit Results
The results of the election audit are listed below:
* The total number of votes in the election was 369,711  
![Total Votes Image](https://github.com/dkristek/election-analysis/blob/main/Resource/total_votes.png)
* Jefferson County had 10.5% (38,855) of votes
* Denver County had 82.8% (306,055) of votes
* Arapahoe had 6.7% (24,801) of votes  
![County Votes Breakdown](https://github.com/dkristek/election-analysis/blob/main/Resource/county_breakdown.png)
* Denver County had the largest turnout with 306,055 votes  
![Largest County Turnout](https://github.com/dkristek/election-analysis/blob/main/Resource/largest_county.png)
* Charles Casper Stockham had 23.0% (85,213) of votes
* Diana DeGette had 73.8% (272,892) of votes
* Raymon Anthony Doane had 3.1% (11,606) of votes  
![Candidate Vote Breakdown](https://github.com/dkristek/election-analysis/blob/main/Resource/candidate_breakdown.png)
* Diana DeGette won the election with 73.8% (272,892) of votes  
![Winner Statement](https://github.com/dkristek/election-analysis/blob/main/Resource/winner_statement.png)
## Summary
In summary, Python was used to analyze the results of the election. WIth some modifications this script can be adapted for use on various other elections. In this script, the vote percentage that each county received was determined. This can be changed to fit the scale of the election being audited. For example, in a nationwide election the statements that calculate the county voting percentages can be repurposed to collect the voting data for States/Provinces. The names of the variables that tracked the county statistics would be changed to fit the needed administrative division and the lines of code that collect the data can be changed to select from the column that contains the new data. This example is explored further in section below.
<details>
  <summary> State Adjustment</summary>
  
```
   # This can be changed to State
   # 3: Extract the county name from each row.
        county_name = row[1]
   # County becomes state x can be changed to whatever row contains
   # the state data in the new csv file
        state_name =row[x]
```
```
  # The rest of the county related code can also be changed
   if state_name not in state_list:

            # 4b: Add the existing county to the list of counties.
            state_list.append(state_name)

            # 4c: Begin tracking the county's vote count.
            state_votes[state_name] = 0

        # 5: Add a vote to that county's vote count.
        state_votes[state_name] += 1
  ```
  </details>

The code can also work for elections with more candidates and more voting jurisdictions. The code could also be altered to account for runoff elections. Code can be added to the statement that determine the winner of the election to add a margin for victory. As an example, the original code and possible modification for a run-off is in the collapisble sections below.
<details>
  <summary>Original Code!</summary>
  
```
   # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
```
</details>

<details>
  <summary>Run-off!</summary>
  
  ```
  # Determine winning vote count, winning percentage, and candidate.
  # Accounting for a run-off. Let's set the margin of victory to >5%
  #This statement determines the winner if the votes are bigger and the percentage is larger than 5% more than the previous highest candidate
        if (votes > winning_count) and (vote_percentage - winning_percentage > 5):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
  
  #Elif statement determines the two runoff candidates if they meet the requirements for a runoff
        elif (votes > winning_count) and (vote_percentage - winning_percentage <= 5):
            count_candidate1 = votes                                                                      
            runoff_candidate1 = candidate_name
            candidate_percentage1 = vote_percentage
            count_candidate2 - winning_count                                                                     
            runoff_candidate2 = winning_candidate
            candidate_percentage2 = winning_percentage                                                                        
```
</details>
 
  These are just some of the ways that the script can be adapted to other elections. 
