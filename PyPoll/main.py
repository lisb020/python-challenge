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
    winner = 0
    # intialize candidates dictionary
    candidates = {}

    # loop through rows
    for row in csvreader:
        voter_count += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {voter_count}")
    print("---------------------------")
    for key in candidates:
        value = candidates.get(key)
        percent = round(int(value)/voter_count * 100,3)
        print(f"{key}: {percent}% ({value})")

    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")