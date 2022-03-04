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
In summary, Python was used to analyze the results of the election. WIth some modifications this script can be adapted for use on various other elections. In this script, the vote percentage that each county received was determined. This can be changed to fit the scale of the election being audited. For example, in a nationwide election the statements that calculate the county voting percentages can be repurposed to collect the voting data for States/Provinces. The names of the variables that tracked the county statistics would be changed to fit the needed administrative division and the lines of code that collect the data can be changed to select from the column that contians the new data. [show code ] The code can also work for elections with more candidates and more voting jurisdictions. The code could also be altered to account for runoff elections. Code can be added to the statement that determine the winner of the election to add a margin for victory. [show code for this]
