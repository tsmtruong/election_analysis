# Election Analysis

## Overview of Election Audit

### Purpose
The purpose of this challenge was to use the various fuunctions of python and VS Code to audit and report the election results from 3 counties and 3 candidates to the election commitee. This information includes the winning percentages, total vote count, voter turnout, county percentages, and the election winner.
## Election Audit Results
1. For the total number of votes casted there were 369,711 votes tabulated overall. This was calculated using a for loop with the names being appended every time the code encoutered it.

2. Of the 369,711 votes 10.5% or 38,855 came from Jefferson County, 6.7% or 24,801 came from Arapahoe County, and  82.8% or 306,055 came from Denver County. This number and percentage was also calculated by usinf loops and conditionals as well as divind by float variables.

3. The county that had the largest number of votes is Denver County with 306,055 of the total votes or 82.8%


4. There were threee candidates for in this election, Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. Charles Casper Stockham recieved 85,213 votes or 23% of the votes. Diana DeGette revieved 272,892 votes or about 73.8% of the votes. Lastly, Raymon Anthony Doane recieved 11,606 votes or 3.1% of the votes.

5. The candidate that won the election by a large margin is Diana DeGette with a total of 272,892 votes or 73.8% of the votes.

[Election Summary](https://github.com/tsmtruong/election_analysis/blob/main/analysis/election_analysis.txt)

[Election Audit Code](https://github.com/tsmtruong/election_analysis/blob/main/PyPoll_Challenge.py)


## Election Audit Summary

The analysis done for the audit was an analysis that can be used synonomously amongst elections. To change the script to use it for other elections the first modification could be a simple replacement of dictionaries, the code that holds all of the name of the candidates and counties. This would then link the code to the information/CSV provided. Another way to change the script is to input the information into a pandas dataframe to make the results more presentable and easier to not only write but read. This would be a simple import script added at the beginning of the analysis.
