# import modules
import os
import csv

# file path for csv
csv_file = os.path.join("Resources", "budget_data.csv")

# open csv file
with open(csv_file, "r") as file:
    csvreader = csv.reader(file)
    # skip header row
    header = next(csvreader)
    # intialize variables
    months = 0
    total = 0
    profitloss = []
    profitlossdif = []

    # loop through rows
    for row in csvreader:
        months += 1
        total += int(row[1])
        profitloss.append(int(row[1]))

    # loop through profitloss list to find difference
    for i in range(1,len(profitloss)):
        profitlossdif.append(profitloss[i] - profitloss[i-1])
    #for i in range(len(profitlossdif))
        #if profitlossdif[i] > max:
            #max = profitlossdif[i]
    # find average diff
    average = round(sum(profitlossdif)/len(profitlossdif),2)
    
    # print out results
    print("Financial Analysis")
    print("--------------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: ${max(profitlossdif)}")
    print(f"Greatest Decrease in Profits: ${min(profitlossdif)}")
    
    
