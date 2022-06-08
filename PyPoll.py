# The data we need to retrieve
# 1. the total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# add our dependencies
import csv

import os


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. initialize a total vote counter
total_votes = 0

 # get candidate names by declaring a new list
candidate_options = []

# declare an empty dictionary
candidate_votes = {}

# winning candidate and winning count tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # print the header row.
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        # 2. add to the total count
        total_votes += 1

        # print the candidate name from each row
        candidate_name = row[2]

        # if the candidate names does not match any existing candidates
        if candidate_name not in candidate_options:

            # add it to the list of candidates
            candidate_options.append(candidate_name)

            # begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate
        candidate_votes[candidate_name] += 1

        # save out results to our text file
with open(file_to_save,"w") as txt_file:

# print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"

        f" --------------------------\n"

        f"Total Votes: {total_votes: ,}\n"

        f"----------------------------\n")

    print(election_results, end="")

    # save the final vote count to the text file
    txt_file.write(election_results)

    # determint the perscentage of votes for each candidate by looping through the counts
    # 1. iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # 3. calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100

        # print out each candidates name, vote count, and percentage of votes to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes: ,})\n")
    
    # print each candidate,  their voter count, and percentage to the terminal
        print(candidate_results)

    # save the candidate results to our text file
        txt_file.write(candidate_results)

        # determine winning vote count and candidate
        # determine if the vote is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
        # if true then set winning_count = votes and winning_percent =
        # vote_percentage
            winning_count = votes

            winning_percentage = vote_percentage

        # and, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name 

    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count: ,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)

    # save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)