# import modules
import os
import csv

# file path for csv
csv_file = os.path.join("Resources", "election_data.csv")

# file path for text file to write to
text_file = os.path.join("analysis", "election_data.txt")

# open csv file
with open(csv_file, "r") as file:
    csvreader = csv.reader(file)
    # skip header row
    header = next(csvreader)
    # intialize variables
    voter_count = 0

    # intialize candidates dictionary
    candidates = {}

    # loop through rows
    for row in csvreader:
        voter_count += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
    # find max value in cadidates dictionary and candidate winner
    winner_value = max(candidates.values())
    # print voter_count results
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {voter_count}")
    print("---------------------------")
    with open(text_file,'w') as txtfile:
        txtfile.writelines(["Election Results\n",
                            "---------------------------\n",
                            "Total Votes: " + str(voter_count) + "\n",
                            "---------------------------\n"])
    # iterate through dictionary and print out person and percent of votes
    for key in candidates:
        value = candidates.get(key)
        decimal = int(value)/voter_count
        percent = "{:.3%}".format(decimal)
        with open(text_file,'a') as txtfile:
            txtfile.writelines(str(key) + ": " + str(percent) + " (" + str(value) + ")\n")
        print(f"{key}: {percent} ({value})")
        if winner_value == candidates.get(key):
            winner = key
    # print out winner
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")
    
    # write to text file
    with open(text_file,'a') as txtfile:
        txtfile.writelines(["---------------------------\n",
                            "Winner: " + winner + "\n",
                            "---------------------------\n"])